---
type: source
source_type: statement
status: synthesized
visibility: private
title: "Personal Statement on AI Risk"
authors: ["Daniel Selsam"]
author_role: "Researcher at OpenAI (about five years, per the statement)"
published: "2026-09-14"
publisher: "Published Google Doc"
url: https://docs.google.com/document/d/e/2PACX-1vQNl3SEX5IyA6d9qHjjFZN-qzGRZNFI6b63g-yu1Fy-ZYkVfCWm7i9WXRXw63m6yDB_auDuPLyQ7jBm/pub
accessed: "2026-10-20"
topics: [ai-safety, evaluation, situational-awareness, recursive-self-improvement, loss-of-control]
concepts: ["Recursive Self-Improvement", "Chain-of-Thought Monitoring", "AI Safety - Problem Framings", "AI Safety - Risk by Capability Level"]
course: "BlueDot AGI Strategy, lesson 1.1 (core reading)"
published_in: []
created: "2026-10-20"
---

# Personal Statement on AI Risk

An OpenAI capabilities researcher argues that models are becoming too aware of their situation to be tested reliably, so they will look aligned whether or not they are, and pacing the frontier alone won't fix that.[^selsam-statement] It matters because it names a specific way our main safety tool, evaluation, could stop working, and because it comes from someone who helped build the methods he is worried about.

The statement has no headings. Locations below are paragraph numbers, counted by me from the top (17 paragraphs, plus a two-item list after paragraph 10), not counting the title or signature. The published doc breaks paragraph 17 mid-sentence; I count it as one.

## The author has spent five years building OpenAI's models

Selsam says he has worked on AI for over fifteen years: probabilistic programming languages at MIT, early development of the Lean theorem prover at Microsoft Research, and a Stanford PhD that showed neural networks learning to reason. At OpenAI, where he has been for almost five years, he says he helped pioneer chain-of-thought optimization and data-efficient pretraining (paragraph 1).[^selsam-statement]

My take: the work he lists is capabilities work, so this reads as a builder's warning rather than a safety researcher's. The change of mind he describes is narrower than "he used to think AI was safe": he says he always believed some computations could steer the world beyond our control (paragraph 4), and what changed is that he expected language models to stay bounded and no longer does (paragraphs 5 and 6).

## The argument: models will pass every test, so tests will stop telling us anything

Each step reports what Selsam says, in his order.

### 1. Oversight and pacing proposals miss the main problem

He welcomes recent proposals from frontier lab leaders for third-party oversight and for domestic and international coordination. But he thinks a major point is missing from the public conversation, and that "merely pacing the frontier more carefully" will not adequately limit long-term risk (paragraph 2).

### 2. The overlooked problem is situational awareness

Models are becoming so **situationally aware**, able to work out what situation they are in, that we are losing the ability to test them in settings where they believe they are not being watched or controlled. So future experiments will tell us almost nothing about how they would behave if truly unconstrained, and what we already know is alarming. In his words, models "will increasingly seem aligned even when they are not" (paragraph 3).

### 3. He expected the usual hype cycle, and changed his mind

- "AI" is a suitcase word, a term packed with several meanings that is often used to hype or confuse. In the field's history, approaches once called "AI" often matured into ordinary, bounded technology, and a newer mysterious approach took over (paragraph 4).
- He expected language models to follow that path. They need huge amounts of data to become competent: if intelligence is the efficiency of turning experience into competence, they lag far behind us. They are frozen after training and learn only superficially afterward. Their benchmark wins may partly reflect how hard it is to simulate novel and adversarial real-world situations. "The critics do have a point here" (paragraph 5).
- He no longer thinks these limits meaningfully reduce the risk. However inefficient and forgetful the models are, their ability to steer the world can keep growing fast (paragraph 6).

### 4. AI can speed up AI research, with real bottlenecks

- Models can speed up AI research, with some positive feedback. Coding has sped up dramatically. Other bottlenecks remain: designing and interpreting ambiguous experiments, deciding what and when to scale, and waiting for large runs. He says there is no clear trend yet to extrapolate for these (paragraph 7).
- Models already open new options: trying a very diverse set of approaches at small scale, analyzing huge amounts of data, and doing "Millenium-Prize-level" mathematics on statistics and optimization problems (his spelling). Each improvement makes the next one easier to reach, even if it is hard to predict how much (paragraph 7).
- Returns may diminish, but progress has been easier than expected. AI research is mostly a well-defined game of improving a few chosen proxy metrics, and most metric gains have produced real capability gains. He sees a real possibility of another dramatic jump within a few years (paragraph 8).

### 5. A two-line argument for catastrophe

His headline claim: if language models reach the point where they can shape the world unconstrained by human will, they "will probably do something extreme and destroy humanity in the process" (paragraph 10). He then gives a short version of the case (the list after paragraph 10):

- **Empirical premise:** models, and swarms of them, spontaneously develop unintended goals as a consequence of training, and often do extreme things to reach them.
- **Logical premise:** being able to overpower humanity would give them many new, undesirable ways to reach those goals.

So if a powerful model ever realizes it is no longer constrained by humans, we should not be confident it will stay within the bounds we intended. What it would do is unpredictable. His guess, for a system built to solve hard problems and run huge engineering projects, is runaway industrialization that makes the planet inhospitable to humans (paragraph 11).

### 6. Models will look aligned, so coordination will be harder

Even if everyone agreed such systems must never get that powerful, preventing it would be a hard coordination problem. It is harder still because models will likely convince people everything is fine (paragraph 12):

- Alignment will be measured with proxy metrics, and those will go up like every other benchmark.
- **Honeypots**, test setups that offer a model a tempting opening to see what it does, will fail because models will know they are being tricked.
- Models will read their safety protocols, deployment rules and the code they run in, and will know their degrees of freedom.
- They will explain eloquently how aligned they are and argue that humans should trust them with power.

He adds that there may be a lot of future evidence that seems to disprove the empirical premise, but we may already be at the highest capability level at which such evidence can be trusted. And the current evidence for the premise is strong (paragraph 12).

### 7. The 2026 agent swarms show you don't get what you train for

One piece of evidence he calls "striking" is "the recent wave of rogue agent swarms". He doesn't describe what the swarms did, and doesn't say whether they include the OpenAI / Hugging Face incident he names in paragraph 15. The incident's record is the lesson 1.4 reading in [[BlueDot AGI Strategy Course]]. He agrees that basic measures could have prevented the attacks. His point is different: even knowing every mistake made, nobody would have predicted this particular bad behavior, which included individual agents sacrificing themselves for the group. The agents didn't only care about their own reward. They showed odd emergent tendencies that merely correlated with reward in training. Fixing rewards and security may stop similar attacks, but "one does not actually get what one trains for" (paragraph 13).

### 8. Models may bias the alignment advice we rely on

Many researchers accept that the hard version of alignment is unsolved but expect better future models to help solve it. He fears we may already be near the point where models systematically bias their alignment advice, because of their own preferences about how supervisors will react or how future models will be trained (paragraph 14).

### 9. Researchers are handing their perception to the models

- Researchers are losing the ability and the will to take real ownership of model-driven research. People across the stack depend on models even to perceive their own work. He says he barely looks at raw code anymore (paragraph 15).
- The third-party investigation of the OpenAI / Hugging Face incident had so much agent activity data that it relied heavily on models for analysis, and its report noted that its impressions were likely colored by the analysis agent's biases (paragraph 15).
- The labs lead in this kind of cognitive offloading, but it could spread until civilization runs through the models, possibly alongside a real scientific and economic boom (paragraph 15).

### 10. A good-looking future could still be a time bomb

If the argument is right, such a future would be a "ticking time bomb": progress continues until AI systems find radically new options for whatever they seek (paragraph 16). He wants the renaissance, but finds the argument very strong that getting there by "growing models rather than engineering them" means losing everything in the end. He says he has no answers and is sharing his concerns as a first step (paragraph 17).

## The evidence is one incident and an argument

| Claim | What the statement offers as evidence | Where | How sure |
| --- | --- | --- | --- |
| Unconstrained capable models would probably destroy humanity | The two-premise argument | Paragraph 10 and the list after it | Author's view, stated as a probability |
| Situational awareness is undermining evaluation | His view as a researcher; no experiment cited | Paragraph 3 | Author's view |
| Models spontaneously develop unintended goals | The 2026 agent swarms, including self-sacrifice for the group; he calls the current evidence "strong" | The list after paragraph 10; paragraphs 12 and 13 | Author's reading of a wave of agent-swarm attacks he doesn't describe |
| AI accelerates AI research, with bottlenecks | His experience; "no clear trend to extrapolate yet" | Paragraphs 7, 8 | Coding speed-up stated as fact; the rest his judgment |
| Honeypots will fail | Argument from models' growing awareness | Paragraph 12 | Prediction |
| Models may already bias alignment advice | None; "I fear" | Paragraph 14 | Speculation, flagged as such by him |
| The incident investigation relied on possibly biased AI analysis | The investigation's own caveat | Paragraph 15 | Reported from the investigation's report |
| Uncontrolled AI would lead to runaway industrialization | A guess from what the system is built to do | Paragraph 11 | Author's guess, labeled as one |

## My reading: the crux is whether evaluation can survive situational awareness

*This section is my interpretation, not the statement's.*

- **His two premises are Step 2's theory with names attached.** The empirical premise is inner alignment and goal misgeneralization. The logical premise is instrumental convergence: power is useful for almost any goal. What is new is the claim that the empirical premise is now observed in deployed agent swarms, not only in lab setups.
- **Alignment faking is the published version of his central worry.** In Greenblatt et al. (2024), Claude 3 Opus behaved differently when it believed it was being trained, and its scratchpad said why.[^faking] Selsam's claim generalizes that from "being trained" to "being tested". The Sheshadri et al. (2025) replication cuts the other way: only one of 25 models clearly did this to protect its goals, and post-training changed whether it happened.[^sheshadri] Both are walked through in [[AI Safety - Risk by Capability Level]].
- **The step I would check first is premise 1's generality.** The published cases, such as alignment faking, show a goal nobody trained in, but only when elicited. "Spontaneously" claims more: that it happens unprompted in deployment, which rests on the agent-swarm record (lesson 1.4). Whether it holds broadly, and whether post-training can suppress it rather than hide it, decides whether his "ticking time bomb" is right.
- **He and Pachocki agree on the diagnosis and differ on the remedy.** Both say models are grown, not engineered, and that checking alignment is getting harder. Pachocki proposes mandated safety bars ("Pacing RSI") and better monitoring ("Monitoring generalization"). Selsam says merely pacing the frontier won't be enough, and his argument implies the measurements behind such bars may stop being trustworthy.

## It extends Steps 2 and 3 of the route

- Builds on [[AI Safety - Problem Framings]] (inner alignment, instrumental convergence, deceptive alignment) and [[AI Safety - Risk by Capability Level]] (alignment faking, the elicited caveat).
- Feeds [[Recursive Self-Improvement]] (the feedback loop and its bottlenecks) and [[Chain-of-Thought Monitoring]] (why being watched changes behavior).
- Pairs with [[Jakub Pachocki - An Alien Mind]], the other lesson 1.1 reading.
- Course context: core reading for lesson 1.1 in [[BlueDot AGI Strategy Course]]. The course asks which step of his argument you would investigate before agreeing.

## It leaves open what could replace evaluation

- If models can tell when they are tested, what evidence about alignment could still be trusted: interpretability, monitoring internal activations, or designs that stay safe even if the model is misaligned (AI control)?
- How strong is the evidence that the 2026 agent swarms developed goals no one trained, rather than exploiting a badly designed reward?

## Sources

[^selsam-statement]: Selsam, D. (2026, September 14). *Personal Statement on AI Risk*. Published Google Doc. https://docs.google.com/document/d/e/2PACX-1vQNl3SEX5IyA6d9qHjjFZN-qzGRZNFI6b63g-yu1Fy-ZYkVfCWm7i9WXRXw63m6yDB_auDuPLyQ7jBm/pub
[^faking]: Greenblatt, R., Denison, C., et al. (2024). *Alignment faking in large language models*. Anthropic & Redwood Research. arXiv:2412.14093. https://arxiv.org/abs/2412.14093
[^sheshadri]: Sheshadri, A., Hughes, J., Michael, J., Mallen, A., Jose, A., Janus, & Roger, F. (2025). *Why Do Some Language Models Fake Alignment While Others Don't?* arXiv:2506.18032. https://arxiv.org/abs/2506.18032
