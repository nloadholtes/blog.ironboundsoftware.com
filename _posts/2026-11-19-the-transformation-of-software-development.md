---
title: "The transformation of software development"
date: 2026-11-19
tags:
  - "AI"
  - "software dev"
---

Compared to what I was doing 2 years ago, being a Software Developer has completely changed with the introduction of LLMs.

Today (November 2026) the code that the machine writes is typically very high quality. I have some quibbles about some things it does, but these are more along the lines of a "I wouldn't do it that way because of taste-or-style" type that I would normally have a conversation with a co-worker about. And the speed... we can deliver working code in minutes instead of weeks. Rapid iteration is finally here in a meaningful way everyone can use.

The biggest change seems to be with the suductress of speed: most developer's comfort levels with the accuraccy are met so they assume whatever it produces is correct. Then 3 or 4 Pull Requests in we discover the original agent was mis-informed about something and as a result the code have, while working, doesn't do what was originally wanted.

Which raises all kinds of new things to consider:
- What are we really trying to build?
- Who defined this? A human or the output of a previous LLM run?
- How do we verify that what was built is what we actually want?

That last one is the challenging one. I have noticed a lot of new-to-the-company or junior devs don't seem to have a test plan beyond the unit test that get generated along side the code in the PR. I've had to advocate several times for some kind of integration test that we can run to verify a feature has actually shipped (or if you prefer: that the feature actually works).

So in the space of 2 years I've become something of a manager, and less of a typist.

I find myself very concerned about "verification" of what we are building. And I've had to give up several aspriations that I had (really mastering functional programming, building in certain languages) because they just don't serve any future I want anymore. 

And that's probably one of the biggest internal shifts for me. In a short period of time I have become a Project Manager instead of a Project Builder. Sure I could invest the time and learn a new language, but what does that buy me? The returns I get from better planning and then guiding the machine seem to far outweigh the joy I got from building toy programs as I learned something new.

Its a strange new world. I like it, but I'm still adjusting to it.
