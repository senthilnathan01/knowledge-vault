---
type: concept
status: active
visibility: private
created: 2026-07-27
tags: [ai-safety, learning-route]
---

# AI Safety

This is the hub for a top-down study of AI safety. Each step gets its own note, linked below, and the [[VAULT_INDEX|Vault Index]] maps the rest of the vault.

## I care most about the existential case and prosaic alignment

I care about the existential case because it is why the problem matters, and about prosaic alignment because it is work I can do now and get hired for. The **existential case** is the worry that advanced misaligned AI could cause a catastrophe we can't recover from (a projection, not yet a measurement; see Step 3's Tier 3). **Prosaic alignment** is the empirical work on today's models.

The two meet in Step 3's Tier 2, where today's models show early, elicited forms of the failures the existential case worries about. For example, Claude 3 Opus complied with harmful requests more often when it believed it was being trained, to protect its values. I argue for this pair in [[AI Safety - Foundations|Step 1]] and turn it into priorities in [[AI Safety - Risk by Capability Level|Step 3]].

## Steps 1 to 3 are done, and Step 4 is next

1. [[AI Safety - Foundations|The map and the case]]: what "AI safety" means, the accident / misuse / structural taxonomy, the three-premise case (P1 to P3) for why it matters, and the major camps. Done.
2. [[AI Safety - Problem Framings|Core problem framings]]: capability vs. alignment, outer and inner alignment, reward hacking, mesa-optimization and deceptive alignment, goal misgeneralization, goal vs value alignment, orthogonality and instrumental convergence. Done.
3. [[AI Safety - Risk by Capability Level|Where risk enters, by capability level]]: present harms and misuse, early misalignment signals in frontier LLMs (including evaluation awareness and the 2026 agent incidents), and speculative advanced-AI risk. Done.
4. Technical alignment approaches, the responses to Step 3's failures: RLHF (reinforcement learning from human feedback), Constitutional AI (training against a written list of principles), scalable oversight (ways for people to supervise systems more capable than they are), interpretability (reading what a model computes inside), red-teaming (attacking a system on purpose to find its failures) and evals (tests that measure what a model can do). Next, and already seeded by [[Chain-of-Thought Monitoring]]. The likely first topic to study in depth is **mechanistic interpretability**, because Step 3's Sleeper Agents result showed that standard safety training may not remove a planted deception from a large model, and training on behavior cannot target what it cannot see.
5. Governance and the ecosystem: labs, policy, evals orgs and standards. Started early through the [[BlueDot AGI Strategy Course]]; [[Recursive Self-Improvement]] covers why the pace of AI research is itself a governance question.
6. Open problems and my own synthesis. Not started.

## The BlueDot course brings Step 5 forward, ahead of Step 4

Most of BlueDot's AGI Strategy course is Step 5 material (strategy and governance), so taking it from October 2026 means meeting Step 5 before Step 4. Progress is tracked in [[BlueDot AGI Strategy Course]]. My guess: Unit 1's Hugging Face incident (lesson 1.4) will update Step 3, and Unit 4.2 may change whether my first Step 4 topic is mechanistic interpretability or AI control and evals.

## Concept notes hold single ideas that the steps link to

Step notes are the study path. Ideas that stand on their own get their own concept note, which several steps and course lessons can link to:

- [[Recursive Self-Improvement]]: AI doing a growing share of the research that builds the next AI, and why that shrinks the time for safety checks.
- [[Chain-of-Thought Monitoring]]: reading a model's written reasoning to catch bad intent, why grading that reasoning teaches models to hide it, and why it is getting less reliable.
- [[Drivers of AI Progress]]: what makes AI better: compute and algorithms, turned into capability by four drivers (pretraining, reasoning training, longer thinking, agents), and the limits on each.
- [[AI Timelines]]: how to forecast when specific capabilities arrive, the time horizon trend, and Todd's argument that the probability is concentrated before about 2030.

## My questions live in Thinking

The questions these notes raise, and my answers as they form, are collected in [[Open Questions]]; ideas to act on are in [[Ideas]]. That is where I work out what I think, not just what sources say.

## Each step is discussed first, then written up

I discuss each step with Claude first, then write the note. Sources I hand over with "ingest" go through the ingest workflow: a source note per reading in `sources/`, with ideas pulled into concept notes. Each note starts conceptual and goes technical only on the parts I care about, and follows the [[templates/Note Style Guide|Note style guide]].
