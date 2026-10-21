---
type: concept
status: active
visibility: private
created: 2026-10-21
tags: [ai-progress, timelines, forecasting, agi]
sources: ["Benjamin Todd - Will We Have AGI by 2030", "David Owen - What Will AI Look Like in 2030"]
---

# AI Timelines

"Timelines" means forecasts of when AI will reach capabilities that change the world. The useful version names a specific capability and asks when it arrives, because "when will we have AGI?" hides too much. Timelines matter for safety because they set how much time there is to solve alignment and build the oversight that powerful systems need.

This note builds on [[Drivers of AI Progress]], which explains what makes AI better. Here the question is how fast, and how to tell. It draws on the two lesson 2.1 readings in [[BlueDot AGI Strategy Course]]: Benjamin Todd (80,000 Hours) and David Owen (Epoch AI).

## "AGI" is too vague, so forecast specific milestones

People who ask "what are your timelines?" usually mean "when do you expect AGI?", but what counts as AGI is often left vague.[^bluedot-2-1] Todd defines it roughly as AI that matches human performance at most knowledge work, and says where the line is drawn is "ultimately arbitrary".[^todd-agi2030] The BlueDot course suggests tracking separate milestones instead, each with different consequences:[^bluedot-2-1]

1. Matching skilled humans at specific tasks, such as fixing software bugs or solving math problems.
2. Completing longer tasks without human help (measured by time horizons, below).
3. Automating all economically valuable work, at least as well and as cheaply as people.
4. Automating AI research and development, possibly before AI can automate many other jobs.
5. Being able to permanently take control away from humanity, if the systems tried, despite efforts to stop them.

A concrete case of why this matters: Todd says AGI in the sense of "better than almost all humans at reasoning when given an hour" seems "basically here already", while AGI in the sense of doing almost all remote work more cheaply than people may take much longer.[^todd-agi2030] Both are called "AGI", and they are years apart.

The course also separates four questions that "timelines" blurs together:[^bluedot-2-1]

- What resources and methods are improving? (covered in [[Drivers of AI Progress]])
- What can systems actually do? (time horizons, below)
- What would those capabilities change if adopted at scale? (capability before impact, below)
- Could AI change the process of improving AI? ([[Recursive Self-Improvement]])

## The task time horizon is the most watched single trend

A **time horizon** measures how long a task an AI can complete, using the time a human expert would need for it. METR, an AI evaluation organization, defines a one-hour horizon at 50% reliability as: the AI is predicted to succeed half the time on tested software tasks that take human experts about an hour.[^bluedot-2-1]

The trend, as Todd reported it in 2025: GPT-2 could do tasks that take humans a few seconds, GPT-4 a few minutes, and late-2024 reasoning models just under an hour. The horizon doubled about every seven months from 2020, and possibly every four months from 2024 (established trend data; whether it continues is debated).[^todd-agi2030] For scale: a seven-month doubling means about 3.4 doublings every two years, so roughly a tenfold longer task every two years.

By September 2026 Todd reported the 50% time horizon at 16 hours or more (about two working days of expert time), against his prediction of 6 hours for the end of 2026 (his assessment, as quoted by the course).[^bluedot-2-1] So the trend ran faster than his forecast.

Todd calls the key question "perhaps the central question of AI forecasting right now: will the horizon over which AIs can act plateau or continue to improve?"[^todd-agi2030]

## Extrapolating trends is the baseline, and it has done well so far

The main forecasting method is simple: measure the trends in compute, algorithms and benchmarks, and assume they continue. Epoch AI calls this "a strong baseline prediction" and says arguments for a coming slowdown "are often not compelling" (authors' judgment, after checking six such arguments).[^owen-2030]

Todd's own record is one test of the method. Of the predictions he made in early 2025 for the end of 2026, his September 2026 assessment says most held or were beaten: FrontierMath was saturated (he had predicted 50% to saturated), SWE-bench Verified and GPQA were saturated as predicted, Humanity's Last Exam reached 54% (he had predicted 40% to saturated), the time horizon beat his forecast, and lab revenue grew 6x a year instead of 4x.[^bluedot-2-1]

Todd's main miss was that shifting compute into reinforcement learning slowed pretraining; he also thinks he may have overemphasized test-time compute.[^bluedot-2-1] Claude's take (not yet discussed): that miss shows the method's weakness: it can't see interactions between drivers, or new drivers and limits, coming.

## The probability is concentrated in the next few years, then thins out

Todd's central argument is about the shape of the forecast, not just its median. Here transformative AI means AI that can speed up AI research itself, roughly milestone 4. The inputs to progress (the limits table in [[Drivers of AI Progress]]) can't keep growing at current rates much past 2030. So transformative AI is most likely to arrive while they are still growing fast. If it hasn't arrived by around 2028 to 2032, the yearly chance drops, because progress slows (author's view).[^todd-agi2030] His illustration: if compute and algorithms improved 50% a year instead of 3x, a jump like GPT-3 to GPT-4 would take over 14 years instead of 2.5.

That gives two broad scenarios, which he rates roughly 50:50:[^todd-agi2030]

- **Fast:** AI capable of transformative effects, especially on AI research, arrives by around 2030, and progress continues or accelerates.
- **Slowdown:** AI gets much better at well-defined tasks but not at messy, long, high-context work, and the world looks more normal.

By 2026 he added a third: a gradual slowdown after 2028 with AGI in 2030 to 2035, unless feedback loops start first. He also said his probability of AGI before 2029 had gone up.[^bluedot-2-1]

An analogy for the shape: a rocket with a fixed amount of fuel. If it reaches orbit, it reaches it while the engines are still burning. Once the fuel runs low, the chance of reaching orbit later gets small. The analogy breaks down in one important place: if AI starts contributing to AI research, it can make its own fuel, which is the loop in [[Recursive Self-Improvement]].

## The case against short timelines is about messy, uncheckable work

The strongest case against, in Todd's telling:[^todd-agi2030]

1. Grant that AI becomes superhuman at clearly defined tasks.
2. But tasks that are ill-defined, need lots of context, or take a long time have no quick way to check answers, so reinforcement learning can't train them and they aren't in the training data.
3. Most knowledge jobs are full of such tasks. If AI makes coding 10x faster but coding is half a software engineer's job, their overall productivity only roughly doubles.
4. So AI stays a powerful tool, humans remain the bottleneck, revenue doesn't justify the next round of investment, and progress slows after about 2028.

His counter is the time horizon trend: AI is getting better at longer tasks, and long tasks can often be broken into short ones.[^todd-agi2030] Claude's take (not yet discussed): the 16-hour result bears on this only partly, because METR's tasks are well-defined software tasks, the kind the case against already grants. It connects to verifiability in [[Drivers of AI Progress]].

## Capability arrives before impact

Both lesson 2.1 readings say capability will run ahead of visible effects on the economy:

- Todd: deployment is slowed by regulation, reliability, reluctance to let AI decide and institutional inertia, so "most of the economy will probably continue pretty much as normal for a while". AI research, being virtual and close to the labs, may automate first.[^todd-agi2030]
- Epoch: software changes fast, but drug development is slow. Few if any drugs approved by 2030 will have benefited from today's AI tools, though early-stage research will feel the effects. Its estimate for science is a 10 to 20% productivity gain within tasks, by analogy with software.[^owen-2030]

Claude's take (not yet discussed): this is why economic numbers are a poor early-warning sign. Todd says broad economic use "is therefore not necessarily a good way to gauge AI progress".[^todd-agi2030] For safety, the signals to watch are capability measures, especially how much of AI research AI is doing.

## Why it matters for safety: timelines set the deadline

Claude's take (not yet discussed):

- **Time for alignment work.** If transformative AI arrives around 2030, the alignment and monitoring problems in [[AI Safety - Problem Framings]] and [[Chain-of-Thought Monitoring]] need answers within a few years, not decades.
- **The milestones aren't equally dangerous.** Milestone 4 (automating AI research) can set off [[Recursive Self-Improvement]], which could compress the time between the later milestones. Todd says that if AI can do AI research, "the gap between AGI and 'superintelligence' could be short".[^todd-agi2030]
- **Situational awareness is on the same trend lines.** Todd lists a benchmark of whether models understand themselves and their context, rising from under 30% in 2022 to 60% at the end of 2024 (he gives no human or chance baseline).[^todd-agi2030] That is the capability behind evaluation awareness in [[AI Safety - Risk by Capability Level]].

## Sources

[^bluedot-2-1]: BlueDot Impact. *AGI Strategy, Unit 2: What drives AI progress?* Accessed 2026-10-21. https://bluedot.org/courses/agi-strategy/2/1 Includes METR's time horizon definition and quotes Todd's September 2026 assessment of his article.
[^todd-agi2030]: Todd, B. (2025, March). *Will we have AGI by 2030?* 80,000 Hours, Introduction and sections "4. The next stage: building better agents", "II. How good will AI become by 2030?", "III. Why the next 5 years are crucial" and "Two potential futures for AI". https://80000hours.org/ai/guide/when-will-agi-arrive/ Source note: [[Benjamin Todd - Will We Have AGI by 2030]].
[^owen-2030]: Owen, D. (2025, September 16). *What will AI look like in 2030?* Epoch AI, sections "Scaling is likely to continue to 2030" and "AI will accelerate scientific R&D across several domains". https://epoch.ai/publications/what-will-ai-look-like-in-2030 Source note: [[David Owen - What Will AI Look Like in 2030]].
