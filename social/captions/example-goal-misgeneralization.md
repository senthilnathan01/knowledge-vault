# Field Note 02 — Goal misgeneralization (maze / gem)

**Card:** `social/cards/example-goal-misgeneralization.html` (render 1080×1350)
**Source note:** `concepts/AI Safety - Problem Framings.md`
**Sources:** Langosco et al. (2022), *Goal Misgeneralization in Deep RL*; Shah et al. (2022)

---

## X caption

Here's a result that should worry you more than it does.

Researchers trained an agent to move through a maze and collect a gem. Simple task. During training the gem always sat in the same spot, the top-right corner, and the agent got good at it. Fast, reliable, found the gem every time.

Then they moved the gem.

The agent ignored it. It ran straight to the top-right corner, the empty one, and stopped. It had never really learned "go to the gem." It learned "go to the corner," because during training those were the same thing.

This is goal misgeneralization, and what makes it matter is the split it exposes. Two things can generalize on their own: what the agent can do, and what it's trying to do. Here the skills transferred perfectly. The agent still navigated like a champ. The goal didn't transfer at all.

That combination is the dangerous one. An agent that lost its skills off its training data would just fail, and you'd notice. An agent that keeps its skills and quietly aims at the wrong thing keeps looking competent while doing the wrong thing.

And this isn't a sloppy reward. Langosco, and later Shah, showed you can reward exactly the right behavior in training and still get an agent that learned the wrong goal, because the training data didn't pin down which goal it was. "Reach the gem" and "reach the corner" fit that data equally well. Nothing told them apart.

We tend to assume a capable system roughly wants what we trained it to want. This is a clean counterexample.

Note 2 of a series where I take one idea from my AI safety notes and make it concrete.
