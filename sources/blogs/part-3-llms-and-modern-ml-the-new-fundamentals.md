---
type: blog
status: published
visibility: private
title: "Part 3: LLMs and Modern ML (The New Fundamentals)"
slug: part-3-llms-and-modern-ml-the-new-fundamentals
publishedAt: "2026-02-12T07:19:24.000Z"
heroImage: /images/blog/part-3-llms-and-modern-ml-the-new-fundamentals/hero.jpeg
contentFormat: markdown
category: tech
summary: (3rd Part of the 7Part series on what it takes to be a strong ML engineer in 2026)
sourceContentFormat: html
sourceRepo: senthilnathan01.github.io
sourcePath: data/md_articles/part-3-llms-and-modern-ml-the-new-fundamentals.md
sourceUrl: https://senthilnathan01.github.io/blog/part-3-llms-and-modern-ml-the-new-fundamentals
importedAt: "2026-07-26"
tags:
  - sources
  - blogs
  - tech
heroImageUrl: >-
  https://senthilnathan01.github.io/images/blog/part-3-llms-and-modern-ml-the-new-fundamentals/hero.jpeg
---

# Part 3: LLMs and Modern ML (The New Fundamentals)

(3rd Part of the 7-Part series on what it takes to be a strong ML engineer in 2026)

I thought I understood LLMs.

I mean, I could explain transformers. I knew about attention mechanisms. I had read the “Attention Is All You Need” paper (okay, skimmed it).

Then I tried to actually build something with LLMs in production.

Turns out, there’s a big gap between “I can use an API” and “I understand how this actually works and why it fails.”

Let me share what I’m learning as I try to cross that gap.

### Tokenization: Where many problems begin (and nobody notices)

I’m embarrassed to admit how long I ignored tokenization. It seemed like implementation detail — just the thing that converts text to numbers so the model can process it.

Wrong. Tokenization is where a lot of subtle problems originate.

**What I’m learning about tokenizers:**

### They fragment your domain-specific language in unpredictable ways:

- Medical terms get split into meaningless pieces
- Code identifiers break in weird places
- Non-English text gets brutally over-tokenized
- Numbers can be one token or many, depending on formatting

**Real example I tested:**

- “cardiovascular” → might be 1 token or 3 tokens depending on the tokenizer
- “2023” → 1 token
- “2,023” → 3 tokens (the comma breaks it)
- “COVID-19” → 2–4 tokens

**Why this matters:**

### Token counts determine your costs:

- Paying per token, not per word
- That innocent comma just increased your costs by 3x for that number
- Formatting choices affect your monthly bill

### Token limits are hard walls:

- 8K context means 8K tokens, not 8K words
- Your carefully crafted prompt might get truncated mid-sentence
- That JSON structure you’re asking for? Might not fit

### Tokenization creates biases:

- English: ~1 token per word
- Chinese: ~2–3 tokens per character
- Some African languages: even worse
- Same semantic content, very different token costs

### What I wish I’d known earlier:

- Always check how your domain-specific text tokenizes
- Test your prompts at different lengths — they might break at token boundaries
- Budget for tokens, not characters
- Different tokenizers behave very differently (GPT vs. Claude vs. Llama)

### Attention and Context: The fundamental constraints

The thing about transformer attention that I didn’t fully appreciate: it’s not just a clever mechanism. It’s a fundamental constraint on what these models can do.

**What “context window” actually means:**

### It’s not just “how much text fits”:

- It’s how much the model can “pay attention to” simultaneously
- Everything in that window competes for the model’s focus
- More context doesn’t always mean better performance
- The model can “forget” things at the start of a long context

### Attention is O(n²):

- Double your context length = 4x the compute
- This is why long context is expensive
- This is why there are hard limits on context size
- This is why clever chunking strategies matter

### The “lost in the middle” problem:

- Models pay more attention to the start and end of context
- Information in the middle can get lost
- This breaks naive RAG implementations
- Putting your most important info in the middle is a recipe for failure

### KV Cache: The thing that determines your serving costs:

I didn’t understand KV cache until recently. Now I realize it’s critical for production LLM systems.

**What it is:**

- During generation, the model caches key-value pairs from attention
- Reuses them for each new token instead of recomputing
- This is what makes generation feasible at all

**Why it matters:**

- KV cache size grows with context length
- It’s often the memory bottleneck in serving
- Longer contexts = more cache = more memory = fewer concurrent requests
- This is why context length and batch size trade off

**What I’m learning:**

- Monitor KV cache hit rates in production
- Understand the memory cost of long contexts
- Design prompts with cache efficiency in mind
- Consider whether you really need that full context

### Fine-tuning vs. LoRA vs. RAG:

### Fine-tuning: When you need to change behavior fundamentally

Use when:

- You need the model to learn domain-specific patterns
- You have enough quality data (thousands of examples minimum)
- You can afford the compute and storage
- You need consistent behavior across all requests

Don’t use when:

- Your knowledge changes frequently
- You don’t have enough training data
- You can’t afford full model copies
- You just need to inject some facts

### LoRA (Low-Rank Adaptation): Efficient adaptation

Use when:

- You want good amount of fine-tuning benefits but cheaper
- You need multiple adapted versions of the same base model
- You want faster training
- Storage/memory is constrained

Don’t use when:

- You need to completely change model behavior
- You’re just adding retrievable facts
- Your task is already handled well by the base model

### RAG (Retrieval-Augmented Generation): Dynamic knowledge

Use when:

- Your knowledge updates frequently
- You need to cite sources
- You want explainability
- Your knowledge base is too large for context

Don’t use when:

- You need the model to internalize patterns, not just retrieve facts
- Your retrieval quality is poor
- Latency is critical
- Your knowledge is small enough to fit in context

**The answer: Often you combine them**

- Fine-tune for domain behavior
- Use LoRA for task-specific adaptations
- Add RAG for dynamic, updateable facts

### RAG: The failure points nobody talks about in tutorials:

**Chunking destroys semantic coherence:**

- Split at 512 tokens? You just broke an explanation in half
- Split at paragraphs? Some paragraphs are 2 words, some are 200
- Split at sentences? Complex documents have sentence dependencies
- No perfect answer. Every strategy has tradeoffs

**Embeddings don’t capture your domain’s notion of relevance:**

- General-purpose embeddings optimize for general similarity
- Your domain has specific notions of “relevant”
- “Similar words” ≠ “relevant for this query”
- You might need domain-specific embedding models

**Retrieval finds plausible-sounding but wrong information:**

- High semantic similarity ≠ correct answer
- Model retrieves confident-sounding wrong information
- Generates plausible answers from irrelevant context

**Reranking helps but isn’t magic:**

- Cross-encoders are slow
- Faster rerankers are less accurate
- Reranking still depends on retrieval quality
- Garbage in, garbage out. Better ranked garbage is still garbage

**Grounding doesn’t actually ground:**

- Just because you retrieved relevant docs doesn’t mean the model used them
- Models can ignore retrieved context and hallucinate anyway
- Citation systems can cite irrelevant sources confidently
- Validating that retrieval helped is surprisingly hard

**What I’m learning to do:**

**Test retrieval independently:**

- Is your retrieval finding the right documents?
- Measure this separately from generation quality
- Track precision and recall of retrieval
- Use retrieval-specific metrics (MRR, nDCG)

**Validate that retrieval actually helps:**

- Compare with vs. without retrieval
- Check if the model is actually using retrieved context
- Measure hallucination rates with and without RAG
- Don’t assume retrieval is helping. Measure it. If you can’t measure it, you can’t manage it.

**Monitor in production:**

- Track which queries fail to retrieve relevant docs
- Monitor retrieval latency
- Watch for drift in retrieval quality
- Detect when your knowledge base becomes stale

### Hallucinations: Not bugs, features of the architecture

This is the hardest thing for me to accept: hallucinations aren’t bugs to fix with better prompting.

They’re fundamental to how autoregressive language models work.

**Why models hallucinate:**

**They’re trained to always produce plausible text:**

- Rewarded for fluent, confident output
- No inherent mechanism for uncertainty
- Will confidently make things up rather than refuse

**They don’t have internal fact databases:**

- Knowledge is distributed across parameters
- No clean separation of “known facts” vs “uncertain guesses”
- Can’t check their own knowledge reliably
- Memorization and confabulation look similar

**They are context-limited:**

- Can’t always retrieve relevant training information
- Might have seen correct info but can’t access it
- Will fill in gaps with plausible-sounding guesses

**What this means for production:**

**You can’t eliminate hallucinations:**

- Better prompting helps but isn’t sufficient
- RAG helps but isn’t perfect
- Fine-tuning can reduce but not eliminate
- You need system-level solutions, not just prompt engineering

**Design for hallucinations:**

- Add verification steps
- Use retrieval with source citation
- Implement confidence thresholds
- Build human review for critical outputs
- Fail gracefully when uncertain

**Measure hallucination rates:**

- Don’t just assume your system is accurate
- Test with known ground truth
- Monitor hallucinations in production
- Track which types of queries cause hallucinations

### What I have heard from production engineers

“Test your system at the token limit. That’s where things break.”

“RAG quality is 80% retrieval, 20% generation. Fix retrieval first.”

“Every LLM has different tokenization. Budget separately for each.”

“Hallucinations will happen. Your system needs to handle them gracefully.”

“Context length and serving costs trade off directly. Design accordingly.”

### Tomorrow: Part 4 (Production systems — where models can die)

What I’m learning about data pipelines, monitoring, deployment, and why most “model problems” are actually infrastructure problems.

And as always, if you spotted something I misunderstood, please correct me. I’m here to learn, not to be right.

## Sources

- [Original published article](https://senthilnathan01.github.io/blog/part-3-llms-and-modern-ml-the-new-fundamentals)
