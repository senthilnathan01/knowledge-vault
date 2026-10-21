---
type: source
source_type: article
status: synthesized
visibility: private
title: "Measurements for understanding the pace of AI development inside frontier labs"
authors: ["Marina Favaro", "Phillie Wright"]
author_role: "Anthropic (roles not stated on the page)"
published: "not stated (measurements are as of July to August 2026)"
publisher: "Anthropic"
url: https://www.anthropic.com/institute/measuring-pace-of-ai-development
accessed: "2026-10-22"
topics: [recursive-self-improvement, measurement, oversight, compute, transparency]
concepts: ["Recursive Self-Improvement", "Chain-of-Thought Monitoring", "Measuring AI Capability"]
course: "BlueDot AGI Strategy, lesson 2.2 (assigned: section 1, footnote 1, and the appendix on AI-led R&D)"
published_in: []
created: "2026-10-22"
---

# Measurements for understanding the pace of AI development inside frontier labs

Anthropic proposes three numbers any frontier lab could publish to show how fast AI is building AI: how much of its research AI does, how well it oversees its AI agents, and how much of its compute goes to safety. It reports its own: as of August 2026, Claude "leads" about a quarter of Anthropic's AI research work, but no part runs fully autonomously.[^favaro-pace] Claude's reading: it matters because it puts a first number on [[Recursive Self-Improvement]] (RSI, AI doing a growing share of the work of building better AI), and shows what outsiders would need in order to check.

## The authors write for the lab whose numbers they report

Marina Favaro and Phillie Wright co-authored the piece for Anthropic, with research direction from Jack Clark, and the page thanks reviewers including Peter Wildeford and Eli Lifland (closing credits).[^favaro-pace] The page gives no publication date; its measurements cover July and August 2026.

This is a lab reporting on itself. One of two obstacles the authors name is that Anthropic used its own model to rate its own automation (section 1).[^favaro-pace]

## The argument: the public needs three measurements, and here is a first set

Each step reports what the piece says, in its order.

### 1. The public needs to see inside labs to decide about pacing

*Introduction and "Reasons to track these measurements"*

- AI systems have "begun to automate more of the process of building themselves", and the world is considering slowing frontier development, so the public needs more information.
- The three measurements focus on how models are built, as a complement to capability tests, which measure what models can do. Anthropic plans to embed independent third-party evaluators from several organizations, with access comparable to its internal risk teams, to verify practices and monitor metrics like these.
- Anthropic expects its numbers to shift if labs coordinated on pacing the frontier, which its CEO Dario Amodei has called for. **Pacing** here means deliberately slowing or timing frontier development, ideally coordinated across labs.

### 2. AI-led research: Claude leads about a quarter of the work, and none is fully autonomous

*Section "(1) Measuring AI-led AI R&D" and its appendix*

- Why: labs use AI to build future AI, which speeds development but "could make it more challenging for humans to understand or control these systems". The measurement shows how close the world is to recursive self-improvement, which the authors define as "a model fully autonomously building its successor".
- The scale: Epoch AI's six **automation levels** (AL). At AL3, AI "collaborates": it does large chunks of work under close human direction. At AL4, AI "leads": it can complete most of a task end to end from a high-level prompt while a human supervises. The full scale runs from AL0 (no AI involvement) through minimal involvement, "assists", "collaborates" (AL3), "leads" (AL4), to "autonomous" (AL5, no human in the loop).
- The page's example, a broken overnight data pipeline (footnote 1):
  - At AL3, an engineer brings Claude the logs and a hypothesis, stays involved, decides what to do when new problems turn up, and reviews the fix line by line.
  - At AL4, the engineer just hands Claude the failure alert. Claude finds the cause, writes and tests the fix, handles surprises, and writes up what it did. The engineer reads the write-up, skims the change and decides whether to ship.
  - At AL5, which Anthropic hasn't reached, Claude would notice the failure itself, fix it and deploy it, with no human needed.
- Findings as of August 2026: Claude does not operate fully autonomously on any measured part of AI research work; it "leads" 26% of the work; and over 90% of the work is at "collaborates" or above.
- Method, which Anthropic calls the Anthropic R&D Automation Index: a Claude research agent reviewed a random 20% of research staff each week of July 2026, using Slack and internal documents, which produced about 15,000 tasks. Claude organized these into a tree of 378 task types, then froze it so every later measurement uses the same basket of work. Claude agents researched how automated each type was, and a separate Claude "judge" assigned the level. Each task type is weighted by how much staff time goes into it.
- Checks: staff who own each area rated automation without seeing the model's evidence. The judge agreed exactly with humans 59% of the time, while humans agreed with each other 35% of the time, and model and human were within one level 97% of the time. So staff agreed with each other less often than with the judge, and exact levels are noisy; the page flags "real room for disagreement" on where "collaborates" ends and "leads" begins, which is exactly the line the 26% depends on. Because a frozen basket can't show new kinds of work appearing, Anthropic built a second version from January 2026 data and found no rise in new kinds of work, suggesting the shape of research work is stable at this level of detail.
- Two obstacles to comparing labs: there is no shared method yet, and a lab's own model judges its own work, so the judge "could make the same kinds of errors as the model it is checking". The proposed fix: verification by a third party or by other labs' models. Such measures could also trigger stricter rules, such as a fixed testing window before a new model is used for further AI research.

### 3. Oversight of agents: on the main internal platform, every action is monitored and about 1 in 47,000 is blocked

*Section "(2) Measuring oversight of AI agents"*

- Why: as work moves from "AI collaborates" toward "AI leads", agents make more consequential decisions. Individual agents rarely misbehave in Anthropic's data, but "when there are millions or billions of agents operating in the economy, even rare events can happen regularly".
- Three metrics: **coverage** (the share of agent actions a monitor sees), **review latency** (how long until an automated monitor, then a human, reviews an action) and **escalation rate** (the share of actions blocked or flagged).
- Findings for August 2026, on Anthropic's most-used internal platform, with about 30,000 agents working at any one time:

  | | Online monitor (real time) | Offline monitor (after the fact) |
  | --- | --- | --- |
  | Built for | Fast, irreversible harms, such as copying model weights out | Slow, reversible problems, such as signs of misalignment |
  | Coverage | 100% of actions, checked before they run, usually within seconds | 100% of actions, reviewed afterward |
  | Review | Humans review any blocked action within a week | About 100,000 flags a week are filtered by classifiers; about 50 a week reach human review |
  | Rate | 0.002% of over a billion decisions blocked, about 1 in 47,000 | One to two transcripts in every thousand flagged |

- Two design choices help oversight (appendix): each agent has its own identity, so every action can be traced to it and agents treat each other's outputs "as a claim to check rather than a thought of its own"; and agents communicate in an open shared channel rather than privately, so monitoring can follow their conversations.
- Labs should also report how often known misbehavior is caught, and have third parties test it. The page notes METR has red-teamed Anthropic's offline monitoring, and says Anthropic has been doing this kind of monitoring "for months, not years".

### 4. Compute: about 6% of research compute goes to safety

*Section "(3) Measuring compute allocation"*

- Why: compute is "among the most verifiable inputs" to AI research, so it could be a key lever in any pacing effort, for example one that would encourage labs to put more compute into safety.
- Finding for one week in July 2026: about 6% of the compute used for AI research went to safety work, and about 12% of the compute used for AI-driven AI research (research done by AI agents) did. The estimate is deliberately conservative: work that helps capability as much as safety counted as capability, and the figures leave out safeguard classifiers, which the page says use a separate, comparable amount of compute.
- The authors caution that safety research needs less compute by nature, so the value is in comparing like with like over time and across labs, not in the absolute number. Drawing the line between safety and capability work is hard, so "the burden of proof should sit with the developer".

### 5. The aim is to close the gap between what labs and the public know

*Section "Conclusion"*

The piece ends by saying the world should "minimize the gap between what frontier labs know and what the public knows" as it considers pacing the frontier, and Anthropic will keep releasing such measurements.

## The evidence is Anthropic's own data, partly checked by its staff

| Claim | Evidence | Where | How sure |
| --- | --- | --- | --- |
| No AI research work is fully autonomous; Claude leads 26% | Anthropic R&D Automation Index | Section 1 | Lab's self-report; judge model checked against staff ratings |
| Over 90% of work is at "collaborates" or above | Same index | Section 1 | Same |
| 100% monitoring coverage; 1 in 47,000 actions blocked | Monitoring data, August 2026, one platform | Section 2 | Lab's self-report; covers the most-used platform only |
| About 6% of AI research compute goes to safety | One week of workload classification | Section 3 | Lab's self-report; one week is not a trend |

## Claude's reading: a measured answer to "how far along is RSI?"

*Claude's reading, written during the ingest and not yet discussed. It is interpretation, not what the page says. Questions from it are in [[Open Questions]].*

- **It puts a number on Selsam's and Pachocki's claims** ([[Daniel Selsam - Personal Statement on AI Risk]], [[Jakub Pachocki - An Alien Mind]]). Both said AI was doing more of AI research. Here, at one lab in August 2026, AI leads about a quarter of the work and none is autonomous. METR's report, covering February to March 2026, five months earlier, found no evidence that any company relied on agents to set research agendas, and Anthropic argued its pace of progress had not doubled as of April 2026 ([[METR - Frontier Risk Report February to March 2026]]). So the loop in [[Recursive Self-Improvement]] has started, but humans still choose what to work on.
- **The weak point is the judge.** Claude rated how much Claude does. Anthropic checks this against staff ratings and proposes outside verification, which is the right fix. But until other labs publish on a shared method, there is nothing to compare against. This is the "how could anyone outside a lab check?" question in [[Open Questions]], with a concrete proposal attached.
- **The monitoring numbers and METR's red-teaming measure different things.** Anthropic reports 100% coverage in August 2026, on one platform. METR's earlier red-teaming found coverage gaps (non-Claude Code traffic wasn't covered, and one environment variable could switch monitoring off) and that simple jailbreaks fooled the monitor. They may not conflict, since they cover different dates and scope, but a coverage figure alone can overstate oversight.

## It extends the RSI and monitoring notes

- Builds on [[Recursive Self-Improvement]] and [[Chain-of-Thought Monitoring]], and the measurement ideas in [[Measuring AI Capability]].
- Pairs with [[METR - Frontier Risk Report February to March 2026]], the other lesson 2.2 reading.
- Course context: lesson 2.2 in [[BlueDot AGI Strategy Course]].

## It leaves open who checks the lab's own numbers

- Will other labs publish the same three measurements on a shared method, and who will verify them?
- How fast does the 26% "leads" share grow from month to month? The page gives one snapshot.

## Sources

[^favaro-pace]: Favaro, M., & Wright, P. (date not stated; data as of August 2026). *Measurements for understanding the pace of AI development inside frontier labs*. Anthropic. https://www.anthropic.com/institute/measuring-pace-of-ai-development
