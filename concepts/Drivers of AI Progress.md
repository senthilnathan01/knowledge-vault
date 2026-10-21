---
type: concept
status: active
visibility: private
created: 2026-10-21
tags: [ai-progress, scaling, compute, capabilities]
sources: ["Benjamin Todd - Will We Have AGI by 2030", "David Owen - What Will AI Look Like in 2030"]
---

# Drivers of AI Progress

AI gets better mainly because more computing power and better algorithms are fed into a few specific methods: scaling pretraining, reinforcement learning for reasoning, test-time compute, and agent scaffolding. Knowing the drivers matters because each one has its own limits, and those limits set how long fast progress can last.

This note explains what makes AI better, the engine behind the rising capability in [[AI Safety - Risk by Capability Level]]. How fast that goes is in [[AI Timelines]]. It draws on the two lesson 2.1 readings in [[BlueDot AGI Strategy Course]]: Benjamin Todd (80,000 Hours) and David Owen (Epoch AI).

## Two inputs, compute and algorithms, multiply into effective compute

At the broadest level, progress has two inputs (established, widely used framing):[^todd-agi2030]

- **Compute:** the computing power used to train and run models. Training compute for leading models has grown more than 4x per year, far faster than the best chips themselves improve (about 35% per year). Todd says the growth was driven by spending more money and using more efficient chips.
- **Algorithms:** better methods that get more out of the same compute. The compute needed to reach a given performance has fallen about tenfold every two years, roughly 3x per year.

The two multiply. Four times the compute, with each unit going three times further, gives about 12x more **effective compute** each year (Todd's figures, from Epoch AI data).[^todd-agi2030] Todd puts the total from GPT-2 (2019) to GPT-4 (2023) at about 300,000x more effective compute. That jump took AI from a model that could "just about stay on topic for a couple of paragraphs" to one that beat most high schoolers at college entrance exams.[^todd-agi2030] One caution: 12x a year for four years gives about 20,000x, not 300,000x. The article gives both figures without reconciling them, so treat the total as Todd's estimate, not a product of the yearly rate.

An everyday analogy is a factory that both buys more machines each year and makes each machine faster: output grows by the product of the two. The analogy breaks down in one place. A factory's output is a count of goods, while "capability" isn't one number: a model can get much better at math while staying weak at something else.

## Four methods turn compute into capability

Todd breaks recent progress into four drivers.[^todd-agi2030] Each works differently and has different limits.

| Driver | What it is | Example of what it bought | What limits it |
| --- | --- | --- | --- |
| Scaling pretraining | Training a model to predict missing text on huge amounts of data, with more compute each time | GPT-2 to GPT-4 | Money, power, chips and eventually training data |
| Reinforcement learning for reasoning | Rewarding the model's step-by-step reasoning when it reaches a correct, checkable answer | GPT-4 scored barely above chance on PhD-level science questions in 2023; o1 matched PhDs a year later | Works best where answers can be checked |
| Test-time compute | Letting the model think longer while it runs, instead of training it more | o1 kept getting more accurate on coding problems as it thought up to 100 times longer | Cost per answer |
| Agent scaffolding | Giving a reasoning model memory and tools so it can plan, act, check and repeat over many steps | On real one-hour software tasks, agents went from about 20% (GPT-4) to over 70% (o3, reportedly) | Reliability over many steps; the most uncertain driver |

### Pretraining follows scaling laws

A **scaling law** is the regular relationship between training compute and performance: historically, each 10x increase in compute brought a steady gain across many benchmarks (established).[^todd-agi2030] Todd notes these laws had been published by 2020, so to people following them GPT-4 "wasn't a surprise". Todd's point is that a lot of AI progress "is more like engineering" than breakthrough: do a lot more of the same and the models improve.

### Reinforcement learning needs answers that can be checked

The reasoning method shows the model a problem with a verifiable answer, has it write out a chain of reasoning, and reinforces the reasoning that reached the right answer.[^todd-agi2030] Because correct solutions can be verified automatically, models can generate their own training data: solve many problems, keep the correct solutions, train the next model on them. Todd calls this a flywheel.

The catch is **verifiability**: whether there is a quick, reliable way to check if an answer is right. Math, coding and science have it. Business strategy and writing mostly don't. Todd later counted identifying verifiability as "the key axis of progress" among the calls he was proud of (his 2026 follow-up, quoted by the course).[^bluedot-2-1] Claude's take (not yet discussed): so where AI gets good first is fairly predictable: wherever answers can be checked.

### Reliability compounds over many steps

Agents fail when any step fails. Todd's arithmetic: a 20-step task at 90% reliability per step succeeds only about 10% of the time. At 99% per step it succeeds about 80% of the time.[^todd-agi2030] So a modest-looking gain in per-step reliability can turn an agent from useless to useful almost overnight, which is why agent progress can feel sudden.

## Todd's 2026 review: shifting compute to reinforcement learning slowed pretraining

Todd's own 2026 assessment of his forecasts says he "underweighted how compute shifting into RL would slow the pretraining trend".[^bluedot-2-1] Claude's take (not yet discussed): the drivers draw on one budget of compute, so extrapolating each one separately can mislead. The full scorecard is in [[AI Timelines]].

## Money, power, chips, data and researchers set the limits

The drivers need their inputs to keep growing, and each input has a ceiling. Both readings cover money, power and data, and differ on when they bind; only Todd covers chips and researchers:

| Input | Epoch AI (Owen, 2025)[^owen-2030] | Todd (2025)[^todd-agi2030] |
| --- | --- | --- |
| Money | Frontier training clusters over $100 billion by 2030 on current trends; matched by revenue if it keeps growing | Another 10x beyond a roughly $10 billion run needs hundreds of billions, comparable to the Apollo program |
| Power | Gigawatts by 2030 (a gigawatt is roughly one large power plant); hard but solvable, unlikely to bind before 2028 | AI chips could use 4%+ of US electricity by 2028; another 10x would be 40%+ |
| Chips | Not a main focus of the summary page | TSMC could comfortably make 5x more AI chips; 50x would be a huge challenge |
| Data | Enough public text to at least 2027; synthetic data helps | Enough for a GPT-6-scale run by 2028; reasoning models generate their own data |
| Researchers | Not discussed on the summary page | Steady algorithmic progress needs an exponentially growing workforce, which can't last |

How sure to be: both are projections. Epoch's view is that the limits are surmountable through 2030 (authors' judgment).[^owen-2030] Todd's view is that growth "most likely" slows around 2028 to 2032 unless AI itself starts substituting for researchers (author's view).[^todd-agi2030]

Claude's take (not yet discussed): the researcher input is the one that matters most for safety, because it is the one AI could replace. If AI can do AI research, the workforce limit disappears, and that is the loop in [[Recursive Self-Improvement]].

## Why it matters for safety: the drivers decide how much warning there is

Claude's take (not yet discussed):

- If the drivers keep working, capability keeps rising on a schedule people can roughly forecast. That gives some warning, and the evaluations in [[AI Safety - Risk by Capability Level]] can be planned against it.
- Verifiability shapes which dangerous capabilities arrive first. Cyber offense and coding have checkable answers, so they are likely early, which matches Pachocki's report of models becoming superhuman at breaking into computer systems ([[Jakub Pachocki - An Alien Mind]]).
- New drivers appear every one to two years, on Todd's count.[^todd-agi2030] Each new driver, like reasoning models in 2024, can produce a jump that earlier trend lines would miss.

## Sources

[^todd-agi2030]: Todd, B. (2025, March). *Will we have AGI by 2030?* 80,000 Hours, section "I. What's driven recent AI progress? And will it continue?" and section "III. Why the next 5 years are crucial". https://80000hours.org/ai/guide/when-will-agi-arrive/ Source note: [[Benjamin Todd - Will We Have AGI by 2030]].
[^owen-2030]: Owen, D. (2025, September 16). *What will AI look like in 2030?* Epoch AI, section "Scaling is likely to continue to 2030". https://epoch.ai/publications/what-will-ai-look-like-in-2030 Source note: [[David Owen - What Will AI Look Like in 2030]].
[^bluedot-2-1]: BlueDot Impact. *AGI Strategy, Unit 2: What drives AI progress?* Accessed 2026-10-21. https://bluedot.org/courses/agi-strategy/2/1 Quotes Todd's September 2026 assessment of his article.
