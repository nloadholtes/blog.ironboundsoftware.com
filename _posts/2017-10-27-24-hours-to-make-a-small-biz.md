---
layout:     post
title:      "24 hours to make a small biz"
date:       2017-10-27 09:36:23
categories: entrepreneur
tags:  
permalink: /2017/10/27/24-hours-make-small-biz/
---
The other day at work I saw something on twitter and I said to myself “Hey, I bet I could build something like that, I’ve got all the parts just laying around...” As I was thinking that I realized I have some time off available to me so on a whim I decided to take a day off and hack on the idea and make it come to life! A hack day!  This post is my work diary. Throughout the day I took a break to record my progress and thoughts through the process. Hopefully this will inspire someone else out there to take some action and make something new in the world! 

# The Plan

I have a database of quotes and few API projects to access it. I’ve been toying with it for years, it seems like I should be able to make something out of it. I have also noticed lately that a lot of social sites like Facebook are just teeming with a lot of negative energy. What if... I could make a service that a person could subscribe to and have positive or inspiring quotes posted to their feed throughout the day? 

## Some high level details

I didn’t want to do too much work ahead of the hack day, but here’s the major points of what I’m trying to do: 

  * An API to access the quotes
  * A DB to hold customer sign up info (how often to post, expiration of trial, API tokens, etc.)
  * A Sales page to get people to sign-in 
    * A short (7 day) free period
    * Probably contact a few friends to get them to beta test it for me (to work out kinks and get some testimonials)
  * Something to look at the signups and do the actual posting

Seems easy enough, let’s do it! 

# The work diary

A few days before I decided that for the sales page I’d just use gitlab.com’s pages feature. I already had a Wordpress hosted domain, but for “reasons” I’ve decided to overhaul it and move to something more static. Using Jekyll is pretty easy, so I setup a repository and all of the things necessary to have gitlab serve up the pages. I also took that time to look at some themes. I found one that I liked so I went ahead and checked it into the repo. At this point I have the exported posts from the WP site, and a new theme. 

## 8am

First things first, I used this page <https://kristofclaes.github.io/2016/06/19/running-jekyll-locally-with-docker/> to get Jekyll to run in a container so I could test out my changes “locally” without having to commit/push every time I need to adjust a pixel. I put locally in quotes because I’m doing a lot of that dev on a cloud machine! For a lot of reasons I find it better to have things in the cloud, so this is where I’m doing that particular work. Next steps: Refactoring some of the old API code to test out a new idea, and then banging out some copy for the sales page. 

## 10:45am

The refactoring was interesting. My gut instinct was to completely gut the working code and replace it with something nicer. I did one [pomodoro](https://en.wikipedia.org/wiki/Pomodoro_Technique) of exploring and quickly realized that if I did that I would spend half the day re-writing it and now (other than me) would know about it. I took another pomodoro and cleaned up the existing code (mainly removing some ancient “features” that didn’t work and kept me from using it like I wanted to). Now I have a functioning core backend. Its minimal, but it will get the job done. Next stop: getting the new code in place that will auth with Facebook and post a quote for a user. I have some existing code that kinda does this, so I think in a pomodoro or two I should have something useful. 

## 11:15am

Ran into my first big hurdle: I need to figure out how to get a user’s permissions to post something to their wall. And store that. I’ve got code that does this, but I’ve always done it with short term tokens and copy-and-pasting things in. Time to educate and take a lunch break. 

## 1:52pm

Took a long lunch and spent some time with my son. Family > everything else. But back at it now. The break was good, it let me think about the architectural mistake I was about to make. [caption id="attachment_1255" align="aligncenter" width="675"]![](https://ironboundsoftware.com/blog/wp-content/uploads/2017/10/Screen-Shot-2017-10-26-at-11.26.09-AM.png) Here's where the wheels started to come off the train![/caption] 

## 4:42pm

Life took over for a few hours and I’m just now trying to squeeze in a few mins of work. The Facebook code to get someone to give my app permission is the main goal right now. Getting an app registered with Facebook was a pain, I had to stop everything to make a logo. That was infuriating. It is important, but not to me getting this up and running. At least to me. [caption id="attachment_1257" align="alignright" width="420"]![](https://ironboundsoftware.com/blog/wp-content/uploads/2017/10/HeroicInspiration-banner-420x315.png) What a logo looks like when you are in a hurry[/caption] At any rate, things are moving along again. It looks like I’ll be working later than I expected tonight. 

## 5:23pm

Got something to appear on Facebook! Now to figure out the tokens and then string everything together. This is coming together later than I wanted it too, so now I’m concerned that I might not be able to get people to help test this right away. I didn’t want to put the call out for volunteers too early because that would add pressure to me, plus probably bore people who couldn’t play with the new thing right away. Waiting was the right call, but ugh. Probably not going to get a lot of buzz tonight. 

## 7:44pm

More family time spent, but I’m back at it. I’m surprised how much time I spent with the kids today, it really impacted this project. If I didn’t have to stop and research so many things (like the Facebook token dance) I think I would have gotten more done faster. Lesson learned for next time. At the moment: swapping tokens, storing them, and making sure the permissions are correct. After that: updating the sales site so we can start signing people up. 

## 8:47pm

I have discovered that for the app to work the way I envision I’ll need to get a review of my app done. It is asking for things I don’t have yet, so that isn’t going to happen. One of the main goals tonight was to get this thing working with Facebook, so that is a big red X on that item. I have other things I can do with the project, so in the next hour or so I’m going to tackle them. Overall this is a setback, but now with the work I’ve done I see the big picture. I’m calling it a day at this point. 

## Lessons learned

Well, it didn’t turn out like I wanted it to. If it did I would have a functioning SaaS that would be posting to Facebook. But that’s ok, a lot of work was done and lot was learned. Let’s review! 

### The good:

  * The “refactoring” of the API Quote server was kept to a bare minimum. It would have been easy to spend the whole day there, but I kept it down to about an hour and wound up with a functional site.
  * The planning I did in the days before this hack day were great! When I got flustered or distracted all I had to do was look at the plan (done in Trello) and it was super easy to get back on track.
  * Related, I worked hard this week to think positive about this whole adventure. When this morning finally hit, I was so excited to get started! In a way I think this validated the underlying thesis that we need more positivity in our lives.
  * Learned lots! Jekyll looks awesome for static sites, lots of great themes out there and it is pretty easy to work with.
  * Was very on task! Early in the day I was using my Pomodoro timer that is pretty noisy. I really like it, but it is totally inappropriate for the office. Its ticking helped me stay focused. I had very little distraction in the first half of my day. Check out my rescuetime report below. Most of that Social Networking was me floundering around in Facebook trying to get this to work.

![](https://ironboundsoftware.com/blog/wp-content/uploads/2017/10/Screen-Shot-2017-10-26-at-9.05.38-PM.png)

### The not-so-great:

  * While my planning was good, as I get further along it was clear I could have done a little bit more. If the project was split into 3 parts, the first part was very well planned, the 2nd not so much, and the 3rd was pretty vague. If I had planned this out a little bit better it would have helped shorten some of those moments where I was struggling on “what to do” when things went wrong.
  * Distractions. My family is very important to me, and I did want to spend time with them on this day off. It is hard to do that and do an all day hack challenge. Next time its going to have to be one or the other.



### The bad:

  * I was trying to follow the mighty example of [@levelsio](https://twitter.com/levelsio) and only look up stuff when I needed it. This overall sounds good, but I ran into some issues requiring research (like the Facebook stuff) and that absolutely ground me to halt. Once I lost the momentum it was hard to get it back.
  * Might have thrown in the towel too early. As I write this I’m thinking of some other tasks I can go and tackle. Its after 9pm and that combined with the setbacks of the day have really got me thinking I’m more tired than I might be.



# Wrapping up

My hack day didn’t end like I wanted it to, but overall I’m happy with how it went. I’m going to take the lessons learned and roll them forward into the next hack day... which will probably be next week. :) Thanks for reading this far! You rock. 

Keep up with what I'm up to
