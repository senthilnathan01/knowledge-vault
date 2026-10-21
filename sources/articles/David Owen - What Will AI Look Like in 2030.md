---
type: source
source_type: article
status: synthesized
visibility: private
title: "What will AI look like in 2030?"
authors: ["David Owen"]
author_role: "Senior researcher, Epoch AI"
published: "2025-09-16"
publisher: "Epoch AI"
url: https://epoch.ai/publications/what-will-ai-look-like-in-2030
accessed: "2026-10-21"
topics: [ai-progress, scaling, forecasting, compute, science]
concepts: ["Drivers of AI Progress", "AI Timelines"]
course: "BlueDot AGI Strategy, lesson 2.1 (core reading)"
published_in: []
created: "2026-10-21"
---

# What will AI look like in 2030?

Epoch AI argues that AI scaling will probably continue to 2030 despite needing hundreds of billions of dollars and gigawatts of power, and that extrapolated benchmarks point to AI becoming a strong research assistant in several sciences, while real-world impact lags behind.[^owen-2030] It matters because it checks each common argument for a slowdown against data, and finds most of them weak.

This note covers Epoch's public summary page. The full report it summarizes was not read.

## The author forecasts AI from data, in work paid for by a lab

David Owen is a senior researcher at Epoch AI, a research group that tracks trends in AI compute, data and capabilities. Before Epoch he built AI models for surgical video in an industrial lab ("About the authors").[^owen-2030]

The report was commissioned by Google DeepMind. Epoch states that the views are the authors' own and not necessarily Google DeepMind's (header note).[^owen-2030]

The page is bylined to Owen but written as Epoch's "we", so this note says "Epoch".

## The argument: scaling continues to 2030, and science gets AI assistants

Each step reports what the page says, in its order. Section names are the page's.

### 1. If today's trends continue, the numbers get extreme

*Section: "Scaling is likely to continue to 2030"*

- On current trends, the computer clusters used to train frontier AI would cost over $100 billion by 2030.
- They could support training runs of about 10^29 FLOP (floating-point operations, the basic unit of computing work). That is as much computing as running the largest AI cluster of 2020 nonstop for over 3,000 years, and thousands of times the compute used for GPT-4.
- Such runs would need gigawatts of electricity. A gigawatt is roughly the output of one large power plant.
- Epoch's general pattern: "if today's trends continue, they will lead to extreme outcomes". Over the past decade extrapolation has been a strong baseline, and arguments for a coming slowdown "are often not compelling".

### 2. Each argument for a slowdown is answered

*Same section*

| Argument for a slowdown | Epoch's answer |
| --- | --- |
| Scaling could "hit a wall": bigger models stop improving | Recent models improved a lot on benchmarks and revenue. Possible, but no obvious evidence yet |
| Training data runs out | Enough public human-written text to scale to at least 2027, and synthetic data is now more clearly useful since reasoning models. A data bottleneck is hard to rule out fully, but "seems surmountable" |
| Electrical power runs short | Gigawatts are hard but can be supplied quickly (solar and batteries, off-grid gas), and training is starting to spread across several data centers. Unlikely to bind before 2028, "solvable even after that" |
| It gets too expensive and investment stops | Possible, but little sign of it. If lab revenues keep growing on trend, they would match the $100 billion+ investments by 2030 |
| Labs switch to more efficient algorithms instead | Algorithmic efficiency already improves alongside compute growth. There is "no particular reason" to expect it to speed up, and if it did, that "seems likely" to encourage using more compute, not less |
| Labs shift compute from training to running models (inference) | Training and inference currently get comparable compute, and better-trained models make inference more valuable, so they should grow together |

Epoch's conclusion: extrapolating current trends to 2030 is "a strong baseline prediction".

### 3. Science will get AI assistants like today's coding assistants

*Section: "AI will accelerate scientific R&D across several domains"*

- Epoch focuses on scientific research because several leading AI developers say it is a priority.
- By 2030, extrapolated benchmarks suggest AI will be able to implement complex scientific software from a plain-language description, help mathematicians formalize proof sketches, and answer complex questions about biology lab protocols.
- Many sciences will have AI assistants comparable to coding assistants for software engineers today. Based on software engineering, Epoch predicts this would eventually bring a 10 to 20% productivity improvement within tasks.
- Where that figure comes from (Notes, 2): a review of seven studies of AI in software engineering. Six found speed-ups or output gains of 20 to 70%. One found a 20% slowdown, and Epoch says that study "has a claim to the most thorough methodology". Epoch takes 20% as the starting point for current tools and says the prediction "comes with significant uncertainty".
- Epoch still expects AI capabilities to be "transformative across several scientific fields", though full deployment "may take longer than 2030" (Introduction and this section).
- Progress is fastest where realistic tasks can be trained on entirely in a computer, such as software and mathematics.

### 4. Four fields show where it is heading

*Same section*

- **Software engineering:** by 2030 on current trends, AI will autonomously fix issues, implement features and solve difficult but well-defined scientific programming problems. Benchmarks: SWE-bench Verified (real GitHub issues) and RE-Bench (research engineering tasks that take humans about eight hours).
- **Mathematics:** AI may soon work as a research assistant, filling out proof sketches. Notable mathematicians disagree a lot about how relevant current benchmarks are and how soon AI will produce results on its own.
- **Molecular biology:** benchmarks for how proteins bind small molecules (PoseBusters) are on track to be solved within a few years. Predicting arbitrary protein-protein interactions will take longer and is uncertain. Biology protocol question benchmarks should be solved by 2030.
- **Weather prediction:** AI already beats traditional methods for forecasts from hours to weeks ahead and is cheap to run. The next challenges are rare events and turning better forecasts into real benefits.

### 5. Impact will lag capability, especially where the real world is slow

*Same section*

- A recurring theme: deployment and impact on society may lag capabilities a lot.
- Software is fast to change: short iteration cycles, no wet labs or clinical trials, rarely safety-critical, easy to check roughly, and lots of training data. Drug development is the opposite.
- So Epoch expects "few if any" drugs approved by 2030 to have benefited from today's AI tools, though early-stage drug development will be seeing real effects. Software engineering, by contrast, will have changed dramatically.

### 6. AI will be everywhere by 2030

*Section: "Conclusion"*

By 2030, AI is likely to be a key technology across the economy, present in every interaction people have with computers and phones. If so, it is "vitally important" that key decision-makers prioritize AI issues over the next five years.

## The evidence is extrapolated trends and benchmark fits

| Claim | What the report offers as evidence | Where | How sure |
| --- | --- | --- | --- |
| Frontier training clusters will cost over $100 billion by 2030 | Extrapolation of current spending trends | "Scaling is likely to continue to 2030" | Conditional projection ("on current trends") |
| No slowdown argument is clearly decisive | A point-by-point check of six arguments | Same section | Authors' judgment, with the data it cites |
| Specific science benchmarks will be solved by 2030 | Fits to top scores on public leaderboards and model cards | "AI will accelerate scientific R&D" | Extrapolation; the report says benchmarks don't capture each field's full challenges |
| 10 to 20% productivity gain within scientific tasks | Analogy with software engineering, based on seven studies with mixed results | Same section and Notes, 2 | Authors' estimate; they flag significant uncertainty |
| Few drugs approved by 2030 will have benefited from today's AI | Reasoning about drug development timelines | Same section | Authors' judgment |

## Claude's reading: the inputs side agrees with Todd, the impact side is more modest

*Claude's reading, written during the ingest and not yet discussed. It is interpretation, not what the report says. Questions from it are in [[Open Questions]].*

- **On inputs, Epoch and Todd largely agree.** Both expect compute scaling to continue to about 2030. Both treat money, power and data as the main limits; Todd adds chips and the research workforce. Epoch is more confident the limits are surmountable through 2030. Todd puts more weight on them biting soon after.
- **On impact measured by 2030, Epoch is more modest.** A 10 to 20% productivity gain within scientific tasks, and few drugs helped by 2030, is a long way from the "100 years of scientific progress in 10" that Todd raises as a possibility (Todd, Introduction; [[Benjamin Todd - Will We Have AGI by 2030]]). Epoch does call the capabilities transformative over a longer period. The difference is mostly about what each is measuring: Epoch extrapolates benchmarks and deployment speed, while Todd's explosive case depends on AI automating AI research first. They can both be right if capabilities race ahead while deployment trails.
- **"Capability arrives before impact" matters for safety.** If impact lags, then economic numbers are a late warning sign, and capability measures are the early one. That is the same point Todd makes about AI research automating before most jobs.
- **The funding is relevant context.** Google DeepMind, which commissioned the report, is a frontier developer. The method (public trend data) is checkable either way.

## It feeds the drivers and timelines notes

- Builds on [[AI Safety - Risk by Capability Level]], where danger changes as capability rises; this report is about how fast capability rises.
- Feeds [[Drivers of AI Progress]] (the inputs to scaling and their limits) and [[AI Timelines]] (extrapolation as a baseline, and impact lagging capability).
- Pairs with [[Benjamin Todd - Will We Have AGI by 2030]], the other lesson 2.1 reading.
- Course context: core reading for lesson 2.1 in [[BlueDot AGI Strategy Course]].

## It leaves open how large the gap between capability and impact will be

- If science gets assistants by 2030 but impact lags years behind, when would the effects become visible, and in which fields first?
- The full report, not read here, may say more about how the four science domains were chosen and how the benchmark fits were done.

## Sources

[^owen-2030]: Owen, D. (2025, September 16). *What will AI look like in 2030?* Epoch AI (report commissioned by Google DeepMind). https://epoch.ai/publications/what-will-ai-look-like-in-2030 (the course links it at https://epoch.ai/blog/what-will-ai-look-like-in-2030)
