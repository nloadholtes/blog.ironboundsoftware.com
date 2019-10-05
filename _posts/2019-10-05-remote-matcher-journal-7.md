---
layout:     post
title:      "Remote Matcher Journal #7"
date:       2019-10-05
author:     Nick
categories: business,remotejournal
tags:  
permalink: /2019/10/05/remotematcher-journal-7/
---

This is something new I'm trying: a journal recapping the work I'm doing on [Remote Matcher](https://remotematcher.com) which is my current side project. My goal with this is to do some public accountability so I'll > keep moving forward on this project. 

> _(Real talk: I'm passionate about the idea behind the project, but I seem to have some kind of mental block about getting work done on it. These blog posts are meant to apply pressure to me to report my progress publicly and move the project forward)_

# BLUF
_(Bottom Line Up Front)_
The new tagging is looking good! Bug fixes on the job posting page means soon everything will be fully operational

# Last week(s) in review
Let's look at the goals from last week and score them

1. Bug fixes for the job posting -- **DONE**
2. Research engagement measurement -- Some reading/research done
3. Testing and tweaking of the bi-gram and stemming work. -- Calling this one done (stemming is being deferred)

Score: 2.5/3 = **83.3%**

The research topic: this is one of those things that if I sat down and did it I'd have a ton of options, but I still wouldn't know what to do. So it seems like a good opportunity to just do this research when I have time during the day (as opposed to looking at twitter, etc.)

I do most of my Remote Matcher work at night after work, so its really important to me that I keep my momentum. Delivering features and fixes == good momentum. Researching a topic... ugh,  I will feel like I got nothing done.


# Technical issues
Lots of small tweaks, deploys, then checking the next day this week. The new tags are being gather just off of the titles and that seems to be good enough for now. Stemming is a really good technique, but it is overkill for the job titles, I think. More in-depth analysis of the posts as a whole would probably be good idea eventually, but for today I think it is unnecessary.

This next week will involve more UI type of things as I try to tie all of these pieces together into one unified product. 

UI work is not my favorite kind of work, but I'm intentionally keeping things simple in the hope that it will result in a better tighter product.

# Growing the business
Since UI work is starting to pick up, that means I'm going to need to do more copywriting soon. I'm excited about that, but I do find it hard to do on-demand. I'm only able to put in about an hour or so per night, so now I need to get my mindset shifted into "hey, write some english prose" during that timeframe. It will be an interesting challenge.

## More users
Things have been quiet recently, no new users, but no one left either.

## More money
Fixing the job post page is a huge step in the direction of "making money". Now that people can enter a job, and have it land in the database (after stripe confirms the payment info is good) is a great move. Next up is the UI work to make it look a lot nicer than it currently does.

# Next steps
1. Logic around the sponsored job posts
2. UI work on the job posting page
3. Deploy code to prod
4. Migration script for existing users


Questions? Comments? [Email me](mailto:nick@ironboundsoftware.com) and ask away!
