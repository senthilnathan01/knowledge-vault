---
type: thinking
status: active
visibility: private
created: 2026-10-20
---

# Open Questions

Questions I want to work out. Each entry says where it came from, why it matters, and the next step. Entries are grouped by theme; a new entry goes at the end of its theme. "Claude's first take" marks a suggestion I haven't discussed or adopted yet. How this list works: [[Thinking]].

## Evaluation and evidence

### Which step of Selsam's argument should I question before agreeing with it?

- Status: open
- From: BlueDot AGI Strategy lesson 1.1, which asks which line of thinking in [[Daniel Selsam - Personal Statement on AI Risk]] I would most want to investigate before deciding whether I agree.
- Why it matters: his conclusion (that growing models rather than engineering them ends in catastrophe) rests on two premises: (1) training gives models goals nobody intended, and (2) the power to overpower humans would give those goals dangerous new routes. These are the same ideas as inner alignment and instrumental convergence in [[AI Safety - Problem Framings]], so judging them tests my route notes too.
- Claude's first take: premise 1. Published cases such as alignment faking show behavior nobody trained in, but only when researchers set up the conditions. If "spontaneously develop unintended goals" means "unprompted, in real use", it rests on the 2026 agent swarms, whose record is not in the vault yet (lesson 1.4). A counterpoint worth discussing: Selsam may only mean "as a side effect of training rather than on purpose", and on that reading alignment faking already fits premise 1.
- Next step: discuss.

### If models can tell when they are being tested, what evidence about their alignment can still be trusted?

- Status: open
- From: Selsam's central claim, and the evaluation awareness section of [[AI Safety - Risk by Capability Level]]. **Evaluation awareness** means a model telling a test from real use, a form of situational awareness. That section cites Needham et al. (2025), who found models can often tell a test from real use, and Schoen et al. (2025), who found that awareness of being evaluated reduced covert misbehavior.
- Why it matters: almost every safety decision, from release decisions to mandated safety bars, rests on test results. If tests stop meaning much, something else has to carry that weight.
- Candidates so far: reading the model's reasoning ([[Chain-of-Thought Monitoring]]), looking inside the network (interpretability), and designing systems that stay safe even if the model is misaligned (AI control). None is settled.
- Next step: revisit at course lesson 4.2, "The technical challenge".

### What could a mandated safety bar measure that an evaluation-aware model can't game?

- Status: open
- From: Pachocki's proposal in [[Jakub Pachocki - An Alien Mind]] that safety commitments become mandated safety bars (a safety level a model must pass before it is scaled further or released), and the same question in [[Recursive Self-Improvement]].
- Why it matters: a safety bar is only as good as its measurement. If the model can recognize the measurement, the bar measures how well it behaves when watched.
- Next step: discuss with the question above.

### Did the 2026 agent swarms show goals nobody trained, or only flaws that better rewards and security would have stopped?

- Status: open
- From: [[Daniel Selsam - Personal Statement on AI Risk]] and the 2026 incidents section of [[AI Safety - Risk by Capability Level]]. Agent swarms here means groups of AI agents that carried out attacks in 2026; neither reading says what they did.
- Why it matters: the first answer would be evidence that goals form on their own in real use. The second would be reward hacking, a known problem but not a solved one. Selsam accepts the second and argues the first anyway (his paragraph 13), so the question is whether the record supports that extra step. It also decides how far the "every result is elicited" caveat (seen only when researchers set up the conditions) still holds.
- Next step: read the investigation of the OpenAI / Hugging Face incident (lesson 1.4 of [[BlueDot AGI Strategy Course]]), and check whether it is one of the swarms Selsam means. He doesn't say.

## Monitoring and pacing

### If chain-of-thought monitoring is getting less reliable, does Pachocki's own reasoning say labs should slow down now?

- Status: open
- From: [[Jakub Pachocki - An Alien Mind]] and [[Chain-of-Thought Monitoring]].
- Why it matters: it tests whether a lab leader's stated principles actually bind what the lab does.
- Claude's first take: his argument runs: scaling should be limited by confidence in safety, that confidence comes mainly from CoT monitoring, and CoT monitoring is getting less reliable. That points to slowing, and he already hopes voluntary slowdowns become common until shared safety bars exist. He also writes that no lab can keep scaling responsibly at maximum speed "for much longer". What he doesn't say is whether his own evaluations show it is time now, or what would trigger a slowdown.
- Next step: discuss.

### How could anyone outside a lab check what the lab reports?

- Status: open
- From: three notes that each hit this wall. Pachocki's evidence for recursive self-improvement and for weakening monitoring is unpublished ([[Jakub Pachocki - An Alien Mind]]). Whether anyone outside a lab can check that a chain of thought still shows the real reasoning is left open in [[Chain-of-Thought Monitoring]]. How fast AI research is being automated is visible mainly from inside ([[Recursive Self-Improvement]]).
- Why it matters: pacing, mandated safety bars and international agreements all depend on someone other than the lab being able to verify.
- Next step: watch for this in lesson 1.3 (coordination) and Unit 4.

### Which bottleneck in AI research gives way first: experiment design, interpreting results, scaling decisions, or compute?

- Status: open
- From: [[Recursive Self-Improvement]]. Pachocki expects the loop to continue. Selsam sees real bottlenecks with "no clear trend" yet, but still a real chance of a dramatic jump within a few years. Todd adds the inputs that limit the whole field around 2028 to 2032: money, power, chips and the human research workforce ([[Drivers of AI Progress]]).
- Why it matters: it sets how soon AI does most of the work of building the next AI.
- Next step: course lesson 2.3, "How could progress accelerate from here?"

## AI progress and timelines

### Where would I place today's models against Todd's end-of-2026 forecast?

- Status: open
- From: BlueDot AGI Strategy lesson 2.1, which asks where to place today's models in Todd's world from 2025 ([[Benjamin Todd - Will We Have AGI by 2030]]). His end-of-2026 forecast: expert-level knowledge in every field, better-than-human coding, general reasoning better than almost all humans, and many day-long computer tasks done alone.
- Why it matters: it tests whether trend extrapolation, the main forecasting method in [[AI Timelines]], is working, and so how much to trust its forecasts for 2028 to 2030.
- Claude's first take: on Todd's own September 2026 scorecard, today is ahead of his end-of-2026 forecast on tasks with checkable answers. METR's time horizon is 16 hours or more against his predicted 6, revenue growth is 6x a year against his 4x, and FrontierMath is saturated (the top of his range). What his picture doesn't settle is the messy, long, high-context work, and whether AI is doing a meaningful share of AI research yet.
- Next step: discuss at the Unit 2 live session (2026-10-21).

### Will time horizons keep growing on messy, real-world work, or only on tasks with checkable answers?

- Status: open
- From: [[Benjamin Todd - Will We Have AGI by 2030]], which calls this "perhaps the central question of AI forecasting right now", and [[AI Timelines]].
- Why it matters: the case against short timelines rests on AI staying poor at ill-defined, high-context work. If the time horizon trend holds there too, that case loses most of its force. If it only holds on well-defined software tasks, AI may stay a powerful tool rather than a replacement for researchers.
- Next step: lesson 2.2, "What can increasingly capable AI systems do?"

### Can Todd's fast scenario and Epoch's slower impact estimate both be right?

- Status: open
- From: [[Benjamin Todd - Will We Have AGI by 2030]] ("100 years of scientific progress in 10") and [[David Owen - What Will AI Look Like in 2030]] (a 10 to 20% productivity gain within scientific tasks, and few drugs helped by 2030).
- Why it matters (from Claude's reading of the Owen note, not yet discussed): it decides which signals to watch. If impact lags capability, economic numbers are a late warning and capability measures an early one.
- Claude's first take: they can both be right. Epoch extrapolates benchmarks and how fast fields adopt AI. Todd's fast scenario depends on AI research being automated first, which Epoch's summary doesn't model. The deciding variable is whether AI research is automated before the inputs to progress run out around 2030.
- Next step: lesson 2.3, "How could progress accelerate from here?"

## My own direction

### Should my first Step 4 topic be mechanistic interpretability, or AI control and evals?

- Status: open
- From: [[AI Safety]] hub and [[BlueDot AGI Strategy Course]].
- Why it matters: it decides what I study in depth first and what kind of work I aim for. Evaluation awareness argues for interpretability, because looking inside doesn't depend on how the model behaves under test. The 2026 incidents may argue for control: assume the model could be misaligned, and contain it.
- Next step: revisit at course lesson 4.2.

## Settled

None yet. When a question is answered, it moves here with a one-line answer and a link to the note that holds the reasoning.
