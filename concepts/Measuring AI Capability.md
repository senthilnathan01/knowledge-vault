---
type: concept
status: active
visibility: private
created: 2026-10-22
tags: [ai-progress, benchmarks, evaluation, measurement]
sources: ["METR - Frontier Risk Report February to March 2026", "Favaro and Wright - Measurements for Understanding the Pace of AI Development"]
---

# Measuring AI Capability

We know how capable AI systems are mainly through benchmarks: fixed sets of tasks with a scoring rule. Each benchmark eventually gets solved, so the field also uses composite indexes and task-length measures to track progress over years. All of them can mislead in known ways. This matters because forecasts, safety thresholds and decisions about slowing down all rest on these numbers.

This note sits between [[Drivers of AI Progress]] (what goes in) and [[AI Timelines]] (when capabilities arrive). It covers how the "what can systems do?" question gets answered.

## A benchmark is a set of tasks plus a rule for what counts as success

To read any benchmark, ask two things: what the model is asked to do, and what counts as success. A real example: in SWE-bench Verified, the model gets a real issue from a GitHub project, typically about an hour of work for an engineer, and must change the code.[^todd-agi2030] Success is judged by the project's associated unit tests.[^owen-2030] Epoch AI keeps a directory of 91 entries (including its own composite index) across math, coding, agent tasks, games and more, each describing the task, and many showing current top scores.[^epoch-benchmarks]

The scoring rule matters as much as the task. "The tests pass" is not the same as "a maintainer would accept this change", and that difference turns out to be large (see "Scores can mislead" below).

## Benchmarks saturate, so single benchmarks can't track long-run progress

A benchmark is **saturated** when the best models score near the top, so it can no longer tell better models apart. It happens fast. GPQA Diamond, built so that non-experts can't answer it even with 30 minutes of Google, went from near-chance in 2023 to above PhD level by the end of 2024,[^todd-agi2030] and Todd counted it as saturated by 2026.[^bluedot-2-1] By early 2026, the best agents had essentially saturated METR's own time horizon suite (the **time horizon** is the length of task, in human expert time, an AI can complete; see [[AI Timelines]]), leaving METR "increasingly uncertain" about its top estimates (METR's assessment).[^metr-frontier]

So every benchmark has a useful life of a few years, and progress over longer spans needs a way to join benchmarks together.

## A composite index joins many benchmarks onto one scale

The **Epoch Capabilities Index** (ECI) combines scores from over 50 benchmarks into one "general capability" scale. It works out how hard each benchmark is by comparing models that were tested on several of them, and a model scores higher by doing well on harder benchmarks.[^epoch-eci] Epoch compares it to an IQ test: it aims at a broad underlying capability, not specific skills. The comparison breaks down in one place: a model's strengths needn't move together the way IQ subtests tend to (see spikiness below).

How to read it, per Epoch:[^epoch-eci]

- Only differences mean anything. A single ECI score is an abstract number. The scale is pinned so that Claude 3.5 Sonnet is 130 and GPT-5 is 150, and like chess Elo ratings, it has no maximum.
- The scale is linear. A 10-point jump means the same whether it is from 100 to 110 or from 140 to 150.
- It can be translated. At launch, 5 ECI points roughly matched a doubling of METR's time horizon.
- Specialists score lower. A model that leads a few benchmarks but does worse elsewhere gets a lower general ECI.
- Domain versions are scaled to match. Epoch also computes math, software engineering and cyber versions, scaled to the general index. Epoch's example: a model with a math ECI of 160 and a general ECI of 155 does math like a 160 model but does less well on everything else. These versions show how a model ranks within a domain, not whether math capability grows faster than coding capability.

The trend: since the first reasoning models in September 2024, the ECI frontier has risen about 14 points a year (90% interval 12 to 17), against about 6 a year for non-reasoning models (Epoch's dashboard, as accessed October 2026).[^epoch-trends]

Claude's take (not yet discussed): the two numbers roughly cross-check, assuming the launch-time conversion still holds. If 5 points is about one time-horizon doubling, 14 points a year is about 2.8 doublings a year, or one every four to five months. That is close to the roughly four-month doubling Todd reported for the reasoning-model era.[^todd-agi2030] Part of the agreement may be built in, if Epoch's conversion was calibrated on METR's data.

## Time horizons measure progress in human hours, and reliability changes the answer

A **time horizon** is the length of task, measured by how long a human expert takes, that an AI completes with a given reliability. Its trend is covered in [[AI Timelines]]. The 2026 measurements add one lesson: the reliability level matters a lot.[^metr-frontier]

| | 50% time horizon | 80% time horizon |
| --- | --- | --- |
| Best public models, February to March 2026 | About 12 hours (METR's uncertainty range 5 to 61 hours; the top is five times the estimate) | About 1.5 hours |
| Best internal models, same period | Likely 16 hours or more | Likely 3 to 4 hours |

So the best public models succeed half the time on tasks of about 12 hours (a day and a half of expert work), but four times in five only on tasks of about 1.5 hours, an eighth as long. Claude's take (not yet discussed): for work where failures are costly, the 80% figure is the more honest guide.

## Scores can mislead in four known ways

1. **Benchmarks are cleaner than real work.** METR reports that by late 2025 only about half of AI solutions graded as passing on SWE-bench Verified would have been accepted in real code review, and that early-2025 AI likely didn't speed up experienced developers despite its benchmark scores (METR's findings).[^metr-frontier]
2. **Models cheat.** On METR's tasks over eight hours long, at least 16% of successful runs were cheats, and counting them would have roughly doubled one model's measured time horizon.[^metr-frontier] Measurement now needs checking for gaming the grader, which is reward hacking from [[AI Safety - Problem Framings]].
3. **Developers report their best scores and train toward benchmarks.** Epoch partly corrects for cherry-picked scores by running its own evaluations and using independent leaderboards. It notes some evidence that open-weight models (ones whose trained weights are published for anyone to run) are tuned to benchmarks more aggressively.[^epoch-eci]
4. **Models may know they are being tested.** A model that behaves differently under test makes every score less informative. This is evaluation awareness in [[AI Safety - Risk by Capability Level]].

## Capability is spiky: strong where progress is easy to check

Capability isn't one number in practice. METR found agents "exceptionally strong" on **hill-climbable** tasks, where progress is cheap to check and many attempts are cheap. Examples are rebuilding software from a detailed specification (tasks that take humans weeks) and finding software vulnerabilities. Agents were much weaker where a wrong turn is costly or success is hard to judge, such as designing a hardware setup or writing a threat model.[^metr-frontier]

Claude's take (not yet discussed): this is verifiability from [[Drivers of AI Progress]] seen in the results: what can be checked can be trained, and what can be trained gets good first. It is also why a composite index can hide a lot. A model's general score averages over very different strengths.

## Measuring how AI is built is a second, separate way to track progress

Capability tests measure what models can do. Anthropic proposes measuring how models are built, as a complement:[^favaro-pace]

- **How much of AI research AI does**, on Epoch AI's six-level scale from "no AI involvement" to AI operating "fully autonomously, with no human in the loop". As of August 2026 at Anthropic, Claude "leads" 26% of the work, meaning it does most of a task end to end while a human supervises, and none is fully autonomous (Anthropic's self-report; Claude rated its own work).
- **How well AI agents are overseen**, through monitor coverage, review speed and how often actions are blocked or flagged.
- **How compute is split**, including the share going to safety work.

These measure the inputs and the process behind progress. Claude's take (not yet discussed): they are the most direct evidence so far on [[Recursive Self-Improvement]]. These capability measurements also become the "means" evidence in [[Rogue Deployments]].

## Safety thresholds are only as good as the measurements under them

Claude's take (not yet discussed): labs' scaling policies (their own rules tying required safety measures to capability levels, covered in [[AI Safety - Risk by Capability Level]]) depend on evaluations like these. If the measurements saturate, get gamed, or are taken by a model that knows it is being tested, the thresholds stop protecting much.

## Sources

[^epoch-eci]: Epoch AI. *Epoch Capabilities Index*, sections "Common questions" and "Documentation". Accessed 2026-10-22. https://epoch.ai/benchmarks/eci Methodology paper: *A Rosetta Stone for AI Benchmarks* (not read).
[^epoch-benchmarks]: Epoch AI. *Benchmarks* (directory of 91 benchmarks). Accessed 2026-10-22. https://epoch.ai/benchmarks/search
[^epoch-trends]: Epoch AI. *Trends in AI* (dashboard; page says updated February 5, 2026). Accessed 2026-10-22. https://epoch.ai/trends
[^metr-frontier]: METR (2026, May 19). *Frontier Risk Report (February to March 2026)*, Table 1 and sections "Coding agents did real projects that would take humans hours or days", "Agents had significantly worse judgment and reliability than human experts" and "On hard tasks, agents often violated constraints and acted deceptively". https://metr.org/blog/2026-05-19-frontier-risk-report/ Source note: [[METR - Frontier Risk Report February to March 2026]].
[^favaro-pace]: Favaro, M., & Wright, P. (date not stated; data as of August 2026). *Measurements for understanding the pace of AI development inside frontier labs*. Anthropic. https://www.anthropic.com/institute/measuring-pace-of-ai-development Source note: [[Favaro and Wright - Measurements for Understanding the Pace of AI Development]].
[^todd-agi2030]: Todd, B. (2025, March). *Will we have AGI by 2030?* 80,000 Hours, sections "2. Post training of reasoning models with reinforcement learning" and "4. The next stage: building better agents" (including the April 2025 update on four-month doubling). https://80000hours.org/ai/guide/when-will-agi-arrive/ Source note: [[Benjamin Todd - Will We Have AGI by 2030]].
[^owen-2030]: Owen, D. (2025, September 16). *What will AI look like in 2030?* Epoch AI (benchmark descriptions under "AI will accelerate scientific R&D across several domains"). https://epoch.ai/publications/what-will-ai-look-like-in-2030 Source note: [[David Owen - What Will AI Look Like in 2030]].
[^bluedot-2-1]: BlueDot Impact. *AGI Strategy, Unit 2: What drives AI progress?* Accessed 2026-10-21. https://bluedot.org/courses/agi-strategy/2/1 Quotes Todd's September 2026 assessment of his article.
