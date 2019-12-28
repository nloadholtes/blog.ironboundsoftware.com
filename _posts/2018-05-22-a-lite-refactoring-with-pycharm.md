---
layout:     post
title:      "A lite refactoring with PyCharm"
date:       2018-05-22 15:27:20
author:     nick
categories: python
tags:  
permalink: /2018/05/22/refactoring-with-pycharm/
---
Inspired by [@levels](http://twitter.com/levelsio) I decided to try adding a Telegram integration to my current project [RemoteMatcher](https://remotematcher.com). After seeing it work in production I decided to expand on the idea a little bit and do some refactoring with [PyCharm](https://www.jetbrains.com/pycharm/).

Let me show you how this all evolved and how easy it was to make this into a reusable bit of code.

> **TL;DR; Here's a[video](https://www.youtube.com/watch?v=EURikItXAgk) of me using PyCharm's refactoring tool**

## Just getting it working

The initial challenge was to get my app to send messages to a private Telegram chat. Telegram has a reputation for being easy to integrate with because of its HTTP based interface.

For me this was pretty ideal: All I want is to post a message once my daily task runs. Since we can talk to Telegram via HTTP, there wasn't really a need to use a full fledged library (and increase the dependencies for the project).

The hardest part of all this was getting the bot to post to the private room. Once I got that figured out, I was able to post things just using cURL. This is a good sign: It means we can use the regular `urllib` code from the Python stdlib.

Here's a rough outline of the steps I took to make this happen: * Create a telegram account for myself * Create a private chat * Create a bot account * Add the bot as an administrator for the private channel * Use cURL to confirm the bot can post things to the channel * Translate the cURL code in to Python

## Working first, then refactor

The part of my app I'm interested in runs only once a day, so after testing I needed to wait overnight to see if the results were what I was looking for.

Of course things weren't 100% the way I liked them the first time, so I did some small tweaks (mostly formatting of the text) for the next run. After 2 days I was pretty happy with results!

My objective for this task was complete. I could now check the status of last night's jobs without having to log into the GCloud logging interface.

Having this nice consoladated information delivered to my phone got me thinking, where else could I do this type of reporting? I quickly thought of 2 more places: new subscribers and unsubscribes!

But to do this... Did I really want to copy and past the same 6 lines over and over? Hell no!

### PyCharm to the rescue

When I worked in Java one of the things I really liked about the Java ecosystem was the strong support for refactoring tools. IntelliJ has great support for this essential Software Engineering task, and thankfully PyCharm inherited many of these capabilities.

I was able to use the "Extract Method" feature to pull out that code into a function, and with a quick modification to the parameters I made a very reusable function.

I also used the "Refactor->Move" feature to rearrange the code a little bit and put my new `send_to_telegram` function to the `util.py` module. This cleanup move resulted in a cleaner looking module that is more focused on one task. (SOLID anyone?)

## Showing, not just telling

The end result of all this?

![Showing the result of refactoring with pycharm: a nice status report in telegram](https://ironboundsoftware.com/blog-imgs/uploads/2018/05/IMG_20180518_081639-420x747.jpg)

The next morning I woke up to a telegram alert showing me that some people got emails with job leads last night!

It also gave me an alert that someone had unsubscribed after getting that email.

_standing-in-the-rain-crying.gif_

Although this was a pretty small refactoring in the grand scheme of things, it was great to see the PyCharm tools in action. Honestly, the hardest part of this whole thing was figuring out how to get the bot to post to the private channel. Everything else was really easy!

Here's a video I made of me doing this fun little task:

Here's a video of me using PyCharm to tackle this fun little task:

## Wrapping up

I hope you liked this little peak into making a quick-and-dirty telegram integration to improve reporting!

If you are looking for a remote programming job, check out my free aggregator: [Remote Matcher](https://remotematcher.com)
