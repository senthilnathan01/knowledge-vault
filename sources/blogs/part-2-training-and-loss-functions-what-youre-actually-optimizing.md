---
type: blog
status: published
visibility: private
title: "Part 2: Training and Loss Functions (What You’re Actually Optimizing)"
slug: part-2-training-and-loss-functions-what-youre-actually-optimizing
publishedAt: "2026-02-06T06:48:12.000Z"
heroImage: /images/blog/part-2-training-and-loss-functions-what-youre-actually-optimizing/hero.jpeg
contentFormat: markdown
category: tech
summary: (2nd Part of the 7Part series on what it takes to be a strong ML engineer in 2026)
sourceContentFormat: html
sourceRepo: senthilnathan01.github.io
sourcePath: data/md_articles/part-2-training-and-loss-functions-what-youre-actually-optimizing.md
sourceUrl: >-
  https://senthilnathan01.github.io/blog/part-2-training-and-loss-functions-what-youre-actually-optimizing
importedAt: "2026-07-26"
tags:
  - sources
  - blogs
  - tech
heroImageUrl: >-
  https://senthilnathan01.github.io/images/blog/part-2-training-and-loss-functions-what-youre-actually-optimizing/hero.jpeg
---

# Part 2: Training and Loss Functions (What You’re Actually Optimizing)

(2nd Part of the 7-Part series on what it takes to be a strong ML engineer in 2026)

![](https://senthilnathan01.github.io/images/blog/part-2-training-and-loss-functions-what-youre-actually-optimizing/hero.jpeg)

Your loss function isn’t just a number that needs to go down. It’s a precise mathematical statement about what you care about and your model will give you exactly what you asked for, even when you asked for the wrong thing.

### Your loss function is a contract with reality

Here’s the pattern I keep seeing in ML failure stories:

Someone builds a model. It trains beautifully. Loss goes down. Metrics look great. They deploy it.

Then it fails in production in completely predictable ways — if only they’d actually thought about what their loss function was telling the model to do.

Real examples I’ve studied:

### Cross-entropy on imbalanced data:

- You have 99 normal transactions, 1 fraudulent transaction
- You use standard cross-entropy loss
- You just told your model: “Being wrong on fraud costs the same as being wrong on normal transactions”
- Model learns: “Just predict ‘not fraud’ every time and get 99% accuracy”

### MSE on heavy-tailed distributions:

- You’re predicting user engagement (most videos get 100 views, some get 10M)
- You use Mean Squared Error
- MSE heavily penalizes being wrong on outliers
- Model learns: “Optimize for rare viral videos, ignore typical content”
- Your recommendations become completely skewed

### Standard classification on biased data:

- Training data has historical bias (fewer loans approved for certain demographics)
- You use cross-entropy to predict “good loan candidate”
- Model learns: “Replicate historical bias perfectly”
- You’ve now automated discrimination at scale
- And it’s mathematically optimal according to your loss function

### What I’m learning to ask:

Before picking a loss function:

- What behavior does this loss actually incentivize?
- How does class imbalance interact with this loss?
- What happens when my data has label noise?
- What are the implicit assumptions in this loss?
- How do those assumptions break in production?

### Training at scale is distributed systems engineering

I used to think training was: write model code, call .fit(), wait.

Then I tried to actually train something non-trivial and realized: oh no, this is way more complicated.

What I’m learning about real training:

### Distributed training isn’t optional at scale:

- Single GPU: limited by memory and speed
- Multiple GPUs: now you need data parallelism or model parallelism
- Data parallelism: split batches across GPUs, synchronize gradients
- Model parallelism: split the model itself across GPUs
- Pipeline parallelism: different GPUs handle different layers
- Each approach has different communication overhead

### Gradient accumulation:

- Want batch size 128 but only fit 32 in memory?
- Accumulate gradients over 4 micro-batches
- Same mathematical result, different memory profile
- But now you need to think about when to synchronize

### Checkpointing that doesn’t corrupt:

- Save model state periodically (obviously)
- But also: optimizer state, scheduler state, RNG state
- Handle failures mid-checkpoint
- Don’t fill disk with redundant checkpoints
- Make sure you can actually restore from them (test this!)

### Reproducibility is harder than it sounds:

- Random seeds aren’t enough
- GPU operations can be non-deterministic
- Distributed training introduces more randomness
- Data loading order matters
- Even with all this, perfect reproducibility might be impossible

### Fault tolerance:

- Your 72-hour training run will crash
- Can you resume from the last checkpoint?
- Do you lose hours of work or just minutes?
- Have you tested your recovery procedure?

### When to stop:

- Early stopping isn’t admitting defeat
- It’s recognizing diminishing returns
- That last 0.5% improvement cost you $5K in compute
- Was it worth it? (Usually no)

### Evaluation: Where theory meets reality (and usually loses)

Kaggle metrics ≠ Real-world metrics

On Kaggle:

- Fixed test set
- Same distribution as training
- Single number to optimize
- Winner takes all

In production:

- Distribution shifts constantly
- Multiple competing objectives
- Tradeoffs between accuracy, latency, cost
- Need to maintain quality over time

Offline evaluation ≠ Online performance

Offline metrics can be completely misleading:

- Great AUC offline, terrible precision at your operating threshold
- High accuracy overall, terrible on rare but important cases
- Perfect on your test set, useless on real user queries

Online metrics are what actually matter:

- Did users click more?
- Did they convert more?
- Did they come back?
- Did the system make money?

The gap between offline and online:

- Offline: 95% accuracy
- Online: 70% user satisfaction
- Why? Your test set didn’t capture real user behavior

What I’m learning to do:

Build regression test suites for models:

- Like unit tests for code, but for model behavior
- “Model should never predict class A when feature X > threshold”
- “Model should maintain >90% accuracy on this critical subgroup”
- “Model latency should stay under 300ms at p99”

Understand when metrics lie:

- Average accuracy hides subgroup failures
- Macro-averaging hides class imbalance
- Micro-averaging hides minority performance
- Overall metrics hide temporal degradation

Track what matters to users:

- Not just “did the model predict correctly”
- But “did this prediction help the user accomplish their goal”
- Sometimes a “wrong” prediction is more useful than a “correct” one

### What production ML engineers told me

“Your offline metrics will lie to you. Build systems that detect this quickly.”

“Most model failures are gradual, not catastrophic. You need monitoring that catches slow degradation.”

“The loss function is where you encode your actual business objective. Get this wrong and everything else is pointless.”

“Training once is easy. Training reproducibly, at scale, with fault tolerance — that’s the actual job.”

“Your test set is the most important dataset you have. If it’s wrong, all your metrics are meaningless.”

### Tomorrow: Part 3

LLMs and Modern ML — the new fundamentals that everyone’s talking about but few people actually understand deeply.

What I’m learning about tokenization, attention, context limits, and why RAG systems fail quietly.

What’s your biggest confusion about training ML models? What do you wish someone had explained better?

Drop your questions below. If I don’t know the answer, maybe someone else reading this does.

Following this series? Part 3 drops tomorrow.

And if you’ve spotted something I got wrong in this post — please tell me. I’d rather learn than be wrong quietly.

## Sources

- [Original published article](https://senthilnathan01.github.io/blog/part-2-training-and-loss-functions-what-youre-actually-optimizing)
