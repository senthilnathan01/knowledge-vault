---
type: blog
status: published
visibility: private
title: "Part 4: Production Systems (Where Good Models Can Die)"
slug: part-4-production-systems-where-good-models-can-die
publishedAt: "2026-02-17T13:51:03.000Z"
heroImage: /images/blog/part-4-production-systems-where-good-models-can-die/hero.jpeg
contentFormat: markdown
category: tech
summary: (4th Part of the 7Part series on what it takes to be a strong ML engineer in 2026)
sourceContentFormat: html
sourceRepo: senthilnathan01.github.io
sourcePath: data/md_articles/part-4-production-systems-where-good-models-can-die.md
sourceUrl: https://senthilnathan01.github.io/blog/part-4-production-systems-where-good-models-can-die
importedAt: "2026-07-26"
tags:
  - sources
  - blogs
  - tech
heroImageUrl: >-
  https://senthilnathan01.github.io/images/blog/part-4-production-systems-where-good-models-can-die/hero.jpeg
---

# Part 4: Production Systems (Where Good Models Can Die)

(4th Part of the 7-Part series on what it takes to be a strong ML engineer in 2026)

**The moment I realized I didn’t understand production ML:**

I had built a model. It worked beautifully on my laptop. 95% accuracy on my test set. Clean code. Fast inference.

Then I tried to deploy it.

Suddenly I needed to think about: data pipelines that don’t break, features that are actually available at inference time, monitoring that catches problems before users do, deployments that don’t take down the service, and a dozen other things that had nothing to do with model architecture.

That’s when it hit me: **Building the model is maybe 20% of the work. The other 80% is everything around it.**

Let me share what I’m learning about that other 80%.

### Data Pipelines: Where ML engineering actually happens

Here’s something nobody told me when I was learning ML from tutorials:

**Your model is only as good as the data flowing into it.**

Not the training data you carefully curated. The messy production data that arrives late, incomplete, or broken.

### Feature stores are Harder than they look

The promise: Store features once, use them for training and serving.

The reality:

- Online-offline consistency is brutally hard to maintain
- Training uses batch features computed with all the time in the world
- Serving needs low-latency features computed in real-time
- These are fundamentally different systems
- Keeping them consistent? That’s an entire challenge

### Point-in-time correctness:

- Training needs to see the world as it looked at prediction time
- Not as it looks now with all future information
- This is harder than it sounds
- Get it wrong = temporal leakage = useless model

**Real example I studied:**

- Model predicting customer churn
- Training used “customer’s total spend” as a feature
- But that feature included spend AFTER the prediction date
- Model learned: “customers who spend a lot don’t churn” (obviously)
- In production: feature only includes past spend
- Model performance: completely different

**Feature freshness:**

- Some features update every second
- Some update daily
- Some update never
- Your model expects fresh data
- What happens when the upstream pipeline breaks?

### What I’m building into my mental model:

**Late-arriving data:**

- Events arrive out of order
- Data processing has delays
- What you see at prediction time ≠ what you see an hour later
- How do you handle this?

**Schema evolution:**

- Upstream teams change their data schemas
- Your features depend on fields that disappear
- Or get renamed
- Or change types
- Without telling you

**Backfills:**

- Need to retrain with new features
- Must recompute features historically
- Without creating temporal leakage
- While keeping the production system running
- This is where most backfills fail

Your model degraded? Probably upstream data changed. Your training failed? Probably a schema migration broke your feature join. Your predictions are wrong? Probably you’re reading stale features.

**Fix the pipeline first. Then worry about the model.**

### Monitoring: If you’re not measuring it, it’s failing silently

Traditional software monitoring: Is the service up? What’s the latency? Any errors?

ML monitoring: All of that, plus a dozen model-specific things that can degrade silently while your service runs “normally.”

**What I’m learning to monitor:**

**Model-specific metrics:**

### Prediction distribution drift:

- Your model starts predicting class A way more often
- Or the distribution of predicted probabilities shifts
- This might be fine (world changed)
- Or catastrophic (model broke)
- You need to know which

### Feature distribution drift:

- Input features start looking different
- Means change, variances change
- New values appear that weren’t in training
- This breaks models in subtle ways

### Calibration degradation:

- Model says “90% confident”
- Actually right 60% of the time
- Your decision thresholds are now completely wrong

**Subgroup performance disparities:**

- Overall accuracy: 90% (great!)
- Accuracy on demographic group X: 60% (disaster)
- Without explicit subgroup monitoring, you’ll never catch this

**For LLM systems specifically:**

### Hallucination rates:

- What percentage of outputs contain ungrounded claims?
- Which types of queries trigger hallucinations?
- Is this rate increasing over time?

### Token consumption:

- Cost per request
- Token usage trends
- Unexpected spikes (someone’s abusing your system?)

### Retrieval quality (for RAG):

- Are you retrieving relevant documents?
- Hit rates on your vector database
- Latency of retrieval operations
- Quality of retrieved chunks

**Operational metrics that matter:**

### Per-layer latency breakdowns:

- Where is your model actually slow?
- Is it tokenization? Embedding? Generation?
- Can’t optimize what you don’t measure

### GPU utilization:

- Are you actually using your expensive GPUs?
- Waiting on data loading?
- Memory-bound or compute-bound?

### Queue depths and backpressure:

- How many requests are waiting?
- Are you falling behind?
- When do you start rejecting requests?

### The hard part: Turning metrics into actionable alerts

Bad alert: “Model accuracy dropped 2%”

- Could be noise
- Could be normal variation
- Probably gets ignored

Good alert: “Model accuracy dropped 15% on users from Region X in the last 6 hours, 99.9% confidence this is real”

- Specific
- Significant
- Localized
- Actionable

### Deployment: Not just pushing to production. Managing risk.

I used to think deployment was: git push, docker build, kubectl apply, done.

Then I learned about all the ways that approach causes production incidents.

**What I’m learning about safe deployment:**

### Model versioning that’s actually traceable:

- Not just “model_v2.pkl”
- Which training data?
- Which code version?
- Which hyperparameters?
- Which person approved it?
- Full lineage from data to deployed model

### Shadow deployments:

- New model runs alongside old model
- New model sees production traffic
- But doesn’t affect user experience
- Compare outputs, latency, error rates
- Catch problems before they impact users

### Canary releases:

- Deploy to 1% of traffic
- Monitor carefully
- Gradual rollout: 1% → 5% → 25% → 100%
- Automatic rollback if metrics degrade

### A/B testing frameworks:

- Not just “which model is better”
- But accounting for:

**Rollback procedures that work at 2am:**

- Not “submit a ticket and wait for approval”
- Not “manually revert the deployment”
- Automated: detect degradation → trigger rollback → notify on-call
- Practice this. Regularly.
- When production is on fire, muscle memory matters

**Real story I heard:**

- Team deployed new model Friday afternoon
- Metrics looked fine initially
- By Monday, customer complaints flooding in
- Took 4 hours to rollback (manual process)
- Lost customers, lost trust
- Now they have one-click rollback tested weekly

### Distributed Systems: ML is just distributed systems with gradients

Your ML system doesn’t exist in isolation. It’s part of a distributed system with all the classic distributed systems problems.

### Retry logic with exponential backoff:

- Request failed? Retry.
- Failed again? Wait longer, retry.
- Keep failing? Eventually give up.
- But: don’t retry on errors that will always fail
- And: be careful not to create retry storms

### Idempotency:

- Request gets processed twice (network glitch, retry, whatever)
- Does this create duplicate predictions?
- Duplicate charges?
- Duplicate database entries?
- Make your endpoints idempotent or suffer

### Partial failures:

- Feature store is down
- Fall back to cached features? Default values? Fail the request?
- Retrieval service is slow
- Wait? Timeout? Use stale cache?
- Model service crashed
- Route to backup? Queue and retry? Error immediately?

### Rate limiting and circuit breakers:

- Downstream service is struggling
- Don’t make it worse by hammering it with requests
- Back off. Give it time to recover.
- Circuit breaker: stop requests after N failures, wait, try again

These aren’t hypothetical problems. They happen in production. Regularly.

Your model might be perfect. But if your distributed systems fundamentals are weak, users will have a bad time anyway.

### What I’ve heard from other engineers:

**“We spent 3 months optimizing model accuracy. It failed in production because our feature pipeline had a 5-minute delay we didn’t account for.”**

**“Our model was great. Our deployment process was terrible. We took down production three times before we built proper canary releases.”**

**“We monitored overall metrics. Didn’t notice we were performing terribly on 10% of users until they complained.”**

**“Shadow mode saved us. New model looked good in offline eval. In shadow mode, we caught that it was 3x slower than the old model under real load.”**

**“We didn’t have automatic rollback. When the model failed at 2am, it took us 6 hours to manually revert. Never again.”**

The model is the easy part (relatively). The system around it: the pipelines, monitoring, deployment, failure handling, that’s where so much more engineering happens.

And that’s okay. That’s the job.

### Next: Part 5

The critical pieces everyone forgets: Observability that actually helps debug, agents and their failure modes, security (prompt injection is real), and why your documentation matters more than you think

## Sources

- [Original published article](https://senthilnathan01.github.io/blog/part-4-production-systems-where-good-models-can-die)
