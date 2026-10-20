---
type: concept
status: active
visibility: private
created: 2026-07-27
parent: "[[AI Safety]]"
tags: [ai-safety, foundations]
---

# AI Safety: the map and the case

Step 1 of the [[AI Safety]] route. The goal here is orientation, not depth: name the sub-fields so later steps have somewhere to live, state the core argument for why the field exists, and sketch the camps I'll keep running into.

## "AI safety" is four different problems under one name

"AI safety" is an umbrella term, and most of the confusion around it comes from people using it for four different things at once. Splitting them apart helps.

- **Alignment:** getting a system to pursue what its designers or users actually intend, rather than a proxy (a stand-in measure) that only looks right. This is the technical core.[^ngo]
- **Robustness:** the system keeps behaving well under distribution shift (inputs unlike the ones it was trained on), adversarial pressure, and strange inputs such as jailbreaks (inputs that get a model past its safety training), prompt injection (instructions hidden in data the model reads) and edge cases.[^hendrycks]
- **Misuse and security:** a capable system aimed at harm by a person who wants that harm, or a system whose weights (its learned parameters) and capabilities get stolen and abused (bio, cyber, disinformation).[^zwetsloot]
- **Governance:** the incentives, institutions and race dynamics around the technology, separate from how any single model behaves.[^zwetsloot]

## Sorting by how harm arises gives three kinds of risk

A cleaner way to sort the same territory is the accident / misuse / structural taxonomy. It maps the four problems onto how the harm arises:

- **Accident risk:** the system does something harmful that nobody wanted (alignment and robustness failures).[^concrete]
- **Misuse risk:** a person deliberately points a working system at something harmful.[^zwetsloot]
- **Structural risk:** there is no single bad actor and no bug. Harm emerges from competition, deployment pressure, and how the technology reshapes power and incentives.[^zwetsloot]

My take: this taxonomy is worth keeping, because most arguments you overhear in AI safety are really disagreements about which of these three boxes dominates. [[AI Safety - Risk by Capability Level|Step 3]] comes back to it when sorting real failures by capability level.

```mermaid
flowchart TD
    S["AI safety (umbrella)"]
    S --> A["Alignment<br/>pursues intended goal,<br/>not a proxy"]
    S --> R["Robustness<br/>holds up under shift,<br/>adversaries, edge cases"]
    S --> M["Misuse & security<br/>capable system aimed<br/>at harm, or stolen"]
    S --> G["Governance<br/>incentives, institutions,<br/>race dynamics"]

    A --> ACC["Accident risk<br/>(nobody wanted it)"]
    R --> ACC
    M --> MIS["Misuse risk<br/>(someone did)"]
    G --> STR["Structural risk<br/>(emergent, no bad actor)"]
```

## Three premises make the case, with no science fiction needed

The field exists because we can build systems more capable than we can reliably specify, verify or control. Three premises carry that argument:

- **P1. Objectives are hard to specify.** We train systems on proxies: a reward signal, human approval, next-token likelihood (how well the model predicts the next word of its training text). None of those is the thing we actually want, and proxy and goal come apart under optimization. This is Goodhart's law: "when a measure becomes a target, it ceases to be a good measure."[^strathern]
- **P2. Capability is outpacing specification and verification.** Systems keep getting more general, and they get deployed into open-ended, high-stakes settings faster than we can audit them.[^hendrycks]
- **P3. Some failures do not stay contained or give a second chance.** A capable system optimizing a subtly wrong objective, at scale, can cause harm that is hard to catch early and hard to reverse late.[^ngo]

P1 to P3 already bite today. Reward hacking, specification gaming (a system scoring well on its measure without doing what was meant) and jailbreaks are P1 and P2 showing up in current models, not hypotheticals.[^concrete] [[AI Safety - Problem Framings|Step 2]] works through real cases. The long-term worry is what happens to P3 as capability climbs.[^bostrom]

```mermaid
flowchart LR
    P1["P1 trained on proxies,<br/>not the goal (Goodhart)"] --> C
    P2["P2 capability outpaces<br/>specify + verify"] --> C
    P3["P3 failures don't stay<br/>contained or reversible"] --> C
    C["The field exists because we can build<br/>systems more capable than we can<br/>reliably specify, verify, or control"]
```

## The camps are different bets, not enemies

The camps I'll keep meeting differ mainly in which risk they think is most neglected and most tractable.

| Camp | Core worry | Emphasis |
| --- | --- | --- |
| Existential / x-risk | Advanced misaligned AI as a catastrophic, maybe unrecoverable threat | Alignment theory, "get it right the first time"[^bostrom] |
| Prosaic alignment | Same long-term worry, but tractable through empirical work on today's models | RLHF (reinforcement learning from human feedback), interpretability, scalable oversight, evals[^ngo] |
| Ethics / present harms | Real harms now: bias, surveillance, labor, concentration of power | Accountability, auditing, deployment norms |
| Governance / policy | Race dynamics and misuse; coordination failure | Regulation, compute governance, standards, evals-as-policy[^zwetsloot] |

The tension that runs across all of them is present harms versus speculative catastrophe, and whether attention paid to one starves the other.

## I sit in the existential and prosaic camps

My two bets are the top two rows. The existential case is why I think the problem is worth a career. Prosaic alignment is where that conviction turns into work I can do this year on real models, which is also where the jobs are.

Russell's framing is a useful bridge between the two: build systems that are uncertain about the objective and defer to humans, rather than systems that optimize a fixed goal we had to guess at.[^russell] Steps 2 to 4 are where I'll test whether that framing holds up.

## Step 2 names the core problems in detail

[[AI Safety - Problem Framings|Step 2]] covers the core problem framings: specification gaming and reward hacking with real examples, instrumental convergence, and the alignment-vs-capability distinction that the whole field turns on.

## Sources

[^concrete]: Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Mane, D. (2016). *Concrete Problems in AI Safety*. arXiv:1606.06565. https://arxiv.org/abs/1606.06565
[^zwetsloot]: Zwetsloot, R., & Dafoe, A. (2019). *Thinking About Risks From AI: Accidents, Misuse and Structure*. Lawfare, Feb 11 2019. https://www.lawfaremedia.org/article/thinking-about-risks-ai-accidents-misuse-and-structure (GovAI mirror: https://www.governance.ai/research-paper/thinking-about-risks-from-ai-accidents-misuse-and-structure)
[^strathern]: Strathern, M. (1997). 'Improving ratings': audit in the British University system. *European Review*, 5(3), 305-321. Source of the popular phrasing of Goodhart's law.
[^hendrycks]: Hendrycks, D., Carlini, N., Schulman, J., & Steinhardt, J. (2021). *Unsolved Problems in ML Safety*. arXiv:2109.13916. https://arxiv.org/abs/2109.13916
[^ngo]: Ngo, R., Chan, L., & Mindermann, S. (2022). *The Alignment Problem from a Deep Learning Perspective*. arXiv:2209.00626 (ICLR 2024). https://arxiv.org/abs/2209.00626
[^bostrom]: Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press.
[^russell]: Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking.
