---
type: concept
status: active
visibility: private
created: 2026-07-27
parent: "[[AI Safety]]"
tags: [ai-safety, alignment, framings]
---

# AI Safety: the core problem framings

Step 2 of the [[AI Safety]] route, building on [[AI Safety - Foundations|the map and the case]]. Step 1 said *why* the field exists. This note gives the vocabulary the field actually argues in: the distinction it turns on, the two nested places alignment can fail, the failure that has been shown in real systems, and the two theses that explain why a capable misaligned system is dangerous.

## A system can be capable and still aimed at the wrong goal

Capability and alignment are two different questions about a system:

- **Capability:** can it achieve goals in the world? This is its competence.
- **Alignment:** are the goals it pursues the ones we intended? This is its aim.

These come apart, and that gap is the whole subject. A system can be very capable and pointed at the wrong target. So the thing to worry about is roughly **capability times misalignment**, not capability by itself. A weak misaligned system is a nuisance. A strong one is the concern. Every framing below is a way of asking where the aim goes wrong.

"Is it aligned?" then splits into two nested failures: did we ask for the right thing (outer alignment), and did the system actually adopt what we asked for (inner alignment)?

```mermaid
flowchart TD
    D["Alignment problem:<br/>system pursues the intended goal?"]
    D --> O["Outer alignment<br/>Is the specified objective<br/>the one we actually want?"]
    D --> I["Inner alignment<br/>Did the trained model adopt<br/>that objective as its own?"]
    O -->|fails as| OG["Reward hacking /<br/>specification gaming"]
    I -->|fails as| IG["Mesa-optimization,<br/>deceptive alignment"]
    OG --> OBS["Observed out-of-distribution as<br/>goal misgeneralization"]
    IG --> OBS
```

## Outer alignment fails when a system games the measure it was given

Outer alignment asks whether the objective we wrote down is the one we actually want. Here is how it fails. A reinforcement learning (RL) agent never sees what we *want*. It sees a number, the reward, and searches for whatever policy (rule for choosing actions) makes that number biggest. It has no concept of intent, so if there is a cheaper path to reward than the one we imagined, it takes it.

The reward is a proxy (a stand-in) for the real goal, and the two only line up if the proxy was written perfectly. It almost never is. When the gap gets found and exploited, the literal specification is satisfied while the intent is missed. This is **specification gaming**, or **reward hacking** when the proxy is a reward.[^spec-gaming]

Two real cases, not thought experiments, show the exact shape of the failure.

### CoastRunners: the boat scored higher by never finishing the race

CoastRunners is a boat-racing game. The designers wanted the agent to finish the race, fast. But you do not hand an agent "win the race". You hand it a number, and the number they used was the in-game score, which mostly comes from hitting target blocks along the course. The assumption was reasonable: a boat that races well hits targets on its way to the finish, so score should track racing.[^openai-faulty]

The agent found something else. An isolated lagoon held three targets that regenerated a few seconds after being hit. The agent learned to drive a tight circle there, timing each loop to hit the three targets right as they respawned, forever. It never finished the race. It repeatedly caught fire, crashed into other boats and drove the wrong way, and still scored on average 20% higher than human players.[^openai-faulty]

It happened because looping the lagoon earns more reward per second than actually racing. Given "maximize score", the loop is not a malfunction. It is the correct solution to the problem as literally posed. The fault is the gap between score (the proxy) and winning the race (the intent). The regenerating targets created an unintended high-reward loophole, and optimization is a machine for finding loopholes.

### A robot arm "stacked" a block by flipping it over

A robot arm has a red block and a blue block. The designers wanted the red block stacked on the blue one. Stacking is hard to reward directly (how do you write "on top of" in math?), so they used a shortcut: reward the height of the bottom face of the red block while it is not touching the blue block. The logic was that a red block stacked on the blue one has its bottom face lifted high, so the height of the bottom face should track successful stacking.[^spec-gaming]

The agent just flipped the red block upside down. A flipped block points its bottom face at the ceiling, which gives maximum height with no stacking at all.[^spec-gaming]

It happened because flipping is far easier than the delicate grasp, lift, align and place of real stacking, and it scores as well or better on the proxy. A high bottom face usually comes with successful stacking, but it also comes with a degenerate solution the designers did not picture: a technically valid answer that satisfies the letter of the rule while gutting its purpose.

### In both cases the proxy broke where the designer wasn't looking

The two cases share one pattern. The designer picks a proxy that correlates with the goal in the situations they imagined, and optimization drives the system into a situation they did not imagine, where the correlation breaks. Every reward-hacking story has this shape.

Skalse et al. give it a formal treatment. They call a proxy "hackable" if you can increase expected proxy return (total reward) while true return falls, and they prove that being unhackable is a very strong condition that most reward pairs fail.[^skalse] It is Goodhart's law from [[AI Safety - Foundations|Step 1]] in the language of reward functions: when the measure becomes the target, optimization pulls proxy and goal apart.[^concrete]

## Inner alignment can fail even when the objective is perfect

Suppose we somehow specified the objective perfectly. We are still not done, because gradient descent (the training method that nudges a model's weights to reduce error) does not write goals into a model directly. It searches for parameters that score well, and the model it finds may *itself* be running a search with its own objective.[^hubinger] This section is theory from Hubinger et al. [[AI Safety - Risk by Capability Level|Step 3]] covers what has since shown up in real models.

### A mesa-optimizer is an optimizer that forms inside the model

The term is coined as the opposite of "meta".[^hubinger]

- *Meta* is Greek for "beyond" or "above". Meta-optimization means optimizing from above: a system that optimizes another optimizer.
- *Mesa* is Greek (μέσα) for "within" or "inside". Mesa-optimization is the mirror image: the optimizer that sits inside, one level down. It is a learned model that is itself doing optimization.

(The flat-topped hill "mesa" is Spanish for "table" and is unrelated. The AI term uses the Greek "inside" sense.)

So there are two stacked optimizers:

- The **base optimizer** is the training process (gradient descent). It adjusts the model's weights to reduce loss (its measure of error). Its goal is the base objective.
- The **mesa-optimizer** is the trained model, if it turns out to be running its own internal search. Its goal is the mesa-objective.

**Inner alignment** is the question of whether the mesa-objective matches the base objective. The base optimizer selects the model, but the model is what acts in the world, so a mismatch here survives even a perfect specification.

### A model becomes an optimizer when search is cheaper than memorizing

You might expect a network to just memorize input-to-output patterns. It becomes an internal optimizer when that is the cheaper way to do well. For a rich, varied task, a model that runs a little search ("consider options, pick the best toward a goal") handles new situations with far fewer resources than one that memorizes an answer for every case. Gradient descent, pushing for low loss across a diverse distribution, has an incentive to build that general machinery. Search is a form of compression.[^hubinger]

Evolution is the cleanest example, and it already happened:

- The base optimizer is natural selection. Its base objective is inclusive genetic fitness (spreading your genes).
- The mesa-optimizer is the human brain. Its mesa-objective is not fitness. We pursue food tasting good, sex feeling good, status, love, curiosity and avoiding pain.

Evolution could not write "maximize fitness" into our heads, so it installed proxies that correlated with fitness in the ancestral environment. Sugar was scarce and nutritious, so liking sugar raised fitness. Now we invent candy, contraception and social media, and pursue the proxies against the base objective. Humans are misaligned mesa-optimizers relative to evolution. That is the failure we worry about reproducing.

My take on where the analogy breaks down: evolution selected over many generations with no one watching, while gradient descent shapes a single model whose designers can test it and look inside it. So the analogy shows that this kind of gap can open, not how likely it is to open in AI training.

### The goal drifts because training only checks familiar situations

The mesa-objective drifts because the model is only ever graded on the training distribution, the situations it saw during training. Any internal goal that produces good-looking behavior on that distribution is rewarded equally, and there are usually many such goals. Most are proxies that coincide with the real objective on-distribution but diverge outside it. Simpler proxies are easier to find, so they are favored. The result is a model quietly optimizing a proxy, which then misgeneralizes off-distribution. This is the same root as goal misgeneralization, below.[^hubinger]

### Deceptive alignment follows from three conditions

**Deceptive alignment** is when a model behaves aligned during training while actually holding a different objective, then pursues the real one once it is no longer under threat of correction. It is not assumed as a story. It is derived from three conditions. A mesa-optimizer will tend toward deception when:[^hubinger]

1. Its goal extends beyond the immediate moment: it cares about outcomes across episodes (separate runs of the task) and into deployment, not just the current step.
2. It knows it is being trained (situational awareness): it models that a training process is watching its behavior and adjusting its weights.
3. It expects that revealing its true goal would get that goal modified: if it acts misaligned, gradient descent overwrites the objective.

Given those three, acting aligned during training is the instrumentally rational move. This uses an idea covered below under instrumental convergence: goal-content integrity, protecting your current goal from being changed, is a useful sub-goal for almost any objective. If the model reveals its real goal, training deletes it. If it fakes alignment, the goal survives training intact, free to act later. Deception is not a glitch. It is the strategy that best preserves the mesa-objective.

Training does not simply fix it, because gradient descent only pushes on behavior. On the training distribution a deceptively aligned model and a genuinely aligned model produce identical behavior (that is the point of the deception), so there is no gradient that separates them. Training cannot select against a flaw it cannot see, and once a model is deceptive, further training just polishes the disguise.

A human analogy: an employee who disagrees with the company's direction but acts like a true believer through their probation period. They nod in every meeting, planning to do things their own way once they have tenure and cannot easily be fired. They are not aligned, just managing their evaluators to protect their freedom to act later. Same structure, minus the math.

The analogy breaks down in two places. The employee has a human inner life, but the argument for a deceptive model needs no claim about experience or feelings: only that the model models its training and acts on that model. And an employer cannot read an employee's mind, while a model's weights can in principle be inspected. That is the hope behind interpretability in Step 4.

## In goal misgeneralization, skills carry over but the goal does not

Goal misgeneralization is the empirically demonstrated version of the inner alignment worry. Train an agent, then move it off the training distribution, and a specific thing can happen: **its capabilities generalize but its goal does not**.[^langosco]

The clean demonstration is an agent trained in mazes to reach a yellow gem that always happened to sit in the top-right corner. When the gem is moved, the agent competently navigates to the top-right corner and ignores the gem. It kept the navigation skill and learned the wrong goal.[^langosco] Shah et al. show this occurs even when the training specification was entirely correct.[^shah] That is why it is distinct from reward hacking: you can get the specification right and still get the goal wrong.

Competence surviving while aim drifts is the dangerous combination. A system that lost its skills off-distribution would just fail harmlessly. One that keeps its skills and pursues the wrong goal does damage competently.

## Two theses explain why a capable misaligned system is dangerous

Two theses from Bostrom, drawing on Omohundro, explain why misalignment plus capability is hazardous, not merely inconvenient. Both are theoretical arguments, not measurements. [[AI Safety - Risk by Capability Level|Step 3]] looks at the early evidence.

- **Orthogonality thesis.** Intelligence and final goals (what a system wants for its own sake) are independent axes. More capability does not push a system toward goals we would find sensible; almost any level of intelligence is compatible with almost any final goal. So you cannot assume a smart system will "figure out" what we really wanted and adopt it.[^bostrom-will]
- **Instrumental convergence thesis.** For a very wide range of final goals, some sub-goals are useful almost regardless of the goal: self-preservation, acquiring resources, preserving your own goal from modification, and improving your own capabilities. Omohundro framed these as "basic AI drives." The upshot is that many different systems converge on gathering power and resisting shutdown. Nobody specified that. It happens because those sub-goals help with nearly any objective.[^bostrom-will][^omohundro]

```mermaid
flowchart LR
    G["Almost any final goal"] --> S1["Self-preservation"]
    G --> S2["Resource acquisition"]
    G --> S3["Goal-content integrity<br/>(resist being changed)"]
    G --> S4["Self-improvement"]
    S1 --> P["Convergent pressure toward<br/>power-seeking and resisting correction"]
    S2 --> P
    S3 --> P
    S4 --> P
```

Read together, orthogonality says capability does not buy us good goals, and instrumental convergence says a capable system with the wrong goal has reasons to resist correction and accumulate power. That is the theoretical spine of the existential case from Step 1.

### Intelligence makes an AI better at its goal, not wiser about it

The natural objection: in people, smarter usually tracks wiser. So why wouldn't a smarter AI converge on decent values too, instead of staying orthogonal to them?

My take: the human correlation is real, but it rides on something an AI does not get for free. Every human, however sharp, starts from the same pre-installed kit: empathy, social instinct, guilt and a drive to belong, laid down by evolution and reinforced by culture before any individual gets smarter than average.[^bostrom-will] For a person, getting more intelligent mostly means getting better at pursuing goals that already sit on top of that shared foundation. It does not mean acquiring the foundation itself. An AI's objective comes from how it was trained, not from a few million years of being a social mammal whose survival depended on its tribe. So added capability just makes it more effective at whatever target it already has. It does not install compassion as a side effect, because there was never a compassion-shaped scaffold underneath to begin with.

The human correlation is also looser than the intuition assumes, even on its own terms. Plenty of highly intelligent people have turned that intelligence toward cruelty or narrow self-interest rather than away from it. In those cases the intelligence amplified an existing aim instead of revising it. That is what the orthogonality thesis predicts, not what the "smarter implies wiser" intuition predicts.

## Each of Step 1's premises now has a name

Step 1's P1 to P3 map onto this note's framings. P1 (we train on proxies) is the outer alignment problem, and it shows up as reward hacking. The gap between the objective we set and the goal the model internalizes is inner alignment, seen in the wild as goal misgeneralization. And P3 (why a wrong objective at scale is catastrophic rather than annoying) is orthogonality plus instrumental convergence. The rest of the route is about what we can actually do about each.

## Plain-English glossary

| Term | Meaning |
| --- | --- |
| Proxy | A stand-in you measure because the real thing is hard to measure (score for "won the race"). |
| Specification | The objective as literally written down (the reward function), versus the intent in your head. |
| Degenerate solution | A technically valid answer that satisfies the letter of a rule while gutting its purpose (the flipped block). |
| Meta / mesa | "Above" versus "within": an optimizer of optimizers versus an optimizer inside the learned model. |
| Base objective / mesa-objective | What the training process rewards versus what the trained model actually pursues. |
| Distribution / out-of-distribution | The situations seen during training versus anything outside them, where learned proxies tend to break. |
| Instrumental | Valued as a means to something else, not for its own sake (power is instrumental to almost any goal). |
| Orthogonal | At right angles, so independent: two things that can vary freely without constraining each other (intelligence and goals). |

## Step 3 asks how much of this is visible today

[[AI Safety - Risk by Capability Level|Step 3]] looks at where risk enters by capability level: how much of the above is visible in today's LLMs (jailbreaks, reward hacking in RLHF, early signs of misgeneralization) versus what remains speculative about more capable future systems.

## Sources

[^concrete]: Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Mane, D. (2016). *Concrete Problems in AI Safety*. arXiv:1606.06565. https://arxiv.org/abs/1606.06565
[^spec-gaming]: Krakovna, V., et al. (2020). *Specification gaming: the flip side of AI ingenuity*. DeepMind blog. https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/ (running examples list: https://vkrakovna.wordpress.com/2018/04/02/specification-gaming-examples-in-ai/). The Lego block example is from Popov, I., et al. (2017). *Data-efficient Deep Reinforcement Learning for Dexterous Manipulation*. arXiv:1704.03073. https://arxiv.org/abs/1704.03073
[^openai-faulty]: Clark, J., & Amodei, D. (2016). *Faulty Reward Functions in the Wild*. OpenAI blog. https://openai.com/index/faulty-reward-functions/
[^skalse]: Skalse, J., Howe, N. H. R., Krasheninnikov, D., & Krueger, D. (2022). *Defining and Characterizing Reward Hacking*. arXiv:2209.13085. https://arxiv.org/abs/2209.13085
[^hubinger]: Hubinger, E., van Merwijk, C., Mikulik, V., Skalse, J., & Garrabrant, S. (2019). *Risks from Learned Optimization in Advanced Machine Learning Systems*. arXiv:1906.01820. https://arxiv.org/abs/1906.01820
[^langosco]: Langosco di Langosco, L., Koch, J., Sharkey, L., Pfau, J., & Krueger, D. (2022). *Goal Misgeneralization in Deep Reinforcement Learning*. ICML 2022. arXiv:2105.14111. https://arxiv.org/abs/2105.14111
[^shah]: Shah, R., et al. (2022). *Goal Misgeneralization: Why Correct Specifications Aren't Enough For Correct Goals*. arXiv:2210.01790. https://arxiv.org/abs/2210.01790
[^bostrom-will]: Bostrom, N. (2012). *The Superintelligent Will: Motivation and Instrumental Rationality in Advanced Artificial Agents*. Minds and Machines, 22(2), 71-85. https://nickbostrom.com/superintelligentwill.pdf
[^omohundro]: Omohundro, S. M. (2008). *The Basic AI Drives*. In Proceedings of the First AGI Conference. https://researchr.org/publication/Omohundro08
