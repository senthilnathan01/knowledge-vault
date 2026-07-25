---
type: blog
status: published
visibility: private
title: Why Crypto Has Not Beaten Wall Street Yet (And Why That Question Might Be Wrong)
slug: why-crypto-has-not-beaten-wall-street-yet-and-why-that-question-might-be-wrong
publishedAt: "2026-03-26T08:54:14.000Z"
heroImage: >-
  /images/blog/why-crypto-has-not-beaten-wall-street-yet-and-why-that-question-might-be-wrong/hero.jpeg
contentFormat: markdown
category: tech
summary: Why Crypto Has Not Beaten Wall Street Yet (And Why That Question Might Be Wrong)
sourceContentFormat: html
sourceRepo: senthilnathan01.github.io
sourcePath: data/md_articles/why-crypto-has-not-beaten-wall-street-yet-and-why-that-question-might-be-wrong.md
sourceUrl: >-
  https://senthilnathan01.github.io/blog/why-crypto-has-not-beaten-wall-street-yet-and-why-that-question-might-be-wrong
importedAt: "2026-07-26"
tags:
  - sources
  - blogs
  - tech
heroImageUrl: >-
  https://senthilnathan01.github.io/images/blog/why-crypto-has-not-beaten-wall-street-yet-and-why-that-question-might-be-wrong/hero.jpeg
---

# Why Crypto Has Not Beaten Wall Street Yet (And Why That Question Might Be Wrong)

### The Hidden Tax on Every Crypto Trade

**TL;DR:** On public blockchains, your transaction sits in a visible waiting room before it goes through. Automated bots and block producers can read it, act on it, and leave you with a worse outcome before your trade ever confirms. Traditional finance has its own version of this problem, just wrapped in legal infrastructure. Researchers have identified two properties that would help fix the on-chain version, but each comes with real engineering costs. This piece covers all of it, plainly.

### Every Day, Traders Lose Money They Never See Leaving

On public blockchains, trades go through. Prices are just slightly worse than they should have been. The difference quietly moves to someone who saw the trade coming and acted first.

This problem has a name, a measurable dollar scale, and a set of proposed fixes that each come with their own costs. Understanding it means being honest about how blockchains actually work, and equally honest about the financial system people claim blockchains should replace.

### A Clarification Worth Making Early

There is no single way that all blockchains process transactions.

The problems described in this piece apply specifically to public-mempool blockchains. Ethereum is the most prominent example. Solana uses a fundamentally different architecture. Rather than a shared public waiting room, Solana forwards transactions directly to upcoming validators through a system called Gulf Stream. Different networks make very different architectural choices about how transactions move.

This distinction matters because a lot of criticism aimed at blockchain infrastructure applies to one specific design pattern, not to every network in existence.

### The Public Waiting Room

On public-mempool blockchains, sending a transaction works like this. Your transaction does not go straight into the next block. First, it enters a public waiting area called the mempool. It sits there, readable by anyone watching the network, until a block producer picks it up and includes it in the next block.

That block producer has meaningful power. They choose which transactions enter the block and in what order. They can prioritize transactions with higher fees, delay certain ones, or reorder them in ways that benefit themselves.

The practical guarantee most chains offer today is called eventual inclusion. Submit a valid transaction and it will probably land within a few seconds. For sending money to a friend, that is perfectly fine. For executing time-sensitive financial operations in a publicly readable environment, a few seconds of uncertainty is a structural problem.

### The Hidden Cost Has a Name

The name for what arises from this setup is MEV, short for Maximal Extractable Value.

Picture a sealed envelope. You write down exactly what you want to buy and what you are willing to pay. Before you hand it over, someone holds it up to a light, reads everything inside, places their own order first, and then passes yours along. Your transaction still goes through. You simply get a slightly worse price because of what they saw and acted on ahead of you.

On public-mempool blockchains, automated bots and block producers do exactly this at scale. They watch the mempool, identify trades that will move prices, and insert their own transactions ahead of those trades to capture the price movement. A related tactic called sandwiching places two transactions around a target trade, one before and one after, extracting value from both sides of the price move.

The scale of this is not trivial. Research tracking Ethereum found over 500 million dollars extracted before the network’s 2022 architectural upgrade, and over 500,000 ETH extracted since then. Estimates vary by chain, attack type, and measurement period, but the pattern is consistent. MEV is a structural feature of how public-mempool systems work, not an edge case.

### Traditional Finance Has the Same Problem, Dressed Differently

A common response to blockchain’s fairness problems is to point at traditional financial markets as the working model. That comparison deserves more scrutiny than it usually receives.

The New York Stock Exchange does not run a simple queue where the earliest order always wins. It uses a parity and priority model, where multiple factors determine execution order and some orders share execution at the same price level. The structure is considerably more complex than a clean, first-in-first-out line.

Beyond exchange mechanics, consider the co-location industry. High-frequency trading firms pay substantial fees to place their servers physically inside or adjacent to exchange data centers. The goal is microsecond execution advantages over everyone else. The SEC has described this as a low-latency arms race built around physical proximity and connectivity. Speed in traditional markets is infrastructure you purchase. Only firms with the resources to buy it compete at the top level.

Most relevant to everyday investors: the SEC found that more than 90 percent of marketable retail orders are routed to a small group of wholesale market makers rather than directly to an open exchange. When a retail investor places a trade on a consumer platform, a private firm sees and executes that order before it ever touches a public exchange. This practice is called Payment for Order Flow, and it is legal and widespread.

There is also a legal protection worth understanding precisely. FINRA Rule 5270 prohibits certain types of front-running based on material non-public market information. That rule exists because getting in front of another person’s order is structurally possible. The protection is regulatory and institutional. The underlying technical possibility is real.

Traditional finance has its own version of information asymmetry and ordering advantages. They are institutionalized, regulated to varying degrees, and available primarily to participants who can afford the infrastructure to access them. This does not make blockchain’s problems smaller. It makes the comparison more honest.

### What Crypto Built Instead of Copying an Order Book

Faced with its own latency limitations, parts of the crypto ecosystem did something worth noting. Rather than attempting to replicate a traditional order book on a public blockchain, they designed something structurally different. It is called the Automated Market Maker, or AMM.

Decentralized exchanges like Uniswap do not rely on buyers and sellers constantly posting and updating prices. Instead, they use liquidity pools governed by a simple mathematical relationship: x multiplied by y equals k. The two variables represent the amounts of two tokens sitting in a shared pool. The constant k never changes. When you trade, the formula automatically adjusts the price based on how much you are taking out relative to what is in the pool. No human market maker required. No order book that needs millisecond updates.

AMMs have their own trade-offs. Liquidity providers face a risk called impermanent loss when prices move sharply, and certain types of MEV can still target AMM trades. For highly liquid assets, traditional order book depth can offer tighter pricing. For long-tail tokens and open access to markets, AMMs unlocked trading that previously could not exist on-chain at all.

The relevant point here is that this was a deliberate architectural decision to work with the blockchain’s design rather than against it.

### Where the Infrastructure Actually Stands Today

A lot of blockchain criticism still uses Ethereum Layer 1 as its frame of reference. That picture is several years behind where development actually is.

Solana offers sub-second finality and bypasses the traditional mempool entirely. Application-specific blockchains are built from the ground up for particular financial use cases. dYdX runs a decentralized order book and matching engine that processes trades quickly and only settles final state to the chain. Its own documentation is transparent about the trade-offs that remain, including divergence between local node order books and the propagation constraints that require specific safeguards when cancelling orders.

Layer 2 networks built on top of Ethereum handle significant transaction volume at much lower fees. Ethereum itself still runs on 12-second slot times, which creates latency constraints for time-sensitive applications regardless of other improvements. The broader ecosystem has built well past that single bottleneck. The base layer constraint is still there.

None of this proves the fairness problems are solved. It shows they are being actively engineered around, with deployed, production systems as evidence.

### Two Properties Researchers Say Would Help

For the specific problem of building adversarially fair, low-latency financial applications on public-mempool chains, researchers have identified two properties that would directly help.

**Censorship resistance at the block level.** This is a guarantee that any valid transaction submitted to an honest node will be included in the very next possible block. No delays, no skipping, no discretion from the block producer. Think of it as a hard postal commitment: any letter dropped in before the cutoff ships today, with no exceptions. Most major blockchains do not currently offer this guarantee in a strong, enforceable form.

**Pre-trade privacy.** On public-mempool chains today, a transaction becomes readable the moment it is submitted. Pre-trade privacy would keep a transaction hidden until it is officially confirmed in a block, removing the information advantage that enables front-running.

It is worth being precise about what existing systems actually provide here. Flashbots Protect routes transactions through a private mempool so they never appear in the public waiting room. MEV-Share goes further: the MEV-Share node can selectively share transaction information with searchers and forward transaction bundles to block builders. That is a meaningful privacy improvement over a public mempool, and it is also meaningfully different from a model where only one party ever knows about a transaction before it confirms.

A more robust cryptographic approach is threshold encryption. In this model, a transaction is scrambled in a way that requires multiple independent parties to cooperate before it can be read. No single actor, including the block producer, can access it alone. This is active research territory.

The honest trade-off: these cryptographic processes are computationally heavy. Adding encryption, commitment, and decryption steps to every transaction introduces processing overhead that directly competes with the speed required to make these systems financially useful. That tension is not resolved yet.

These two properties address ordering power and transaction visibility for public-mempool chains. They do not address finality timing, liquidity depth, matching engine design, or the off-chain operational layers that financial infrastructure also depends on. Ethereum’s 12-second slot structure remains a constraint regardless of how well these two properties are eventually implemented.

### The Honest Picture

Public-mempool blockchains are genuinely difficult environments for time-sensitive financial applications. Transactions sit in a visible, readable waiting room. Block producers can see and reorder them. MEV extraction is large, structural, and ongoing.

Traditional finance carries its own version of these problems. More than 90 percent of retail orders go to a small group of wholesalers. Co-location infrastructure creates legally permissible speed advantages available only to firms that can pay for them. The protection against front-running is regulatory, not structural. The playing field is not flat in either system.

Crypto is also not one coherent machine. Solana, Ethereum, dYdX, and a Layer 2 rollup make fundamentally different architectural choices. Treating them as interchangeable obscures both the genuine progress and the genuine remaining gaps.

The most accurate version of where things stand: public-mempool chains remain poor environments for adversarial, low-latency financial execution. The gap is real. Closing it requires solving hard problems with real engineering costs. The work being done through AMMs, private order flow systems, application-specific chains, and cryptographic research is more structurally novel than a simple race to match what traditional finance already built.

Both systems have fairness problems. One of them is at least being designed in public.

### **Glossary**

**Mempool:** The public waiting room where transactions sit before being included in a block. Anyone watching the network can read what is in there.

**MEV (Maximal Extractable Value):** The profit that block producers and bots extract by reading pending transactions and manipulating the order in which they are processed.

**AMM (Automated Market Maker):** A type of decentralized exchange that uses a mathematical formula and shared token pools to set prices automatically, without needing a traditional order book.

**Censorship Resistance:** A property that guarantees a valid transaction will be included in the next block without a block producer being able to skip or delay it.

**Threshold Encryption:** A cryptographic method where a piece of data is scrambled and can only be unscrambled when multiple independent parties cooperate, so no single party can read it alone.

**Co-location:** The practice of placing trading firm servers physically close to exchange matching engines to gain microsecond speed advantages.

**Payment for Order Flow (PFOF):** A practice where retail trading platforms route customer orders to private wholesale market makers, who execute and profit from seeing those orders before they reach an open exchange.

*Have a question about anything covered here, or a point you think deserves more scrutiny? Leave it in the comments.*

## Sources

- [Original published article](https://senthilnathan01.github.io/blog/why-crypto-has-not-beaten-wall-street-yet-and-why-that-question-might-be-wrong)
