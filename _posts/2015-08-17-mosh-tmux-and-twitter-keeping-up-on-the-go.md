---
layout:     post
title:      "Mosh, tmux, and twitter: Keeping up on the go"
date:       2015-08-17 05:35:48
author:     nick
categories: organization,productivity,thinking,web
tags:  
permalink: /2015/08/17/mosh-tmux-and-twitter-keeping-up-on-the-go/
---
I'm a big fan of twitter and I wanted to share some tips to help everyone get the most out of it. Here's some of the hacks I'm doing that make using twitter faster and more effective for me. Here's the  **TL;DR** version for the impatient: 

  * Use a text based client
  * Run the client on a remote machine (or [IN THE CLOUD](https://m.do.co/c/76f9b19dc762))
  * Use tmux to get the most out of your session
  * Use mosh to have a seamless connection
  * Use twitter lists to get a laser focus on important topics/people

( _[Follow me on twitter for more stuff like this! @nloadholtes](https://twitter.com/nloadholtes)_ ) 

## Text is where its at

With only 140 chars (and occasionally some pictures), twitter is all about text. So, why not use twitter in a place where text is king: the command line! There are several command-line twitter clients out there. I've been using [rainbowstream](https://github.com/DTVD/rainbowstream) for a few months, and recently started trying out [krill](https://github.com/p-e-w/krill). They each have their pluses and minuses, so I encourage everyone to try them both out and see which one appeals to you more. Rainbowstream is nice to look at because of its adjustable themes. But... I've noticed it tends to "hangup" on the stream and I have to re-switch back to my stream to ensure it updates. Krill is relatively new to me, so far it seems really stable, but doesn't look as nice as rainbowstream. Krill also has the ability to follow RSS and other formats which sounds awesome. Currently I'm running both side-by-side in a split tmux panel. More on that in a minute! 

## Run the client on another machine

Every time you close your laptop, you lose your network connection. Wouldn't it be cool if you didn't lose your place in the stream? Tweets will come in while you are away, but scrolling backwards will be time consuming. So, run the command line clients on another machine! Cloud based machines are dirt cheap these days, and they are a snap to set up. If you have one running already, adding these clients takes up almost no resources. Or... if you are like me and you have a RaspberryPI laying around... you can use that! I set mine up at home and configured my router to route incoming requests to it so I can easily access it no matter where I go. Its always on (thank you battery backups!), so it keeps track of the conversations going on while I'm asleep/commuting/out-and-about. Using ssh keeps it secure and an snap to log into. [caption id="attachment_453" align="aligncenter" width="584"][![The big guy keeps an eye on it for me](/blog-imgs/uploads/2015/08/20608765435_32023eb3db_k-1024x615.jpg)](/blog-imgs/uploads/2015/08/20608765435_32023eb3db_k.jpg) The big guy keeps an eye on it for me[/caption] And since the command line clients are so lightweight, I can run lots of stuff (like an IRC bouncer/client, a bitcoin miner, etc.) on it with no problem. Right now you're probably saying "But hey, you still need to log into that machine every time you open you laptop!" Well... 

## Use mosh to connect, and tmux to manage!

While I can use ssh to connect to the machine, if the network connection goes down I have to re-login which can be a pain, especially if you happen to be on a very flaky internet connection (like at the coffee shop or at my office). That why you should use [mosh](https://mosh.mit.edu/). Mobile SSH Shell is a very cool project that uses SSH over UDP/IP. Since UDP is designed to work on unreliable networks, this is the perfect solution. When mosh (on your computer) notices the network connection goes down, it will try and contact the remote host. When the network comes back, it will automatically reconnect, and update the terminal. The end result is that you can drop in and out without really knowing it, yet you never miss anything! I mentioned earlier that I was also running an IRC bouncer/client. How I'm going that is with [tmux](https://tmux.github.io/) which is a "Terminal Multiplexer". It basically allows one ssh/mosh connection to have multiple terminal windows. tmux is awesome and if you get nothing else from this article you should go learn and use tmux. (If you are familiar with "screen", tmux is a much much much better alternative. If you've never heard of screen... excellent.) So, how I'm using this whole set up is this way: 

  * mosh into my RaspberryPI
  * start up a tmux session
  * make one pane for twitter, another for IRC
  * Never look back. :)

From that point on, until one of the machines reboots, my computer will automagically reconnect (via mosh) and show me what's happening on twitter or IRC. AWESOMENESS! This is what my setup looks like: [caption id="attachment_452" align="aligncenter" width="300"][![A screenshot of my twitter tmux setup](/blog-imgs/uploads/2015/08/Screen-Shot-2015-08-14-at-9.38.47-AM-300x201.png)](/blog-imgs/uploads/2015/08/Screen-Shot-2015-08-14-at-9.38.47-AM.png) A screenshot of my twitter tmux setup[/caption] 

## Use the lists!

A while ago twitter rolled out a feature called lists. Lists are just ways to subscribe to users but not have them in your normal timeline. The beauty of this is you can now create lists centered on a topic, and fill it with relevant accounts. For example, I have a list called "funny" that has some accounts that spew out jokes and other humorous quips. I also made a list called 5 which is a very focused list of people who I think are doing important and inspiring things, and these are people I should pay attention to. (The name of the list is from the Jim Rohn quote "You are the average of the 5 people you spend the most time with".) I then use the command line clients to watch these lists. Since the lists are focused, the are not as "active" as the normal timeline. This way I can cut back on the distractions and time suck that the normal twitter timeline can become. On a normal day I check in on the 5 list a couple of times, and occasionally check funny, or one of my other lists. The beauty is now I've trained myself that it isn't necessary to check twitter constantly because a) it won't "update" as frequently, and b) when it does, I'm more likely to like the content. 

## Wrapping up

Use a lists to get focused on a topic that is important to you, use a command line client to keep it fast & clean, and host it somewhere other than your machine using mosh and tmux for extra awesomeness. Here are the links to everything: 

  * mosh <https://mosh.mit.edu/>
  * rainbowstream <https://github.com/DTVD/rainbowstream>
  * krill<https://github.com/p-e-w/krill>
  * My 5 list <https://twitter.com/nloadholtes/lists/5>
  * tmux <https://tmux.github.io/>
  * Me on twitter: <https://twitter.com/nloadholtes>


