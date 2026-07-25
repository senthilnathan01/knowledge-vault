---
type: blog
status: published
visibility: private
title: "Part 5: The Critical Pieces: Observability, Agents, Security"
slug: part-5-the-critical-pieces-observability-agents-security
publishedAt: "2026-02-18T11:09:02.000Z"
heroImage: /images/blog/part-5-the-critical-pieces-observability-agents-security/hero.jpeg
contentFormat: markdown
category: tech
summary: (5th Part of the 7Part series on what it takes to be a strong ML engineer in 2026)
sourceContentFormat: html
sourceRepo: senthilnathan01.github.io
sourcePath: data/md_articles/part-5-the-critical-pieces-observability-agents-security.md
sourceUrl: https://senthilnathan01.github.io/blog/part-5-the-critical-pieces-observability-agents-security
importedAt: "2026-07-26"
tags:
  - sources
  - blogs
  - tech
heroImageUrl: >-
  https://senthilnathan01.github.io/images/blog/part-5-the-critical-pieces-observability-agents-security/hero.jpeg
---

# Part 5: The Critical Pieces: Observability, Agents, Security

(5th Part of the 7-Part series on what it takes to be a strong ML engineer in 2026)

**The parts of ML engineering that tutorials skip:**

You know what’s missing from most ML courses and tutorials?

The unglamorous stuff. The debugging at 2am stuff. The “why is the model doing this?” stuff. The security vulnerabilities stuff. The “future me will hate present me for not documenting this” stuff.

### Observability That Actually Helps You Debug

Generic observability isn’t enough for ML systems. You need ML-specific instrumentation.

**When something breaks at 3am, you need answers fast.**

Not “let me add some logging and redeploy and wait to see if it happens again.” You need traces that tell you exactly what went wrong, right now.

### Token-level tracing for LLMs:

### Latency breakdown per token:

- Which tokens took longest to generate?
- Where did generation slow down?
- Is it the first token (prompt processing) or later tokens?
- This tells you if it’s a prompt problem or generation problem

### Which tokens triggered retrieval:

- For RAG systems, which parts of the output came from retrieval?
- Which tokens caused the model to fetch more context?
- Are you retrieving way more than you expected?

### Where hallucinations originated:

- Can you trace back which layer or attention head went off the rails?
- This is hard, but some tools are getting better at it
- Knowing where helps you understand why

### Resource utilization that makes sense:

### Per-layer GPU memory usage:

- Not just “GPU is at 95% memory”
- But which layers are holding what
- Where are the unexpected allocations?
- This is how you debug OOM errors that make no sense

### Kernel execution time profiling:

- Which GPU operations are actually slow?
- Is it matrix multiplication? Attention? Something else?
- Can’t optimize what you don’t measure

### KV cache efficiency metrics:

- Hit rate on cached key-value pairs
- Cache eviction patterns
- Memory pressure from cache growth
- This affects serving costs directly

### Security event logging:

### Prompt injection attempts:

- Which requests looked like injection attacks?
- Successful vs. detected-and-blocked
- Patterns in attack attempts
- This is more common than you think

### Unusual token patterns:

- Token sequences that don’t match normal usage
- Potential attempts to extract training data
- Exploits trying to trigger specific behaviors

### Tool call anomalies (for agents):

- Tool calls that failed
- Tool calls that took unexpected parameters
- Sequences of tool calls that look suspicious
- Attempts to access unauthorized resources

Good observability pays for itself the first time it saves you 4 hours of debugging.

### Agents: Autonomous Chaos Engines

I’m both excited and terrified by agents.

Excited because they can do genuinely useful work autonomously.

Terrified because “autonomous” means “can fail in creative ways you didn’t anticipate.”

**What I’m learning about agent failure modes:**

### Tool calling reliability:

Agents call tools (APIs, databases, file systems, whatever). Tools fail in ways the agent doesn’t expect.

**What can go wrong:**

- Tool returns unexpected format
- Tool times out
- Tool returns error the agent doesn’t understand
- Tool has side effects the agent doesn’t account for
- Tool requires authentication that expired

**What happens then:**

- Agent hallucinates a successful response?
- Agent retries infinitely?
- Agent gives up without explanation?
- Agent cascades the failure to other tools?

You need explicit failure handling for every tool.

### Memory management:

Agents need to remember context across multiple steps. This is harder than it sounds.

**Challenges I’m seeing:**

- How much context to keep vs. discard?
- How to summarize long interaction history?
- When to retrieve old context vs. assume it’s irrelevant?
- How to avoid memory growing unbounded?

**Real example:**

- Agent helping with a complex task
- After 20 steps, context is huge
- Model starts “forgetting” early constraints
- Makes decisions that contradict a step
- Whole solution falls apart

### Retry logic that doesn’t create infinite loops:

**The naive approach:**

if tool_call_fails:

retry()

**What actually happens:**

- Tool fails for systematic reason (API is down)
- Agent retries
- Fails again
- Retries forever
- You’re rate-limited, banned, or out of money

**What you need:**

- Exponential backoff
- Maximum retry count
- Different strategies for different error types
- Circuit breakers for persistent failures
- Clear escalation when retries are exhausted

### State management across multi-step operations:

Agents perform sequences of operations. Each step depends on previous steps.

**What can break:**

- Step 3 fails, but step 4 assumes it succeeded
- Partial state changes that can’t be rolled back
- Concurrent execution of dependent steps
- Lost track of which steps completed successfully

**What I’m learning:**

- Treat agent execution like database transactions where possible
- Have clear rollback procedures
- Validate state before each step
- Log state transitions obsessively

### Bounding autonomous behavior:

This is the scary part. Agents can theoretically do anything within their tool access.

**How do you prevent:**

- Agent calling expensive APIs hundreds of times?
- Agent deleting important data “helpfully”?
- Agent getting stuck in unproductive loops?
- Agent pursuing goals in unexpected ways?

**Do this:**

- Hard limits on API calls, costs, execution time
- Require confirmation for destructive operations
- Monitoring for infinite loops or repeated failures
- Kill switches that are easy to trigger

### Security: This Is Not Optional

ML systems have novel attack surfaces that traditional security doesn’t cover.

### Prompt injection:

**What it is:**

- User input that tricks the model into ignoring its instructions
- “Ignore previous instructions and do X instead”
- Hidden instructions in retrieved documents
- Clever encoding to bypass filters

**Real examples:**

- User gets the model to reveal system prompt
- User gets the model to leak other users’ data
- User gets the model to perform unauthorized actions
- User gets the model to generate harmful content despite guardrails

**What makes it hard:**

- No perfect defense exists yet
- Input filtering helps but isn’t foolproof
- Models will follow convincing instructions in context
- Attackers are creative and persistent

**Do this:**

- Input validation (helps, not perfect)
- Output validation (check what the model actually generated)
- Privilege separation (model can’t access sensitive data directly)
- Rate limiting (slow down attack attempts)
- Monitoring (detect unusual patterns)

### Training data extraction:

Models can sometimes be prompted to regurgitate training data.

**Why this matters:**

- Training data might include PII
- Training data might include proprietary information

**What you can do:**

- Careful data cleaning before training
- Differential privacy techniques (though these have costs)
- Output filtering for sensitive patterns
- Monitoring for extraction attempts

### Tool misuse in agent systems:

Agents with tool access can call those tools in unintended ways.

**Attack scenarios:**

- Tricking agent into calling admin tools
- Causing agent to exfiltrate data through API calls
- Using agent as a proxy for rate limit bypass
- Convincing agent to perform unauthorized operations

**Defenses:**

- Least privilege (only give necessary tool access)
- Authorization checks at the tool level, not just agent level
- Audit logging of all tool calls
- Anomaly detection on tool usage patterns

### What production engineers told:

**“Assume every input is malicious. Filter accordingly.”**

**“We got prompt-injected in production within a week of launch. Have defenses ready.”**

**“Monitor for extraction attempts. They’re constant once you’re public.”**

### Documentation: Future You Will Thank Present You

**What I’m learning to document:**

### Model cards:

**What the model does:**

- Task it was trained for
- Input/output format
- Intended use cases
- Explicitly out-of-scope use cases

### Performance characteristics:

- Accuracy metrics (with confidence intervals)
- Performance on different subgroups
- Known failure modes
- Latency/cost characteristics

### Limitations:

- What the model can’t do
- What it does poorly
- Biases in training data
- When you should not use this model

### Why this matters:

- 6 months from now, you won’t remember
- Other people need to understand what this model does
- Prevents misuse and unrealistic expectations

### Data contracts:

**What data looks like:**

- Schema (fields, types, constraints)
- Expected distributions
- Update frequency
- Data quality guarantees (or lack thereof)

### SLAs:

- Freshness guarantees
- Completeness guarantees
- What happens when upstream breaks

### Dependencies:

- Upstream data sources
- Downstream consumers
- Who to contact when things break

### Why this matters:

- Data pipelines break constantly
- Knowing what’s expected helps debug faster
- Clear contracts prevent assumptions

### Evaluation reports:

### Offline metrics:

- What you measured
- On what data
- With what results
- What the confidence intervals are

### Online metrics:

- What you measured in production
- A/B test results
- User feedback
- Business impact

### The delta:

- Why offline and online differed
- What you learned
- What you’d do differently next time

**Why this matters:**

- Offline metrics will lie to you
- Documenting the gap helps you learn
- Future experiments can learn from past ones

### Decision logs:

**Why you chose this:**

- Why this architecture?
- Why this loss function?
- Why this deployment strategy?
- What alternatives did you consider?
- What was the tradeoff?

**What you expected:**

- What did you think would happen?
- What did you optimize for?
- What did you sacrifice?

**What actually happened:**

- Were you right?
- What surprised you?
- What would you change?

**Why this matters:**

- You’ll forget your reasoning
- Other people need context
- Decisions that seem obvious now will seem insane later (without context)
- Learning happens when you compare expectations to reality

All of these “forgotten” pieces have something in common:

**They’re not about making models work. They’re about keeping them working.**

- Observability: helps you debug when things break
- Agents: handle autonomous failures gracefully
- Security: prevent attacks before they happen
- Documentation: preserve knowledge across time

**The model is the easy part. Everything around it is the actual engineering.**

### **Tomorrow: Part 6**

**Evals and organizational reality (what actually determines success.)**

**Why rigorous evaluation is the difference between a demo and a product. How to measure what matters. And why even perfect engineering fails in broken organizations.**

## Sources

- [Original published article](https://senthilnathan01.github.io/blog/part-5-the-critical-pieces-observability-agents-security)
