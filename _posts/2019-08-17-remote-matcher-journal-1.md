---
layout:     post
title:      "Remote Matcher journal #1"
date:       2019-08-17 11:14:59
author:     admin
categories: business
tags:  
permalink: /2019/08/17/remote-matcher-journal-1/
---
This is something new I'm trying: a journal recapping the work I'm doing on [Remote Matcher](https://remotematcher.com) which is my current side project. My goal with this is to do some public accountability so I'll keep moving forward on this project. _(Real talk: I'm passionate about the idea behind the project, but I seem to have some kind of mental block about getting work done on it. These blog posts are meant to apply pressure to me to report my progress publicly and move the project forward)_ Over the next couple of updates I'll include a section on the "who/what/why" of this project. This update is all about just noting where the project is. 

# BLUF

_(Bottom Line Up Front)_ After a hiatus of many months, I have restarted work on Remote Matcher. The current focus is on reducing technical debt and growing this into a real side business. 

# Technical debt issues

The project is built on the foundation of a previous project. As a result, there is a lot of "dead" code that is been dragged around. Last weekend I started addressing this by adding in tests for known critical paths, refactoring obvious pain points (Python pro-tip: don't execute code at the module level, it makes huge pains when the module is imported), and deleting things that were clearly not being used. The end result: the code coverage jumped to almost 70% and more importantly it covers some critical areas. Deploying this code in a test project over the week has confirmed everything seems to be working correctly. 

## Lessons learned

  1. Running the project in a parallel system (Where I'm the only subscriber) is a great idea. In the morning I can compare the emails the two systems generated and quickly tell if something isn't quite right.
  2. It is amazing how quickly adding tests revealed some problems in the code base. Some problems were "quick" to fix, such as the import issue, others will need to be done in the future (before more features are added in those areas).



# Growing the business

I had an unusual thought this week after seeing 2 or 3 people unsubscribe: If this site is doing its job people will be unsubscribing. (The goal is to help developers get their ideal remote job so there's no need to stay subscribed after that happens!) I might need to add some kind of metric to track how long someone was subscribed to judge if their time in the system was good or not. There's already an exit interview (which has a very low conversion rate), so adding a new metric will be useful at some point. 

## Adding users

I turned off the [Twitter account](https://twitter.com/remotematcher) this week. It needs some work to improve its quality and I just don't have the bandwidth at the moment to mess with it. I am going to address this in two weeks. Until I get the tech debt paid down and 1 new major feature (more on that in a future update) shipped I'm not going to spend a lot of time on user acquisition. 

## Making money

The point of a business is to make money. I have parts and pieces of this but they all need to be put together and polished. Shipping this is a priority for September. 

# Next steps

  1. New production deployment (now that staging has been validated)
  2. Address HTML scrubbing bug (not user-facing, but it is a blocker for #3) a. This is going to require a light refactoring of some of the parsing code in order to isolate the trouble spots b. MOAR tests will be added.
  3. Phase 1 of tagging improvements (tag extraction from untagged data)
  4. Create OKR's for this project.

For #4: I've been reading [Measure What Matters](https://amzn.to/2HcGsVu) and implementing OKR's at the day job. It seems like a really great way to get a project moving, and I'm anxious to see if it can improve my efficiency.
