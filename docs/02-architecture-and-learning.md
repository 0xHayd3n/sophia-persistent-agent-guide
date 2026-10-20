# 2. Architecture and learning

[Guide home](../README.md) · [Previous: concepts](01-concepts-and-context.md) · [Next: pilot](03-pilot-and-evidence.md)

## Follow the data, not just the labels

Figure 3 places the environment below perception/action, deliberate reasoning above it, and executive supervision at the top. Memory, user modeling, self modeling, and hybrid reward supply context to the executive. Outcomes flow back into memory and rewards. The diagram includes an RL policy-update path, but the pilot does not execute runtime weight updates. [Figure 3 and §4.1, p. 7](https://arxiv.org/pdf/2512.18202v1#page=7).

A companion restatement of the proposed flow is:

```text
environment event
  -> encode and timestamp
  -> executive consults memory, user model, self model
  -> search and critique candidate goals/plans
  -> deliberate planner produces a command
  -> actuator performs primitive actions
  -> verifier + reflection supply feedback
  -> update stored episodes/context; choose next goal
```

This is an explanation of the design, not runnable pseudocode or a reproduction of the implementation.

## Persistent-POMDP notation

The paper writes its model as
`H = <S, O, A1, T, Ω, Rext, γ, (π1, π2, π3), D>`.
The equations in this section are explanatory formalizations; the paper gives no theorem establishing convergence or general lifelong learning. [§4.1, p. 7](https://arxiv.org/pdf/2512.18202v1#page=7).

| Symbol | Role |
| --- | --- |
| S, s_t | World-state space and current hidden state |
| O, o_t | Observation space and current observation |
| A1, a_t | Primitive action space and executed action |
| T | Transition distribution from state and action to next state |
| Ω | Observation/emission distribution conditioned on world state |
| Rext | External task reward |
| γ | Discount factor in [0, 1) |
| π1, π2, π3 | Action, deliberation, and supervisory policies |
| D | System context including memory, self-model, and reasoning context |

Partial observability matters because the supervisor does not see the full world state. A user model and recalled episode are fallible contextual inputs, not direct access to another person's intentions.

## System 1: encoding and action

An encoder `E` maps observations to typed events `x_t = E(o_t)`. The general design names CLIP and Whisper as examples, not as a documented list of models deployed in the browser pilot. Tool wrappers or optional robot controllers translate an upper-level command into primitive actions. Action outcomes provide external feedback. [§4.1.1, p. 8](https://arxiv.org/pdf/2512.18202v1#page=8).

## System 2: deliberate planning

The planner receives a goal, short-term scratchpad, and observation history. An LLM generates a response, and a parser turns it into a machine-executable command. The compact policy expression means “sample a plan-like response, then parse it”; it is not a full specification of tool validation or failure recovery.

The subsequent gradient-ascent expression proposes updating planner parameters to increase expected discounted hybrid reward over a finite horizon. It includes a learning rate and reward discounting. It does not report an optimizer, dataset, or trained pilot model. **§5.1.2 explicitly states that the actual deployment never changes runtime parameters.** [§4.1.2, p. 8](https://arxiv.org/pdf/2512.18202v1#page=8); [§5.1.2, p. 10](https://arxiv.org/pdf/2512.18202v1#page=10).

## System 3: executive routines

The executive's meta-policy outputs a goal, intrinsic reward definition, and weighting parameter β from executive context, retrieved memory, and the self-model. The description mentions a Python orchestration loop, event broker, and priority queue. Detailed code and scheduling configuration are not included.

1. **Thought search** grows a tree of partial plans with estimated utility. Breadth or beam expansion stops when utility passes a threshold or the search budget runs out; a high-valued leaf supplies the chosen output.
2. **Process supervision** asks a secondary guardian LLM to critique new nodes for consistency and safety. It may prune bad branches or annotate repairs. “Critiqued” does not mean formally verified.
3. **Reflection** compares predicted and realized outcomes after an episode, revises mistakes, and extracts reusable heuristics.

The paper does not specify the value estimator, threshold training, exact prompts, beam width, or a complete mapping from a selected leaf to every meta-policy output. A notation such as argmax identifies a selection intention, not those missing implementation decisions. [§4.1.3, pp. 8–9](https://arxiv.org/pdf/2512.18202v1#page=8).

## Four supporting services

| Service | Proposed information or transformation | Open implementation question |
| --- | --- | --- |
| Memory | Update an episodic store using observations, actions, rewards, goals, and context; retrieve through vector search and optionally a graph | Which memories are admitted, revised, forgotten, or rejected as stale? |
| User modeling | Track goals, knowledge, and affect | How is an inferred user belief checked and corrected? |
| Hybrid reward | Combine external feedback and intrinsic drives using β; permit numeric or natural-language representations | How are linguistic rewards ranked and balanced consistently? |
| Self-model | Maintain state, capabilities, and terminal creed, updated through reflection | What verifies a newly claimed capability? |

The mention of Natural Language Reinforcement Learning points to related work by Feng et al.; it does not demonstrate that a parameter-training procedure ran here. In the pilot, feedback components are concatenated as natural language. Do not impose a fixed arithmetic mixture on that implementation. [§4.1.3, p. 9](https://arxiv.org/pdf/2512.18202v1#page=9).

## Autonomous cognitive cycle

§4.2 describes a hypothetical API competence gap: a poor outcome triggers supervisor attention; the self-model helps diagnose a deficit; the system proposes a remedial learning objective; search and critique choose a plan; lower layers execute it; reflection and memory retain the outcome.

The cycle illustrates an intended feedback structure. Its final description of improved competence is not a separate controlled experiment. A failed plan could be stored or a guardian could miss an error; those cases require evaluation rather than being excluded by the architecture. [§4.2, p. 9](https://arxiv.org/pdf/2512.18202v1#page=9).
