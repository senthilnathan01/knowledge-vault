---
type: source
source_type: article
status: synthesized
visibility: private
title: "Q2.5 2026 Timelines Update: Uplift and Revenue"
authors: ["Eli Lifland", "Daniel Kokotajlo", "Brendan Halstead"]
author_role: "AI Futures Project (authors of AI 2027 and the AI Futures Model)"
published: "2026-08-17 (byline; the page metadata gives 2026-08-16 UTC)"
publisher: "AI Futures Project blog"
url: https://blog.aifutures.org/p/q25-2026-timelines-update-uplift
accessed: "2026-10-22"
topics: [timelines, forecasting, recursive-self-improvement, uplift, scenarios]
concepts: ["Intelligence Explosion", "AI Timelines", "Measuring AI Capability"]
course: "BlueDot AGI Strategy, lesson 2.3 (assigned: the summary, the 3-parameter uplift model section, and the appendix subsection 'Clarification regarding what we're forecasting')"
published_in: []
created: "2026-10-22"
---

# Q2.5 2026 Timelines Update: Uplift and Revenue

The AI 2027 authors update their forecast of when AI will be good enough that a leading lab would rather fire its software engineers than give up AI coding. They add a new way to forecast it, from how much AI speeds up engineers, and find it agrees with their time-horizon method and a new revenue method. Their medians fall between late 2027 and early 2030, and they judge reality to be moving at about 70 to 90% of AI 2027's pace.[^aifutures-q25] It matters because it replaces a measure that was hard to pin down with one that is easier to tie to the milestone, and it shows a published scenario being graded against what happened.

This note covers the assigned parts: the summary, the 3-parameter uplift model, and one appendix subsection. It also uses a few lines from the "Updated forecasts" section and the chart descriptions for the authors' dates, marked where used. The revenue anchor and the full model's details weren't part of the reading.

## The authors forecast for a living and grade their own scenario

Eli Lifland, Daniel Kokotajlo and Brendan Halstead write for the AI Futures Project, the group behind the AI 2027 scenario ([[Kokotajlo et al - AI 2027]]) and the AI Futures Model, an interactive forecasting model at aifuturesmodel.com. The post is a planned periodic update ("Summary").[^aifutures-q25]

## The argument: uplift gives the same answer as time horizons and revenue

Each step reports what the post says, in its order. Section names are the post's.

### 1. The target milestone is the Automated Coder

*Section: "Summary"*

- The milestone they forecast is the **Automated Coder** (AC): an AI for which "the leading AI company would rather fire its human software engineers than forego AI usage for coding".
- Their headline (Tl;dr): "Our timelines haven't changed much (they got slightly shorter) but our modeling and evidence base have noticeably improved, so we feel somewhat more confident."

### 2. Forecasting from time horizons had "huge weaknesses"

*Section: "Summary"*

- Their original model used METR's coding time horizons (how long a task, in human time, an AI can complete; see [[Measuring AI Capability]]) to estimate how much effective compute AC needs (computing power adjusted for better algorithms; see [[Drivers of AI Progress]]).
- They give two weaknesses: it's unclear what time horizon AC corresponds to, or whether any finite value would; and people strongly disagree about whether the time horizon trend speeds up (is "superexponential") as compute grows, which leads to very different predictions.

### 3. Uplift is a better anchor, and three methods agree

*Section: "Summary"*

- Two new anchors: **coding uplift**, how much faster AI makes software engineers at AI companies, and revenue.
- Uplift is their favorite. Uplift minus 1 is the extra speed AI adds: 1x means no help, so 2x is one unit of extra speed. The method: estimate how fast the quantity (uplift minus 1) doubles, and extrapolate until it reaches the uplift that AC corresponds to. With uplift, the value at AC is "much less uncertain" than with time horizons.
- "Surprisingly, all 3 methods predict quite similar AC arrival dates." They take this as a "somewhat encouraging sign", though they are "still very uncertain".
- They re-graded AI 2027 against reality: "reality seems to be going about 70-90% as fast as AI 2027 predicted". Elsewhere in the post, at 75% of AI 2027's pace, AC would arrive in mid-2027 ("Comparing the AI 2027 pace of progress to reality").
- They changed the model to account for the fact that "training is needed to apply software improvements", which "reduces the chance of very fast takeoffs".

### 4. A simple model needs only three numbers

*Section: "A 3-parameter uplift model for predicting when Automated Coder will arrive"*

They call assuming that (uplift minus 1) grows exponentially "the best simple model for predicting when AC will arrive". The three inputs, with Daniel Kokotajlo's medians and the evidence the post gives for each:

| Input | Daniel's median | Evidence the post cites |
| --- | --- | --- |
| Today's coding uplift (speedup from AI assistance) | 2x | METR's study found 1.04x to 1.2x, which METR thought was biased low, so Daniel treats 1.04x as roughly a lower bound. An April 2026 Anthropic internal survey gave a geometric mean of 4x. A private estimate by Ryan Greenblatt gave 1.7x for AI research labor overall, "so presumably coding-only would be higher" |
| How long (uplift minus 1) takes to double | 5 months | Anthropic employee surveys went from 1.25x to 4x uplift in 7 months, about a 2-month doubling, or about 3.5 months after a correction. Employees probably overestimate, but unless that bias has been growing over time, it's still "a 3.6 month doubling time". Daniel's 5 months partly defers to colleagues who think it's longer |
| Uplift at which AC arrives | 20x | The full AI Futures Model says 32x in the median case; they expect the true figure to be a little lower |

- The post links a small app that runs this extrapolation. Its chart description gives AC in May 2028 with Daniel's medians.
- The full model adds three things. The doubling time shortens over time, because the share of coding tasks automated follows an S-curve rising toward everything. Automation of AI research changes how fast effective compute grows. And uplift at AC is worked out by the model, not set by hand.

### 5. The forecasts assume nothing slows things down on purpose

*Appendix: "Clarification regarding what we're forecasting"*

- They had been unclear whether they were forecasting what will actually happen, or what happens if things go as fast as technically possible. They now forecast the second: "conditional on things going as fast as is technically feasible", so a government slowdown, for example, isn't included.
- Their reason: they think that is "more informative to forecast" than trying to estimate the chances of each level of slowdown.

### 6. The authors' medians differ by about two years, their 90% dates by decades

*Section: "Updated forecasts" and its chart descriptions (outside the assigned parts)*

| Author | AC: 10% chance by | 50% chance by | 90% chance by |
| --- | --- | --- | --- |
| Daniel Kokotajlo | January 2027 | November 2027 (another chart gives December 2027) | April 2030 |
| Eli Lifland | June 2027 | January 2030 | October 2070 |
| Brendan Halstead | January 2027 | January 2029 | January 2050 |

These are all-things-considered forecasts, with each author's judgment applied on top of the model. Daniel's median for artificial superintelligence (ASI) is March 2029, so on his view superintelligence follows AC by under two years. Accounting for training time pushes his model's median gap from AC to ASI from 1.22 to 1.72 years (appendix chart description).

## The evidence is surveys, one study and a model

| Claim | Evidence | Where | How sure |
| --- | --- | --- | --- |
| Today's coding uplift is about 2x | METR study (1.04 to 1.2x), Anthropic survey (4x), one private estimate (1.7x) | 3-parameter model section | Authors' judgment across sources that disagree by a factor of four |
| (uplift minus 1) doubles every few months | Anthropic employee surveys over 7 months | Same section | Authors' estimate; they expect survey bias |
| Three anchoring methods agree | Model runs | "Summary" | Model output; authors still "very uncertain" |
| Reality runs at 70 to 90% of AI 2027's pace | Their grading across several metrics | "Summary" and "Comparing the AI 2027 pace of progress to reality" | Authors' own assessment of their own scenario |

## Claude's reading: uplift is a measurable form of the RSI loop, but it rests on self-reports

*Claude's reading, written during the ingest and not yet discussed. It is interpretation, not what the post says. Questions from it are in [[Open Questions]].*

- **The arithmetic is simple, so check it.** Starting at 2x, (uplift minus 1) is 1. Reaching 20x means it must reach 19, which is about 4.25 doublings. At 5 months each, that is about 21 months from August 2026, or around May 2028, which matches the app. Change the doubling time to 3.6 months and it is about 15 months, around November 2027. The forecast is very sensitive to that one number.
- **The weak link is the starting uplift.** The evidence spans 1.04x to 4x, and the high figure comes from employees rating themselves. METR's own report found self-reports have overstated gains before ([[METR - Frontier Risk Report February to March 2026]]).
- **"As fast as technically feasible" changes how to use these dates.** They are an upper-speed scenario, not a prediction of what will happen with regulation, slowdowns or the coordination the course discusses. Comparing them with Todd's forecasts ([[Benjamin Todd - Will We Have AGI by 2030]]) means comparing different questions.
- **Grading your own scenario is the right habit.** Writing a concrete path, then checking how fast reality is moving against it, is a method anyone can copy. It is in [[AI Timelines]].

## It feeds the intelligence explosion and timelines notes

- Feeds [[Intelligence Explosion]] (uplift as the measured quantity) and [[AI Timelines]] (scenarios graded against reality).
- Builds on [[Kokotajlo et al - AI 2027]] and [[Measuring AI Capability]] (time horizons).
- Course context: lesson 2.3 in [[BlueDot AGI Strategy Course]].

## It leaves open how to measure uplift without self-reports

- Could labs publish uplift measured from work records, as Anthropic did for its automation index, rather than from surveys?
- What would it take to forecast the realistic case, with slowdowns included?

## Sources

[^aifutures-q25]: Lifland, E., Kokotajlo, D., & Halstead, B. (2026, August 17). *Q2.5 2026 Timelines Update: Uplift and Revenue*. AI Futures Project blog. https://blog.aifutures.org/p/q25-2026-timelines-update-uplift Sections as named above; author dates are from the "Updated forecasts" chart descriptions.
