---
type: blog
status: published
visibility: private
title: "Part 6: Evals, Optimization and Organizational Reality (What Actually Determines Success)"
slug: part-6-evals-optimization-and-organizational-reality-what-actually-determines-success
publishedAt: "2026-02-20T08:25:06.000Z"
heroImage: >-
  /images/blog/part-6-evals-optimization-and-organizational-reality-what-actually-determines-success/hero.png
contentFormat: markdown
category: tech
summary: "Part 6: Evals, Optimization and Organizational Reality (What Actually Determines Success)"
sourceContentFormat: html
sourceRepo: senthilnathan01.github.io
sourcePath: >-
  data/md_articles/part-6-evals-optimization-and-organizational-reality-what-actually-determines-success.md
sourceUrl: >-
  https://senthilnathan01.github.io/blog/part-6-evals-optimization-and-organizational-reality-what-actually-determines-success
importedAt: "2026-07-26"
tags:
  - sources
  - blogs
  - tech
heroImageUrl: >-
  https://senthilnathan01.github.io/images/blog/part-6-evals-optimization-and-organizational-reality-what-actually-determines-success/hero.png
---

# Part 6: Evals, Optimization and Organizational Reality (What Actually Determines Success)

(6th Part of the 7-Part series on what it takes to be a strong ML engineer in 2026)

**The hardest lesson I’m learning about ML engineering:**

Technical excellence is not enough.

You can build the perfect model. Implement flawless pipelines. Have bulletproof monitoring. Deploy with zero downtime.

And still completely fail to deliver value.

Why? Two reasons that nobody talks about enough:

1. **You didn’t measure the right things (evals)**
2. **The organization wasn’t set up for success (organizational context)**

Let me share what I’m learning about both.

### Evals: The Difference Between a Demo and a Product

Here’s the uncomfortable pattern I keep seeing:

**Month 1:** “Look at this amazing POC! 95% accuracy!”
**Month 3:**“We’re still working on production readiness…”
**Month 6:** “We decided not to move forward with this.”

What happened?

**They didn’t have real evals.**

They had metrics that looked good in development. But those metrics didn’t predict production success. Didn’t correlate with user value. Didn’t catch the failure modes that mattered.

**If you don’t have rigorous evaluation, your POC has a ~90% chance of never reaching production.**

Not because the model doesn’t work. Because you can’t prove it works, can’t measure when it degrades, and can’t iterate systematically.

**What I’m learning about real evaluation:**

**Offline evals that actually predict online performance:**

**This is harder than it sounds. Most offline evals lie.**

**What makes offline evals predictive:**

### Test sets that represent production distribution:

- Not just “held-out data from the same source”
- But data that looks like what you’ll see in production
- Including edge cases, adversarial examples, distribution shifts
- Updated regularly as production distribution changes

### Metrics that correlate with business value:

- Not just “accuracy” or “F1 score”
- But metrics that predict user satisfaction, retention, revenue
- Sometimes a “worse” model on traditional metrics wins on business metrics
- Measure what actually matters, not what’s easy to measure

### Subgroup analysis:

- Overall accuracy: 90%
- Accuracy on critical subgroup: 60%
- You just found a disaster waiting to happen
- Always slice your metrics by important dimensions

### Adversarial examples:

- Inputs designed to break your model
- Edge cases that seem unlikely but will happen at scale
- Systematic testing of failure modes
- If you don’t test it, production will

**Lesson: Your test set needs to be adversarial, not just representative.**

### Online evals that measure reality:

Offline metrics tell you what might happen. Online metrics tell you what actually happened.

**What I’m learning to measure online:**

### A/B testing with statistical rigor:

- Not just “model A vs. model B”
- But proper sample sizes, statistical significance, confidence intervals
- Account for novelty effects (early results often don’t hold)
- Run long enough to see long-term impacts

### Metrics that matter:

- Click-through rate
- Time spent
- Conversion rate
- User retention
- Not just “model accuracy”

### Leading indicators of problems:

- Metrics that degrade before users complain
- Changes in prediction distribution
- Shifts in feature values
- Increases in model uncertainty
- Catch problems early, before they compound

**Real-world example:**

- Recommendation system A/B test
- Model B had slightly better offline metrics
- Model B launched to 5% of users
- Engagement went up initially (novelty effect)
- But retention dropped after a week (users got bored of narrow recommendations)
- Good thing: canary deployment caught this before full rollout
- Offline evals missed the long-term retention impact entirely

### Continuous monitoring as ongoing evaluation:

Evaluation doesn’t stop after deployment. It’s continuous.

**What to monitor:**

### Model performance over time:

- Are metrics degrading?
- On which subgroups?
- How fast?
- What’s causing it?

### Distribution drift detection:

- Input distributions changing
- Output distributions changing
- Feature correlations changing
- Triggers for retraining

### User feedback loops:

- Explicit feedback (ratings, reports)
- Implicit feedback (engagement, behavior)
- Qualitative feedback (support tickets, surveys)
- Close the loop from feedback to model improvement

### Eval pipelines that run automatically:

- On every model change
- On every data change
- On schedule (daily, weekly)
- Before any deployment

### Regression test suites:

- “Model must maintain >X% on critical subgroup Y”
- “Model must not predict Z when feature W is present”
- “Model latency must stay under N milliseconds at p99”
- Fail the deployment if any regression test fails

### Eval dashboards:

- Real-time view of online metrics
- Historical trends
- Breakdowns by subgroup, geography, time
- Alerts when metrics degrade

> If you can’t measure it, you can’t improve it. And you probably shouldn’t deploy it.

### Optimization: Making Models Economically Viable

This is the part that’s humbling me right now.

A model that costs $10 per inference will never scale to production. No matter how good it is.

**Real constraints I’m learning about:**

### Cost per inference:

- What does each prediction actually cost?
- Token costs (for LLMs)
- Compute costs (GPU time)
- Infrastructure costs (serving, storage)
- Can you afford this at scale?

### Latency requirements:

- Users won’t wait 10 seconds
- Your model needs to be fast enough for your use case
- Or it doesn’t matter how accurate it is

### Throughput needs:

- How many requests per second?
- Can your infrastructure handle peak load?
- What’s the cost at peak vs. average?

**What I’m learning about optimization:**

### Model compression techniques:

### Distillation:

- Train small model to mimic large model
- Can achieve 90%+ of performance at 10% of size
- When to use: need to preserve quality, willing to invest in training
- Trade compute during training for efficiency during serving

### Quantization:

- Reduce precision of weights and activations
- FP32 → FP16 or INT8 or even INT4
- Dramatic speedups and memory savings
- Some accuracy loss (how much depends on the model and task)
- When to use: when you can afford small accuracy drops for big efficiency gains

### Pruning:

- Remove unnecessary parameters
- Surprisingly many weights can be zeroed out
- Reduces model size and compute
- Requires careful validation to avoid breaking the model

### Caching strategies:

### Prompt caching:

- Cache embeddings for repeated prompts
- Huge savings for common queries
- Works great when queries are repetitive
- Doesn’t help much for unique queries

### Result caching:

- Cache outputs for repeated inputs
- Instant responses for cache hits
- But: cache invalidation is hard
- But: how do you handle slight variations in input?

### KV cache optimization:

- Reuse cached key-value pairs in attention
- Critical for LLM serving efficiency
- Manage cache size vs. context length tradeoffs

### Prompt compression:

- Shorter prompts = fewer tokens = lower cost
- Remove unnecessary words
- Use abbreviations where possible
- But: don’t compress so much you lose meaning

### **What actually works (from people running this in production):**

**“We distilled GPT-4 to a smaller model for our specific use case. 95% of the quality at 5% of the cost.”**

**“Quantization to INT8 gave us 3x speedup with negligible quality loss for our task.”**

**“Caching saved us hundreds of thousands in LLM costs. 40% of our queries were effectively duplicates.”**

**“We optimized prompts from 1000 tokens to 300 tokens. Same quality, 70% cost reduction.”**

Every optimization is a tradeoff:

- Quality vs. speed
- Quality vs. cost
- Latency vs. throughput
- Accuracy vs. efficiency

### Organizational Context: Even Perfect Engineering Fails in Broken Systems

Here’s the part that most technical posts completely ignore.

And it’s the part that I’m realizing might matter most.

**You can be an exceptional ML engineer and still completely fail if the organization isn’t set up for success.**

**Real failure modes I’m learning about:**

### Data pipelines owned by teams that don’t understand ML:

**What happens:**

- ML team needs features with specific properties
- Data team builds pipeline that seems reasonable but breaks ML assumptions
- ML team discovers problems months later
- Finger-pointing ensues
- Nobody wins

**What’s needed:**

- Shared understanding of ML requirements
- Clear contracts and SLAs
- Regular communication
- Mutual respect for each other’s expertise

### Deployment processes that make iteration impossible:

**What happens:**

- Model needs emergency update (data drift, critical bug)
- Deployment requires 3 weeks of approvals
- By the time it’s approved, the problem has compounded
- Users have bad experience, trust erodes

**What’s needed:**

- Streamlined deployment for pre-approved model updates
- Emergency procedures for critical issues
- Trust in ML team’s judgment (earned through reliability)
- Fast rollback capabilities

### Monitoring systems that can’t handle ML metrics:

**What happens:**

- ML team needs to monitor distribution drift, calibration, subgroup performance
- Existing monitoring only supports basic metrics (latency, errors, throughput)
- ML-specific problems go undetected
- Models degrade silently

**What’s needed:**

- Monitoring infrastructure that supports custom metrics
- Investment in ML-specific observability
- Buy-in from infrastructure teams

### Success metrics that don’t reflect value:

**What happens:**

- ML team optimizes for accuracy
- Business cares about revenue
- Model gets 95% accuracy, revenue stays flat
- Business: “What was the point?”
- ML team: “But the model is great!”

**What’s needed:**

- Alignment on what success actually means
- Metrics that connect model performance to business outcomes
- Regular check-ins to ensure alignment

**What You Can Do:**

### Build relationships with data engineering:

- Understand their constraints and challenges
- Explain ML requirements clearly
- Collaborate on pipeline design
- Create shared ownership of data quality

### Advocate for ML-friendly infrastructure:

- Make the case for necessary tooling
- Show ROI of proper monitoring, deployment, etc.
- Start small, demonstrate value, expand
- Don’t ask for everything at once

### Educate stakeholders on meaningful metrics:

- Explain why accuracy isn’t enough
- Connect model metrics to business outcomes
- Set realistic expectations
- Celebrate real wins, not vanity metrics

### Create feedback loops:

- From model performance to business outcomes
- From user feedback to model improvements
- From production issues to training data
- From online metrics to offline evaluation

**ML engineering is not just technical. It’s organizational.**

You’re not just building models. You’re building systems that exist in organizations with people, processes, politics, and constraints.

Ignoring the organizational context doesn’t make it go away. It just means you’ll be surprised when it blocks you.

**Real stories that illustrate this:**

**Story 1: Perfect model, broken deployment**

- Team built amazing model
- Deployment process required 6 weeks of security reviews
- By the time it was approved, the business priorities had changed
- Model never deployed
- Lesson: Understand deployment constraints early

**Story 2: Model that measured the wrong thing**

- Team optimized for click-through rate
- Business wanted revenue
- CTR went up, revenue went down (people clicked but didn’t buy)
- Misaligned incentives from the start
- Lesson: Align on success metrics before building

**Story 3: Data pipeline that broke ML assumptions**

- Data team built aggregations that seemed reasonable
- But introduced temporal leakage for ML use case
- ML team discovered this 3 months into training
- Had to rebuild from scratch
- Lesson: Involve ML in data pipeline design

The best ML engineers I’m learning from aren’t just technically excellent.

They’re also:

- Great at measurement and evaluation
- Conscious about economic constraints
- Skilled at navigating organizations
- Effective at communication and alignment

**Technical skills are necessary. But not sufficient.**

**What organizational challenges have blocked your ML work? What would you do differently?**

And as always, if you have experience with evals, optimization, or organizational ML that I’m missing please share it. This is how we all learn.

### Tomorrow: Part 7 (Final)

Putting it all together. What this actually means for becoming a great ML engineer in 2026.

Building real systems end-to-end. Learning from failure. The path forward.

## Sources

- [Original published article](https://senthilnathan01.github.io/blog/part-6-evals-optimization-and-organizational-reality-what-actually-determines-success)
