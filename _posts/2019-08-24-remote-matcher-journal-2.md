---
layout:     post
title:      "Remote Matcher Journal #2"
date:       2019-08-24 10:46:37
author:     nick
categories: business,remotematcher
tags:  
permalink: /2019/08/24/remote-matcher-journal-2/
---
> This is something new I'm trying: a journal recapping the work I'm doing on [Remote Matcher](https://remotematcher.com) which is my current side project. My goal with this is to do some public accountability so I'll keep moving forward on this project. _(Real talk: I'm passionate about the idea behind the project, but I seem to have some kind of mental block about getting work done on it. These blog posts are meant to apply pressure to me to report my progress publicly and move the project forward)_

# BLUF

_(Bottom Line Up Front)_ Low progress week. New code was written, but not for the week's objectives. I need to focus on the plan, not on what it is fun/easy. A success of **37.5%** for the week. 

# Last week in review

Let's look at last week's goals and score them 

  1. ~~New production deployment (now that staging has been validated)~~ DONE
  2. Address HTML scrubbing bug (not user-facing, but it is a blocker for #3) -- Not done a. This is going to require a light refactoring of some of the parsing code in order to isolate the trouble spots b. MOAR tests will be added.
  3. Phase 1 of tagging improvements (tag extraction from untagged data) -- Not Done
  4. Create OKR's for this project. -- Partially done

Score: 1.5/4 = **37.5%** Deploying code is easy, so that almost shouldn't count. This week I was busy with life, but I still managed to find time to do some development... But not on anything that was on the schedule. Instead I refactored a Clojure script I wrote to post Tweets to get new users. :facepalm: On the positive side, this did have some good effects... more on that below. I did do some thinking on the OKR's for this project. I didn't write anything down though and that is a major part of having OKR's. I'm not beating myself up too much over this though, setting OKR's is hard thing to start. It is an ongoing process, but I feel strongly I should get something big/high-level in place soon. 

# Technical issues

Legacy code issues aside, my major concern at the moment is consistency and quality of the job leads that are being sent out. 

## Consistency

In the past I had an issue where the same job should have gone to multiple people. (e.g. a job tagged "Python" went to 3 people when it should have gone to 5 people.) That seems to be cleared up and the latest release seems to be really good. In this area I believe the best step forward is to improve the tests. Why? The system seems to be functioning correctly and tests will help ensure that things don't change in that area. 

## Quality

Making sure people get the jobs that they are interested in is my metric for quality. To achieve this, I need to make sure I'm correctly interpreting both the jobs and the requests from the users (e.g. what "tags" they are interested in). Doing this involves some more logic than I have in place currently. This will be the focus of most of my development efforts going forward. I also need to start measuring what the people think of the leads I'm sending them. A count of clicks on jobs and email opens is a nice superficial way of doing this. But I am thinking that if I put in a simple question in the emails like "How are these leads?" with a thumbs-up/thumbs-down link, I could get an even better answer. That's not a small development task, so I need to do some research on what it would take to get good measurements from that type of effort. 

# Growing the business

For growth, I'm defining two aspects: Bringing in more users and more money. 

## More users

Twitter is now the main driver of new signups. The work I did on refactoring the Clojure script to post to twitter paid off almost immediately: 3 new signup in 3 days after restarting the script. Granted, this is the most minimal effort thing I could be doing. But the thing is... it seems to be effective. Seeing new people come in gives me more data on what people are looking for in a new job. I need to spend some time on creating new tweets, this would be a good exercise in copy writing. For the moment, I'm ok with the level of users coming into the system. I've got some things I can do to press on the accelerator, so its good to know I've got options. Especially if I need to make a splash after shipping some new feature. 

## More money

I've got a high level plan on this. I also have a belief about somethings that should happen first. I need to spend some time and map both of those out and see if they are true. (Pro-tip: I'm probably wrong about what should happen first) 

# Next steps

Here's the plan for the next week: 

  1. Address HTML scrubbing bug (not user-facing, but it is a blocker for #3) a. This is going to require a light refactoring of some of the parsing code in order to isolate the trouble spots b. MOAR tests will be added.
  2. Phase 1 of tagging improvements (tag extraction from untagged data)
  3. Continue ~~Create~~ thinking about OKR's for this project.

Questions? Comments? [Email me](mailto:nick@ironboundsoftware.com) and ask away!
