---
layout: post
author: Nick
title: AdditPulse mid-moretem
date: 2024-10-27
categories: experiments,thinking
tags:
  - building
summary: A point in time review of my current project
---

So I've got a project I've built and I'm in the process of trying to get people to use it. I've decided this is a good point to do a what I'm calling a "mid-mortem".

A "post-mortem" is done after something is over (or is dead), and a "pre-mortem" is an exercise to figure out what could go wrong and kill a project.

Since I've already started the project, the former is premature, and latter is too late. So a "mid-mortem" it is.

## The subject: Addit Pulse
A few months ago I saw a random tweet asking for what I thought was a great idea: a place to see who is advertising on a subreddit:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">is there any tool that shows who&#39;s advertising on Reddit? like FB ads library. <br><br>I want a list of every advertiser targeting a subreddit</p>&mdash; stetson 🤠 (@stetsblake) <a href="https://twitter.com/stetsblake/status/1779902015960678813?ref_src=twsrc%5Etfw">April 15, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

This seemed like a fun idea to build out, and something that would be really useful. In other words, a business idea I could make money with!

So I did some building, and launched a few ~~weeks~~ months ago. But I haven't made any money off of it. In fact, I'm not really seeing any interest in it at the moment.

[AdditPulse](https://additpulse.com) might be a failed project. Or is it too soon to tell?

I have more marketing work I can and should do to answer that question. But in the meantime I think it would be great to look at what I've done so far, and write down what I think went well and what I should have done differently.

## The good
Overall, there's a lot of good stuff to report here. No real regrets.
- Using [claude](https://claude.ai/) to write a lot of the code - I decided to really lean on AI to see if it could help me get from 0 to 1 on the code: Getting bogged down in minutia has stopped me in the past. Claude blasted me through that and I was able to keep momentum. 
- Keeping the tech stack simple - I stuck with what I knew (python, jinja) and only used new things that were small enough for me to reason about them (sqlite3, bootstrap, jquery). Claude was a huge help with this, especially on the font-end stuff where I am typically very weak.
- Shipping Fast* - I was able to ship small features _really_ quickly compared to my past efforts. The * is because I didn't ship the whole site as quickly as I should have (more on that below)
- Keeping the feature set small - I was working hard to stay focused on the "important" things first. I still have features I can add, but getting small things out first and fast feels good and feels like a win.
- Setting up [coolify](https://coolify.io/) - The mantra for a while has been to not waste time on setting up infrastructure. Overall I agree with that, but coolify was a game changer for me: it is the best parts of k8s without the headaches. Using it allowed me to deploy my changes faster and manage things on my terms. And it kept my sever bill cheap: 1 hetzner ARM node has been all I've needed. You can run your own infra, and it doesn't have to consume all your time and money.
 
## The bad/should-have-done-differently
Looking back now, I see some things that probably should have been approached differently.
* While I did get Stetson (who wrote the original tweet) to try it out, I didn't really get anyone else looking at it early on. More "validation" or at least finding my target audience would have been a thing to do earlier in the process.
* Too simple? My mastermind group were concerned I was keeping the UI too simple and it should have had more style. This is one I wrestled with a little bit: They are not wrong, but there is no clear line on how much time and money is too much in the beginning. I think as I learn more I'll develop a better sense of "taste" on these things and probably produce a nicer first draft.
* Related to the last point, I "launched" without a working buy button or analytics. IF someone tried to buy and couldn't I have no idea. Both of those should have been day 1 features.
* I sat on the site for about a month before finally launching. No excuses here, should have just gotten it out there sooner.
* I have no customers. So no one is looking at the site. I've been tweeting about it a little bit, but finding the community where people are discussing the problems I'm solving has been a challenge. I should have found the community first, then built.

## What's next?
I'm going to continue trying to find my users. There's still lots of ground I can cover on this one I think, so I shouldn't give up... yet.

I do think I should set an internal deadline for myself though so I don't squander my time chasing after something that isn't there.

I believe that withing a month I should know if this is going to work or not. And by that time I can just put this on the back burner since it doesn't cost much money to operate at this level. So it will just slowly wither on the vine.

Using the infrastructure and code I made for this project I am confident I'm in a strong position to start my next project: A lot of the boilerplate is there waiting to be reused, so I can pick it up and run with it and start focusing on the things I should do better the next time around:

1. Find customers first.
2. Build what they need/will pay for.
