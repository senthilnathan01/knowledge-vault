---
type: blog
status: published
visibility: private
title: Google Analytics Worked on Localhost but Failed on GitHub Pages. Here’s What I Learned.
slug: google-analytics-worked-on-localhost-but-failed-on-github-pages-heres-what-i-learned
publishedAt: "2026-03-18T14:59:05.000Z"
heroImage: >-
  /images/blog/google-analytics-worked-on-localhost-but-failed-on-github-pages-heres-what-i-learned/hero.jpeg
contentFormat: markdown
category: tech
summary: Google Analytics Worked on Localhost but Failed on GitHub Pages. Here’s What I Learned.
sourceContentFormat: html
sourceRepo: senthilnathan01.github.io
sourcePath: >-
  data/md_articles/google-analytics-worked-on-localhost-but-failed-on-github-pages-heres-what-i-learned.md
sourceUrl: >-
  https://senthilnathan01.github.io/blog/google-analytics-worked-on-localhost-but-failed-on-github-pages-heres-what-i-learned
importedAt: "2026-07-26"
tags:
  - sources
  - blogs
  - tech
heroImageUrl: >-
  https://senthilnathan01.github.io/images/blog/google-analytics-worked-on-localhost-but-failed-on-github-pages-heres-what-i-learned/hero.jpeg
---

# Google Analytics Worked on Localhost but Failed on GitHub Pages. Here’s What I Learned.

*A beginner-friendly debugging story about static sites, Next.js, Google Analytics, and why production can behave very differently from local development.*

![](https://senthilnathan01.github.io/images/blog/google-analytics-worked-on-localhost-but-failed-on-github-pages-heres-what-i-learned/hero.jpeg)

I think the problem was actually obvious.

But since I’m still quite new to web development, I had to go through the whole confusion → debugging → learning cycle. That’s also why I’m writing this.

So here’s what happened.

I was trying to add Google Analytics to my portfolio site. It’s built using Next.js and deployed on GitHub Pages.

On localhost, Google Analytics was detecting page visits. On the live .github.io site, it was silent.

At first, that made no sense. Same code, different results. It turns out that is completely possible, and understanding why is one of the more useful lessons you can pick up early.

This post walks through what happened, how I debugged it, and the broader engineering takeaway that I think applies well beyond Google Analytics.

### The Setup

My site is built with Next.js, exported as a static site, and deployed to GitHub Pages.

I wanted something simple: track visitors, see daily and weekly numbers, get a sense of overall traffic over time. Google Analytics 4 was the obvious pick. Free, widely used, and more than enough for a personal site.

So I created a GA4 property, got the measurement ID, and added the standard snippet. The plan was straightforward:

1. Load Google’s gtag.js
2. Initialize it with the measurement ID
3. Deploy the site
4. Watch traffic appear in GA Realtime

That is what should have happened.

### The Confusing Part

The first clue that something was off: localhost visits were showing up in Google Analytics, but GitHub Pages visits were not.

That made the problem genuinely puzzling.

If nothing worked at all, the suspects are obvious: wrong measurement ID, wrong GA property, missing script, bad environment variable. But because localhost was working, the GA account itself was clearly configured correctly. The problem lived somewhere between how the script was added, how the site was built, and how the static output behaved on GitHub Pages.

That narrowed things down quite a bit.

### The First Important Lesson

When debugging production issues, looking at source code and saying ‘this looks fine’ is only half the job. What actually matters is what the browser receives and executes.

That shift in thinking is one of the more useful things I picked up from this whole experience.

Modern frameworks like Next.js do a lot behind the scenes. They optimize scripts, move things around, hydrate pages, and generate different output for development versus production. Your React or Next.js code can look perfectly correct while the final generated HTML behaves differently than expected. On static hosting, that difference matters a lot.

### What I Checked First

The obvious things first:

- Correct GA measurement ID? Yes.
- Correct environment variable name? Yes.
- GitHub Actions workflow had access to the value? Yes.
- Code pushed to main and the production site rebuilt? Yes.

All fine. Still nothing in Realtime.

So I moved to browser-level checks.

### The Browser Checks That Helped

On the live site, I opened the browser console and ran:

```
typeof gtag
```

I expected 'function'. I got 'undefined'.

That was a very useful clue. It meant the Google Analytics function had never been properly initialized in the browser.

Then I checked whether the Google script loader was even present:

```
document.querySelector('script[src*="googletagmanager"]')?.src
```

That did exist.

So the picture became much clearer: the external Google script was loading, but the initialization step was failing silently. The loader was there; the initialized function was not.

### Why This Was Happening

The original setup used framework-managed script injection inside the Next.js layout. That looked reasonable in code, and it worked locally. But in the final static export, the initialization script was behaving unreliably on the live GitHub Pages deployment.

There was no error message explaining this. No warning about static hosting constraints. Just silence.

That silence is what makes production debugging feel mysterious, especially early on.

### The Fix

The reliable solution turned out to be simpler than expected: instead of relying on inline or framework-managed initialization, I switched to plain external scripts.

The final production setup:

1. Load Google’s analytics script
2. Load a small custom external script, ga-init.js
3. Initialize gtag from there

The browser now receives two normal script tags in the generated HTML:

```
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script><script defer src="/ga-init.js?id=G-XXXXXXXXXX"></script>
```

And the initializer file:

```
(function () {  var currentScript = document.currentScript;  if (!currentScript) {    return;  }  var scriptUrl = new URL(currentScript.src, window.location.href);  var measurementId = scriptUrl.searchParams.get('id');  if (!measurementId) {    return;  }  window.dataLayer = window.dataLayer || [];  function gtag() {    window.dataLayer.push(arguments);  }  window.gtag = gtag;  gtag('js', new Date());  gtag('config', measurementId);})();
```

After deploying that version, things started working correctly.

### Why the External Script Approach Helped

For a static site on a simple host like GitHub Pages, making important browser behavior plain and explicit tends to work better. Fewer framework-specific layers, fewer assumptions about runtime behavior, more standard browser script loading.

Framework abstractions are genuinely useful. But for functionality that is simple and critical, the most reliable version is often the one closest to basic HTML and JavaScript.

That was the case here.

### The Bigger Lesson: Localhost Is a Comfortable Lie

Just because something works on localhost does not mean it works in production.

That sounds obvious. But when you are actively building something, local success is easy to over-trust.

Local development and production can diverge for all kinds of reasons: build-time optimizations, static export behavior, script ordering, hydration differences, environment variables, caching, browser policies, and hosting platform constraints. Any one of these can produce a gap between what you see locally and what users actually get.

A good habit to build early: always verify the deployed version, not just the local version.

### The Debugging Process That Actually Helped

Here is a summary of the approach that worked:

**Confirm what is already working.** Localhost traffic appeared in GA, which told me the measurement ID and Analytics property were probably fine. That saved time by ruling out the wrong suspects early.

**Check the browser, not just the source code.** Running typeof gtag in the console told me initialization had failed. One line, immediate clarity.

**Separate script presence from script execution.** The Google loader script existed. The initialized function did not. A script tag being present in the DOM does not automatically mean the feature is working.

**Inspect the built output.** Instead of asking ‘does my Next.js code look correct,’ the better question is ‘what exactly is in the exported HTML?’ That question gets much closer to the actual problem.

**Prefer the simpler runtime path when debugging static sites.** When the abstraction is unclear, move closer to plain browser behavior. That is what solved this.

### What I Would Tell Someone Doing This for the First Time

If you are adding Google Analytics to a static site:

- Verify the correct measurement ID is being used
- Confirm the production build actually receives that value
- Check the live deployed HTML, not just your local files
- Use the browser console to confirm gtag really exists as a function
- If framework-managed script injection behaves strangely, simplify the setup

## Sources

- [Original published article](https://senthilnathan01.github.io/blog/google-analytics-worked-on-localhost-but-failed-on-github-pages-heres-what-i-learned)
