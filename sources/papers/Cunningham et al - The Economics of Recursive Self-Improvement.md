---
type: paper
status: synthesized
visibility: private
title: "The Economics of Recursive Self-Improvement"
authors: ["Tom Cunningham", "Lukas Althoff", "Basil Halperin", "Brian Jabarian", "Andrew Koh", "Arjun Ramani", "Phil Trammell", "Parker Whitfill", "Cheryl Wu"]
year: 2026
venue: "Elasticity Institute (paper dated July 13, 2026)"
doi: ""
url: https://elasticity.institute/rsi-paper.pdf
arxiv_id: ""
pdf_path: ""
project: "BlueDot AGI Strategy Course"
topics: [recursive-self-improvement, intelligence-explosion, economics, feedback-loops, forecasting]
research_brief: ""
published_in: []
accessed: "2026-10-22"
pages_read: "1-3 (abstract, introduction, definitions), 29 (calibration result), 30-32 (sections 4.2 to 4.4, the assigned reading) of 36"
course: "BlueDot AGI Strategy, lesson 2.3 (assigned: pages 30 to 32, sections 4.2 to 4.4)"
created: "2026-10-22"
---

# The Economics of Recursive Self-Improvement

Nine researchers, mostly economists, model when AI improving AI could turn into a **self-sustaining acceleration**: progress that keeps speeding up even with no more human researchers or compute added. Their rough calibration says the feedback loop is not yet strong enough for that, but is getting stronger.[^cunningham-rsi] It matters because it turns "will there be an intelligence explosion?" into a question about measurable quantities, and says which ones labs should publish.

Only pages 1 to 3, 29 and 30 to 32 of the 36-page paper were read. The models in sections 2 and 3, and most of the calibration, were not.

## Citation

Cunningham, T., Althoff, L., Halperin, B., Jabarian, B., Koh, A., Ramani, A., Trammell, P., Whitfill, P., & Wu, C. (2026, July 13). *The Economics of Recursive Self-Improvement*. Elasticity Institute. https://elasticity.institute/rsi-paper.pdf

Tom Cunningham (METR) is the lead author; the others are listed alphabetically, from Stanford, the University of Virginia, Carnegie Mellon and Google AI, Columbia, MIT, Epoch AI, METR and Yale. All are affiliated with the Elasticity Institute. METR gave administrative and financial support (page 1).

## Relevance

Lesson 2.3 asks how much better AI systems can speed up the development of their successors, and whether that becomes an intelligence explosion. This paper gives the economist's version of the question: a precise condition, rough numbers, and a list of what to measure.

## Research question

Under what conditions does AI's contribution to AI research produce accelerating progress, and do those conditions hold now (pages 1 to 3)?

## Method

- Design: a sequence of increasingly detailed economic models of AI progress, drawn as diagrams of feedback loops, then calibrated with published estimates (abstract, page 3).
- Core idea: the **core feedback loop** asks, "for a one-unit increase in model capabilities, how much do the capabilities of the next generation of models increase?" (page 2). Acceleration depends on "the product of elasticities across each feedback loop" (abstract). An **elasticity** is how strongly one quantity responds to another, in percentage terms.
- Basic model: AI capabilities and human labor produce better algorithms; better algorithms and training compute produce more capable AI. Extensions add bottlenecks (humans, compute or data that the loop can't do without) and economic feedback (higher economic output pays for more compute and data collection) (page 3).
- Not read: the model details in sections 2 and 3.

## The paper separates four ideas that often get blurred

*Table 1, pages 2 and 3*

| Term | The paper's definition, paraphrased |
| --- | --- |
| Feedback loop | Outputs of a system today become its inputs tomorrow. Arguably most technologies have these, and AI has for a long time |
| R&D automatability | AI can make technical improvements at least as good as human researchers', at equal cost. Being automatable doesn't mean it is automated |
| Self-sustaining acceleration | AI is enough to keep progress speeding up without growth in outside inputs such as human labor or training compute |
| Intelligence explosion | AI capabilities go to infinity in finite time |

The authors note that some treat full automation of AI research as enough for self-sustaining acceleration, quoting I. J. Good's 1965 claim. Their models show it "may not follow" if there are diminishing returns ("ideas become harder to find") or bottlenecks (page 3). They also note "recursive self-improvement" is used inconsistently, and attribute its popularization to Eliezer Yudkowsky, extending Good's argument (page 2, footnote 2).

## The calibration says the loop is below the threshold for now

*Page 29*

- Under their model, self-sustaining acceleration happens if research effort rises by more than 0.15 (15%) for each extra point on the Epoch Capabilities Index (ECI), a combined capability scale. Their example: Anthropic would meet the condition if switching from Claude Opus 4.7 to Opus 4.8, one ECI point better, raised research productivity by 15%.
- Their check uses **uplift**, how many times faster AI makes engineers ([[Measuring AI Capability]]). Opus 4.8 scores 16 ECI points above Claude 3.7 Sonnet (February 2025), when estimates of AI's effect on engineering productivity were "not conclusively larger than 0". Even taking Anthropic engineers' self-reported 4x uplift at face value, which they call "very likely to be an overestimate", that works out to about 9% more productivity per ECI point, below the 15% threshold.
- They expect these elasticities are rising: going from GPT-4 to GPT-5 raised research productivity much more than going from GPT-1 to GPT-2. So they call understanding how and why the key elasticity changes over time "an important research priority".
- They have "almost no evidence" for the key elasticity of research effort to capabilities, because uplift studies don't report results in that form.

## Main claims and evidence (sections 4.2 to 4.4, the assigned reading)

### 4.2 AI already speeds up AI research, but compute, returns and data may cap it

*Pages 30 and 31*

Best evidence in favor, per the authors:

- AI is "meaningfully contributing to AI progress". The Claude Mythos Preview system card reported a self-assessed productivity uplift of roughly 4x among Anthropic researchers ("likely overstated"), and a 40-hour time horizon at which Mythos Preview beat human researchers. In April 2026, Mythos Preview beat human researchers at AI research decisions 64% of the time, up from 50% for Claude models released in 2025 (Favaro and Clark, 2026). OpenAI reported in July 2026 that internal coding inference's share of research compute grew 100-fold in six months.
- Forecasters give it real weight. In August 2025, superforecasters gave an 8% chance and experts a 20% chance (medians) that the growth rate of effective compute would triple by 2029. In May 2026, Jack Clark gave a 60% chance that by the end of 2028 there will be "an AI system powerful enough that it could autonomously build its own successor".

Best evidence against:

- Compute bottlenecks could bind: better algorithms may need more training compute, more AI researchers may need more experimental compute, and the economy may not grow fast enough to fund more investment ("run out of GDP").
- Autonomous improvement of algorithms may hit diminishing returns quickly, which the authors say is "widely observed informally".
- Capabilities may depend on data: one cited view is that "most algorithmic progress is data progress". Better filtering of pretraining data may be a one-time boost, while post-training data and reinforcement learning environments might be automated.

Two further considerations:

- **Narrow before broad.** AI research agents might get good at concrete, benchmark-measured algorithmic gains while staying weak at breakthroughs that let models learn efficiently, or at "amorphous" skills like "vision" or "taste". Spillovers are possible: a narrow system optimizing benchmarks might stumble on something general, such as algorithms that keep learning during deployment.
- **Political and social barriers.** At least 20 US data center projects were cancelled in early 2026 after local pushback, and $85 billion of projects in three years (citing The Economist). Recent US policy reactions to Mythos also suggest more weight on such barriers.

### 4.3 Speed is the danger: less time for institutions and safeguards

*Pages 31 and 32*

A self-sustaining acceleration differs from ordinary progress in speed: it "could compress generations of progress into short periods of time". The authors list five effects:

- Transition costs plausibly rise with speed, as some economists argue happened with the "China Shock" to manufacturing jobs.
- Institutional inertia: regulators, democratic processes, law and infrastructure might lag, and elites might use a temporary spike in power to capture institutions.
- Uneven progress: acceleration is more likely first in tasks "easy to verify in closed loops", such as software, games and math, so there could be breakthroughs in math and chemistry alongside slow progress in messier fields.
- Power imbalances: small gaps in skill between labs or countries could become large gaps in power.
- Greater misalignment risk: sudden jumps in capability leave "less time for technical and social safeguards".

### 4.4 The authors want lab surveys and experiments to pin down the parameters

*Page 32*

They list ten directions, including measuring the return to research, modeling "research taste and vision in AI R&D", treating the decision to automate as something labs choose, surveys and experiments inside frontier labs to estimate the key parameters, and better incentives for prediction markets on AI progress.

## Limitations

- The authors call their calibration a "back-of-the-envelope calculation" (abstract) and say they have almost no evidence for the key elasticity (page 29).
- Self-reported uplift, the main input, is "very likely" an overestimate (page 29).
- Not read here: the models' assumptions in sections 2 and 3, which the conclusions depend on.

## Short quotations

> "for a one-unit increase in model capabilities, how much do the capabilities of the next generation of models increase?"

Location: page 2, "Core argument"

## Claude's reading: the loop's strength is a number labs could measure

*Claude's reading, written during the ingest and not yet discussed. It is interpretation, not what the paper says. Questions from it are in [[Open Questions]].*

- **It makes the vague question precise.** "Will AI improving AI run away?" becomes "does each step of capability raise research productivity by more than about 15%?" That is checkable, at least in principle, which is why the authors ask labs to publish the inputs. By Claude's arithmetic, a 4x gain over 16 points is ln 4 / 16, about 0.087 per point, which is the paper's 9%.
- **The "narrow before broad" point and METR's findings fit.** METR found agents strong where progress is cheap to check and weak on judgment ([[METR - Frontier Risk Report February to March 2026]]). If the loop speeds up only the checkable part of research, the paper suggests it is plausible to get fast benchmark gains with slower real-world change, which is also the capability-before-impact pattern in [[AI Timelines]].
- **The threshold is about the loop, not about danger.** The paper's own impacts section says even a fast but not infinite acceleration would leave less time for safeguards. So "below the threshold" is not "safe".

## Connections

- Concepts: [[Intelligence Explosion]], [[Recursive Self-Improvement]], [[Measuring AI Capability]] (the ECI), [[Drivers of AI Progress]].
- Related readings: [[Kokotajlo et al - AI 2027]] and [[Lifland, Kokotajlo and Halstead - Q2.5 2026 Timelines Update]], the other lesson 2.3 readings; [[Favaro and Wright - Measurements for Understanding the Pace of AI Development]], whose measurements are the kind the paper asks for.
- Course: [[BlueDot AGI Strategy Course]], lesson 2.3.

## Follow-ups

- Read sections 2 and 3 to see which model assumptions drive the 0.15 threshold.
- Favaro and Clark (2026), which the paper cites for the 64% research-decision result and a narrow definition of RSI, is not in the vault; its full reference (in the paper's bibliography) wasn't read.

## Sources

[^cunningham-rsi]: Cunningham, T., et al. (2026, July 13). *The Economics of Recursive Self-Improvement*. Elasticity Institute. https://elasticity.institute/rsi-paper.pdf Pages read: 1 to 3, 29, 30 to 32.
