#!/usr/bin/env python3
"""Offline structural checks for an original, source-grounded reading guide.

Run from any directory: python scripts/validate_repository.py [--root PATH]
This checks document/metadata integrity, not the truth of research claims.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit


REQUIRED = (
    "README.md", "AGENTS.md", "LLMS.txt", "CITATION.cff", "LICENSE",
    "ATTRIBUTION.md", "CONTRIBUTING.md", "VERIFICATION.md",
    "metadata/paper.json", "metadata/claims.json", "metadata/sources.json",
    "references/paper.bib",
)


def unfence(text: str) -> str:
    """Keep line positions while removing fenced examples from link analysis."""
    result = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = (marker[0], len(marker))
            elif marker[0] == fence[0] and len(marker) >= fence[1]:
                fence = None
            result.append("")
        else:
            result.append("" if fence else line)
    return "\n".join(result)


def slug(heading: str) -> str:
    heading = re.sub(r"<[^>]*>", "", heading)
    heading = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", heading)
    heading = heading.replace("`", "").strip().lower()
    heading = "".join(c for c in heading if c in " -_" or unicodedata.category(c)[0] in "LMN")
    return heading.replace(" ", "-")


def anchors(text: str) -> set[str]:
    clean = unfence(text)
    result = set(re.findall(r"\b(?:id|name)=[\"']([^\"']+)[\"']", clean))
    counts: dict[str, int] = {}
    lines = clean.splitlines()
    for i, line in enumerate(lines):
        match = re.match(r"^ {0,3}#{1,6}\s+(.*?)(?:\s+#+)?\s*$", line)
        heading = match.group(1) if match else None
        if heading is None and i + 1 < len(lines) and line.strip() and re.match(r"^ {0,3}(?:=+|-+)\s*$", lines[i + 1]):
            heading = line.strip()
        if heading is not None:
            base = slug(heading)
            count = counts.get(base, 0)
            candidate = base if count == 0 else f"{base}-{count}"
            while candidate in result:
                count += 1
                candidate = f"{base}-{count}"
            counts[base] = count + 1
            result.add(candidate)
    return result


def link_destinations(text: str):
    """Inline links/images, reference definitions and explicit HTML href/src."""
    clean = unfence(text)
    # URLs in parentheses are handled with a balanced-parenthesis scan below.
    for match in re.finditer(r"!?\[(?:[^\]\\]|\\.)*\]\(", clean):
        start = match.end()
        if start < len(clean) and clean[start] == "<":
            end = clean.find(">", start + 1)
            if end >= 0:
                yield clean[start + 1:end]
            continue
        depth, index = 1, start
        while index < len(clean):
            char = clean[index]
            if char == "\\":
                index += 2
                continue
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if not depth:
                    value = clean[start:index].strip()
                    # An optional quoted link title follows whitespace.
                    value = re.split(r"\s+[\"']", value, maxsplit=1)[0]
                    yield value
                    break
            index += 1
    for match in re.finditer(r"^ {0,3}\[[^\]]+\]:\s*(?:<([^>]+)>|(\S+))", clean, re.M):
        yield match.group(1) or match.group(2)
    yield from re.findall(r"\b(?:href|src)=[\"']([^\"']+)[\"']", clean)


def records(value, key: str):
    return value.get(key, []) if isinstance(value, dict) else value if isinstance(value, list) else []


def author_parts(author):
    if isinstance(author, str):
        return [author]
    if isinstance(author, dict):
        for field in ("name", "full_name"):
            if author.get(field):
                return [str(author[field])]
        return [str(author[field]) for field in ("given", "family", "given-names", "family-names", "given_names", "family_names") if author.get(field)]
    return []


def normalized(text: str) -> str:
    return " ".join(re.findall(r"\w+", unicodedata.normalize("NFKC", text).casefold()))


def check(root: Path) -> int:
    errors: list[str] = []
    counters = {"files": 0, "links": 0, "claims": 0, "sources": 0}

    def fail(message):
        errors.append(message)

    for path in REQUIRED:
        if not (root / path).is_file():
            fail(f"Missing required file: {path}")
    docs = sorted((root / "docs").glob("*.md"))
    if len(docs) < 5:
        fail("Expected at least five reading modules in docs/*.md")

    files = [p for p in root.rglob("*") if p.is_file() and ".git" not in p.relative_to(root).parts and "__pycache__" not in p.parts]
    counters["files"] = len(files)
    for path in files:
        rel = path.relative_to(root).as_posix()
        if path.suffix.lower() == ".pdf":
            fail(f"Source PDF must not be redistributed: {rel}")
        if path.suffix.lower() in {".md", ".txt"}:
            content = path.read_text(encoding="utf-8-sig")
            if "<PARSED TEXT FOR PAGE:" in content:
                fail(f"Extracted source text marker found: {rel}")
            if path.suffix.lower() == ".txt" and rel != "LLMS.txt" and any(part.lower() in {"source", "sources"} for part in path.relative_to(root).parts[:-1]):
                fail(f"Possible source transcription must stay outside guide: {rel}")

    cache: dict[Path, set[str]] = {}
    for path in files:
        if path.suffix.lower() not in {".md", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8-sig")
        for destination in link_destinations(text):
            counters["links"] += 1
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc or destination.startswith("//"):
                continue
            decoded = unquote(parsed.path)
            if not decoded and not parsed.fragment:
                fail(f"Empty link in {path.relative_to(root)}")
                continue
            target = (root / decoded.lstrip("/") if decoded.startswith("/") else path.parent / decoded).resolve() if decoded else path.resolve()
            try:
                target.relative_to(root)
            except ValueError:
                fail(f"Link leaves repository in {path.relative_to(root)}: {destination}")
                continue
            if not target.exists():
                fail(f"Broken local link in {path.relative_to(root)}: {destination}")
            elif parsed.fragment and target.is_file() and target.suffix.lower() in {".md", ".txt"}:
                if target not in cache:
                    cache[target] = anchors(target.read_text(encoding="utf-8-sig"))
                if unquote(parsed.fragment) not in cache[target]:
                    fail(f"Broken heading anchor in {path.relative_to(root)}: {destination}")

    metadata = {}
    for name in ("paper", "claims", "sources", "results"):
        path = root / "metadata" / f"{name}.json"
        if path.is_file():
            try:
                def reject_constant(value):
                    raise ValueError(f"Nonstandard JSON numeric constant: {value}")
                metadata[name] = json.loads(path.read_text(encoding="utf-8-sig"), parse_constant=reject_constant)
            except (ValueError, OSError) as exc:
                fail(f"Invalid metadata/{name}.json: {exc}")

    paper = metadata.get("paper", {})
    page_count = paper.get("pdf_page_count", paper.get("page_count")) if isinstance(paper, dict) else None
    if not isinstance(paper, dict) or not paper.get("title") or not paper.get("authors"):
        fail("paper.json must identify title and complete author list")
    if page_count is not None and (isinstance(page_count, bool) or not isinstance(page_count, int) or page_count < 1):
        fail("paper.json page count must be a positive integer")
        page_count = None

    source_rows = records(metadata.get("sources", {}), "sources")
    claim_rows = records(metadata.get("claims", {}), "claims")
    source_ids: set[str] = set()
    source_page_counts: dict[str, int] = {}
    for row in source_rows:
        if not isinstance(row, dict) or not row.get("id"):
            fail("Every source needs a nonempty id")
            continue
        sid = row["id"]
        if not isinstance(sid, str):
            fail("Source id must be a string")
            continue
        if sid in source_ids:
            fail(f"Duplicate source id: {sid}")
        source_ids.add(sid)
        source_pages = row.get("pdf_page_count", row.get("page_count"))
        if source_pages is not None:
            if isinstance(source_pages, bool) or not isinstance(source_pages, int) or source_pages < 1:
                fail(f"Source {sid} page count must be a positive integer")
            else:
                source_page_counts[sid] = source_pages
        if row.get("url") and urlsplit(str(row["url"])).scheme not in {"http", "https"}:
            fail(f"Source {sid} has an invalid public URL")
    if not source_ids:
        fail("sources.json must contain at least one source")
    counters["sources"] = len(source_rows)

    def walk_evidence(value, label, refs, inherited_source=None):
        if isinstance(value, list):
            for child in value:
                walk_evidence(child, label, refs, inherited_source)
        elif isinstance(value, dict):
            local_source = value.get("source_id", inherited_source)
            local_page_count = source_page_counts.get(local_source, page_count) if isinstance(local_source, str) else page_count
            for key, child in value.items():
                if key in {"source_id", "source_ids"}:
                    values = child if isinstance(child, list) else [child]
                    for sid in values:
                        if not isinstance(sid, str) or sid not in source_ids:
                            fail(f"{label} references unknown source id: {sid}")
                        else:
                            refs.add(sid)
                if key in {"page", "pages", "pdf_page", "pdf_pages"}:
                    values = child if isinstance(child, list) else [child]
                    for page in values:
                        # Text ranges such as '5-7' remain human-reviewed.
                        if isinstance(page, int) and (page < 1 or (local_page_count and page > local_page_count)):
                            fail(f"{label} has out-of-range PDF page: {page}")
                walk_evidence(child, label, refs, local_source)

    claim_ids = set()
    for row in claim_rows:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"]:
            fail("Every claim needs a nonempty string id")
            continue
        cid = row["id"]
        if cid in claim_ids:
            fail(f"Duplicate claim id: {cid}")
        claim_ids.add(cid)
        if not any(row.get(key) for key in ("statement", "claim", "text", "summary")):
            fail(f"Claim {cid} needs a statement")
        refs = set()
        walk_evidence(row, f"Claim {cid}", refs)
        if not refs:
            fail(f"Claim {cid} has no registered source_id/source_ids")
    if not claim_rows:
        fail("claims.json must contain source-grounded claims, including conceptual claims where appropriate")
    counters["claims"] = len(claim_rows)

    if "results" in metadata:
        result_data = metadata["results"]
        if not isinstance(result_data, list) and not (isinstance(result_data, dict) and isinstance(result_data.get("results"), list)):
            fail("results.json must be a list or an object containing a results list")
        result_rows = records(result_data, "results")
        result_ids = set()

        def walk_claim_refs(value, label):
            if isinstance(value, list):
                for child in value:
                    walk_claim_refs(child, label)
            elif isinstance(value, dict):
                for key, child in value.items():
                    if key in {"claim_id", "claim_ids"}:
                        values = child if isinstance(child, list) else [child]
                        for cid in values:
                            if not isinstance(cid, str) or cid not in claim_ids:
                                fail(f"{label} references unknown claim id: {cid}")
                    walk_claim_refs(child, label)

        # File-level provenance is checked even when each result also has locators.
        file_refs = set()
        walk_evidence(result_data, "Results metadata", file_refs)
        walk_claim_refs(result_data, "Results metadata")
        for row in result_rows:
            if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"]:
                fail("Every result needs a nonempty string id")
                continue
            rid = row["id"]
            if rid in result_ids:
                fail(f"Duplicate result id: {rid}")
            result_ids.add(rid)
            refs = set()
            walk_evidence(row, f"Result {rid}", refs)
            if not refs:
                fail(f"Result {rid} has no registered source_id/source_ids")
        counters["results"] = len(result_rows)

    if isinstance(paper, dict):
        for filename in ("CITATION.cff", "references/paper.bib"):
            path = root / filename
            if not path.is_file():
                continue
            citation = normalized(path.read_text(encoding="utf-8-sig"))
            for author in paper.get("authors", []):
                parts = author_parts(author)
                if not parts:
                    fail(f"Cannot parse author record: {author}")
                # CFF and BibTeX can reverse family/given order, so compare name tokens.
                for part in parts:
                    tokens = normalized(part).split()
                    if any(token not in citation.split() for token in tokens):
                        fail(f"{filename} is missing author name component: {part}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAIL: {len(errors)} issue(s)", file=sys.stderr)
        return 1
    print("PASS: " + ", ".join(f"{value} {key}" for key, value in counters.items()))
    print("Checked local links/anchors, source/claim/result IDs, integer page bounds, author credits, and source-redistribution guards.")
    print("Research accuracy, external URL availability, source equivalence, and publication visibility require separate review.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"Root is not a directory: {root}")
    return check(root)


if __name__ == "__main__":
    raise SystemExit(main())
