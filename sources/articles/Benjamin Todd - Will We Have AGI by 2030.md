---
type: source
source_type: article
status: synthesized
visibility: private
title: "Will we have AGI by 2030?"
authors: ["Benjamin Todd"]
author_role: "Writes for 80,000 Hours (role not stated on the article page); says he has written about AGI since 2014"
published: "2025-03 (day not stated)"
publisher: "80,000 Hours"
url: https://80000hours.org/ai/guide/when-will-agi-arrive/
accessed: "2026-10-21"
topics: [ai-progress, scaling, timelines, forecasting, agents]
concepts: ["Drivers of AI Progress", "AI Timelines", "Recursive Self-Improvement"]
course: "BlueDot AGI Strategy, lesson 2.1 (core reading; the course calls it 'The case for AGI by 2030')"
published_in: []
created: "2026-10-21"
---

# Will we have AGI by 2030?

Benjamin Todd argues that four drivers of AI progress (scaling pretraining, reinforcement learning for reasoning, test-time compute and agent scaffolding) can all keep going until about 2028, so AI that transforms research could plausibly arrive by around 2030. If it doesn't, progress will likely slow, because the money, power, chips and researchers behind it can't keep growing at today's rates much past 2030.[^todd-agi2030] It matters to the vault because it lays out the four drivers in one place and names 2028 to 2032 as the window when we'll learn which way things go.

## The author forecasts from public trends, not inside knowledge

Todd writes for 80,000 Hours, an organization that advises people on high-impact careers, and the article is part of its AGI careers guide. He describes himself as a non-expert who has written about AGI since 2014, and he builds his case from public data, much of it from Epoch AI (sections "Introduction" and "When do the 'experts' expect AGI to arrive?").[^todd-agi2030]

He also scored his own forecasts 18 months later. That follow-up, quoted on the course page, has its own section after the argument below.[^bluedot-2-1]

## The argument: four drivers keep going to about 2028, then hit limits around 2030

Each step reports what Todd says, in his order. Section names are his.

### 1. Lab leaders became confident fast, and the question is whether it's hype

*Section: Introduction*

- Between late 2024 and January 2025, the heads of OpenAI, Anthropic and Google DeepMind all spoke with growing confidence about rapid progress. Demis Hassabis, for example, Demis Hassabis went from "as soon as 10 years" to "probably three to five years away".
- Todd defines AGI roughly as AI that matches human performance at most knowledge work, and says where the line is drawn is "ultimately arbitrary". What matters is whether AI can start to speed up AI research itself.
- Where the line is drawn matters less than what such AI could do: speed up AI research, and possibly "trigger explosive growth and 100 years of scientific progress in 10".
- His thesis: the drivers of progress can't keep growing at current rates much beyond 2030, so "we either reach AI systems capable of triggering an acceleration soon, or progress will most likely slow significantly".

### 2. Betting against deep learning has repeatedly failed

*Section: "The deep learning era"*

- His example: in 2022 Yann LeCun said no text-trained model would learn that an object on a table moves when the table is pushed. Within a year, GPT-4 answered that question correctly.
- AI has repeatedly gone from incompetent to better than humans at a task within a couple of years, so current limitations are a poor guide to where things are heading.

### 3. Progress comes from compute and algorithms, through four drivers

*Sections: "What's coming up" and "1. Scaling pretraining to create base models with basic intelligence"*

- At the broadest level, progress comes from more computing power and better algorithms. He breaks it into four drivers: scaling pretraining, reinforcement learning for reasoning, test-time compute (letting models think longer), and agent scaffolding. This note uses those four names throughout.
- **Pretraining** is the first stage of training: the model predicts missing text from the internet, is scored, and is adjusted, trillions of times. More training compute lets the model have more parameters and learn from more data.
- Training compute for leading models has grown more than 4x per year, far faster than chip performance alone (about 35% per year). Each 10x increase has brought steady gains across many benchmarks. This regular relationship is called a **scaling law**.
- Algorithms improve too: the compute needed for the same performance has fallen tenfold every two years, about 3x per year. Combined with 4x more compute, that gives about 12x more **effective compute** each year.
- From GPT-2 to GPT-4 was about a 300,000x increase in effective compute. On current trends, another 300,000x (a hypothetical "GPT-6") is reachable by about 2028, at roughly $10 billion per training run, which the biggest tech companies can afford. Training data is the most plausible bottleneck, but he cites analysis that there is enough for a GPT-6-scale run by 2028.

### 4. Reinforcement learning taught models to reason

*Section: "2. Post training of reasoning models with reinforcement learning"*

- Post-training is training after pretraining. RLHF (reinforcement learning from human feedback) trained models to give answers human raters found helpful.
- The newer method trains models to solve problems with verifiable answers, such as math, by rewarding chains of reasoning that reach the right answer. It started working in 2024.
- The result: on GPQA Diamond, a set of science questions that PhDs in the field can mostly answer but others can't, GPT-4 scored barely above random guessing in 2023. OpenAI's o1, built on GPT-4o with reinforcement learning, reached 70% in late 2024, about equal to PhDs. o3 went beyond expert level.
- The reinforcement learning stage of DeepSeek-R1 likely cost about $1 million, so labs could scale it about 1,000x at $1 billion. Models can generate their own training data here: solve many problems, keep only the verified correct solutions, and train the next model on them, which creates a flywheel.
- It works best where answers can be checked (math, science, coding). How well it carries over to areas like business strategy or writing is "a crucial question going forward".

### 5. Letting models think longer buys capability early

*Section: "3. Increasing how long models think"*

- **Test-time compute** is computing power used while the model runs rather than while it trains. OpenAI showed o1 getting steadily more accurate on coding problems as it was allowed to think up to 100 times longer.
- Todd estimates GPT-4o could usefully think for about a minute, and o1 and DeepSeek-R1 for the equivalent of about an hour.
- The upshot: paying more lets you reach future capabilities early. He expected that in 2026 you could pay 100,000 times more to get performance otherwise available in 2028.
- This also enables another flywheel, iterated distillation and amplification: let a model think longer for better answers, train a new model to give those answers instantly, then repeat. He says this is essentially how AlphaZero became superhuman at Go without human data.

### 6. Agents are the next stage, and the most uncertain driver

*Section: "4. The next stage: building better agents"*

- An agent is a reasoning model with memory and tools that works through a long chain of tasks toward a goal: plan, act, observe the result, update the plan, repeat.
- On SWE-bench Verified, real software problems that typically take about an hour, GPT-4 in a simple agent setup solved about 20%, Claude 3.5 Sonnet 50%, and o3 reportedly over 70%.
- On RE-Bench, a set of hard AI research engineering tasks from METR (an organization that evaluates AI models), agents built on o1 and Claude 3.5 Sonnet beat human experts given two hours. Humans still won when given more than about four hours.
- METR's time horizon measure: GPT-2 could do tasks that take humans a few seconds, GPT-4 a few minutes, and late-2024 reasoning models just under an hour. The trend doubled about every seven months since 2020, and possibly every four months since 2024. If it continued, AI would handle multi-week tasks by 2028.
- Reliability compounds: a 20-step task with 90% success per step succeeds only about 10% of the time; at 99% per step it succeeds about 80% of the time. So small reliability gains can suddenly make agents useful.
- He calls agents "the most uncertain of the four drivers": there are no great benchmarks for it, and more fundamental breakthroughs might be needed.

### 7. Extrapolated, the trends point to beyond-human coding and reasoning by about 2026 to 2028

*Section: "II. How good will AI become by 2030?"*

- In the next two years he projects: a base model with 500x GPT-4's effective compute, trained to reason with up to 100x o1's compute, able to think for the equivalent of a month on a task, inside better agent scaffolding. By 2028, $10 billion runs.
- New drivers like reasoning models have appeared every one to two years, so he expects at least one more by 2028.
- Extrapolating benchmarks to the end of 2026, he expects AI with expert-level knowledge in every field, better-than-human coding, general reasoning better than almost all humans, and the ability to complete many day-long computer tasks on its own.

### 8. Deployment lags, except in software, science and AI research

*Section: "What jobs would these systems be able to help with?"*

- Many things slow real-world deployment: regulation, reluctance to let AI decide, reliability, institutional inertia, no physical presence. So "most of the economy will probably continue pretty much as normal for a while".
- Three areas could move fast anyway: software engineering (he cites Google saying about 25% of its new code is AI-written), scientific research in virtual, verifiable domains, and AI research itself.
- AI research is "especially amenable to acceleration": it is fully virtual, AI researchers understand it best, they have huge incentives to automate it, and nothing stops them deploying AI on it. So AI may do AI research before it can do most remote jobs, and broad economic impact is "not necessarily a good way to gauge AI progress".

### 9. The strongest case against: messy, long tasks

*Section: "What's the case against impressive AI progress by 2030?"*

- Grant that AI becomes superhuman at clearly defined tasks. The case against says it stays poor at ill-defined, high-context, long tasks, because those have no quick way to check answers, so reinforcement learning can't train them, and they aren't in the training data.
- Most knowledge jobs are full of such tasks. His example: if AI makes coding 10x faster but coding is half a software engineer's job, their overall productivity only roughly doubles.
- A prime example of messy work is having new conceptual insights. On this view, that task, which matters most for setting off an acceleration, may be "the hardest to automate", contrary to people who think AI research may be easier to automate than many other jobs.
- In that world AI stays a tool, humans remain the bottleneck, revenue doesn't justify runs above $10 billion, and progress slows a lot after about 2028.
- His counter: METR's time horizons keep growing, and long tasks can often be broken into short ones. He calls this "perhaps the central question of AI forecasting right now: will the horizon over which AIs can act plateau or continue to improve?"
- Other ways it could be slower: cognitive work alone may not be very useful without broader automation, pretraining may hit diminishing returns, poor visual perception, benchmarks overstating progress, a crisis or a Taiwan conflict, or other unforeseen bottlenecks.

### 10. Every group of forecasters has shortened its estimates

*Section: "When do the 'experts' expect AGI to arrive?"*

- There are no reliable experts on this, only groups with different drawbacks. But every group's estimates have shortened sharply. On Metaculus, a forecasting site, the mean estimate for AGI fell from 50 years away to 5 years away in four years.
- He concludes AGI by 2030 is "within scope of expert opinion". His analogy: if 30% of experts think a plane will explode, non-experts shouldn't conclude it definitely won't.

### 11. The next five years are crucial because the inputs can't keep growing

*Section: "III. Why the next 5 years are crucial"*

- Powerful AI is most likely to be found while the compute and workforce behind it are growing fastest. Total AI compute is growing about 3x per year.
- Money: another 10x beyond a GPT-6-scale run needs hundreds of billions of dollars, comparable to the Apollo program. GPT-8 would need trillions.
- Power: AI chips could use 4% or more of US electricity by 2028; another 10x would be 40% or more.
- Chips: TSMC, which makes all leading AI chips, could comfortably make 5x more, but 50x would be a huge challenge.
- Researchers: each discovery makes the next harder, so steady progress needs an exponentially growing research workforce. OpenAI grew from about 300 to about 3,000 employees since 2021, and that can't continue indefinitely.
- So compute growth likely slows around 2028 to 2032. If compute and algorithms improved 50% a year instead of 3x, a jump like GPT-3 to GPT-4 would take over 14 years instead of 2.5.
- This sets up a race: can AI earn enough to pay for the next round, and can it contribute to research before the human research workforce runs out?

### 12. Two scenarios, roughly even odds

*Sections: "Two potential futures for AI" and "Conclusion"*

- Either AI capable of transformative effects arrives by about 2030 and progress continues or accelerates, or progress slows: AI gets much better at well-defined tasks but can't do the messy long-horizon work, and the world looks more normal. He puts these at roughly 50:50, varying "between 30% and 80% depending on the day".
- He says it "seems clearly overconfident" to put the chance of AGI before 2030 below 10%.
- If AI can do AI research, the gap between AGI and superintelligence could be short.

## His 2026 follow-up: the drivers held, and progress outran his forecasts

This section reports a different source: Todd's own assessment of the article, posted on September 22, 2026 and quoted in full on the BlueDot lesson 2.1 page.[^bluedot-2-1]

Todd says the four drivers kept working, as predicted. Comparing his end-of-2026 predictions with what happened:

| Measure | His 2025 prediction for end of 2026 | What happened, per Todd |
| --- | --- | --- |
| FrontierMath (very hard math problems built by Epoch AI) | "50% to saturated" | Saturated |
| METR 50% time horizon (the length of task, in human expert time, the model completes half the time) | 6 hours | 16 hours or more |
| Humanity's Last Exam (about 3,000 questions at the edge of human knowledge) | "40% to saturated" | 54% |
| SWE-bench Verified and GPQA | Saturated | Saturated |
| Frontier lab revenue growth | 4x per year | 6x per year |

What he would change: he underweighted how shifting compute into reinforcement learning would slow the pretraining trend, and may have overemphasized test-time compute. He would now give more weight to a third scenario, a gradual slowdown after 2028 with AGI in 2030 to 2035, unless feedback loops kick in first. But his probability of AGI before 2029 has gone up.

## Most of the evidence is public trends, extrapolated

| Claim | What the article offers as evidence | Where | How sure |
| --- | --- | --- | --- |
| Effective compute grows about 12x per year | Epoch AI data on training compute (4x) and algorithmic efficiency (3x) | "1. Scaling pretraining" | Established trend data, as cited |
| Reinforcement learning made models reason at PhD level on science questions | GPQA Diamond scores for GPT-4, o1, o3 | "2. Post training" | Reported benchmark results |
| Agents' time horizon doubles every 4 to 7 months | METR's time horizon data | "4. The next stage" | Reported trend, new when the article was written; its continuation is debated |
| The drivers continue to about 2028 | Extrapolation of the above, plus cost estimates | "II. How good will AI become by 2030?" | Author's view; his 2026 follow-up says they did |
| Inputs hit bottlenecks around 2028 to 2032 | Estimates of money, power, chips and workforce growth | "III. Why the next 5 years are crucial" | Author's view, built on cited estimates |
| AGI by 2030 is about even odds | His judgment | "Two potential futures for AI" | Author's view, which he says swings from 30% to 80% |

## Claude's reading: the "now or slowdown" structure is the part to keep

*Claude's reading, written during the ingest and not yet discussed. It is interpretation, not what the article says. Questions from it are in [[Open Questions]].*

- **The lasting idea is that timelines aren't spread evenly across the future.** Because the inputs to progress can't keep growing at today's rates past about 2030, a lot of the probability of transformative AI is concentrated in the next few years. If it doesn't arrive then, the yearly chance drops. That holds even if the benchmark forecasts are off, as long as the inputs really do stop growing fast around 2030.
- **His 2026 scorecard is a useful check on extrapolation.** Most predictions held or were beaten, which supports trend extrapolation as a method. But the main thing he got wrong (compute shifting to reinforcement learning slowed pretraining) is a reminder that the drivers interact, so extrapolating each separately can mislead.
- **The case against is about verifiability, and so is the safety angle.** Reinforcement learning works where answers can be checked. The same property decides where AI gets good first. Todd's point that AI research may be automated before most jobs connects directly to [[Recursive Self-Improvement]]: the field that would set off the loop may also be one of the easiest to automate, though Todd's own case against says its insight-heavy part may be the hardest.
- **The step to check first** is whether METR's time horizons keep growing on messy, real work, not just well-defined software tasks.

## It feeds the drivers and timelines notes, and the RSI note

- Feeds [[Drivers of AI Progress]] (the four drivers, effective compute, verifiability) and [[AI Timelines]] (milestones, time horizons, the two scenarios, the bottlenecks around 2030).
- Extends [[Recursive Self-Improvement]]: why AI research may be automated early, and the race between AI contributing to research and the inputs running out.
- Pairs with [[David Owen - What Will AI Look Like in 2030]], the other lesson 2.1 reading, which looks at the same inputs from Epoch AI's side.
- Course context: core reading for lesson 2.1 in [[BlueDot AGI Strategy Course]].

## It leaves open whether the time horizon trend survives messy work

- Will time horizons keep doubling on ill-defined, high-context work, or only on tasks with checkable answers?
- If the article is right that AI research automates before most jobs, what early signal would show it from outside a lab?

## Sources

[^todd-agi2030]: Todd, B. (2025, March). *Will we have AGI by 2030?* 80,000 Hours. https://80000hours.org/ai/guide/when-will-agi-arrive/ (day of publication not stated; the course links the same article at https://80000hours.org/agi/guide/when-will-agi-arrive/)
[^bluedot-2-1]: BlueDot Impact. *AGI Strategy, Unit 2: What drives AI progress?* Accessed 2026-10-21. https://bluedot.org/courses/agi-strategy/2/1 The page quotes Todd's September 2026 assessment of his article and links it to a post on X (https://x.com/ben_j_todd/status/2102381077826285922, dated 09/22 on the course page), which was not opened.
