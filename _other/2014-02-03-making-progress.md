---
layout:     post
title:      "Making Progress"
date:       2014-02-03 15:16:56
categories: linux
---
I have a problem. Actually two problems. One problem is that I have this feeling that I can't shake. A feeling that I'm not doing enough, or getting enough things done. The second problem is that I have this strange hesitation to post on my blog these days. The 2nd problem is related to twitter, I tend to post things there more frequently. Short thoughts, less friction. The first problem has a bit of a challenge to it. Most people by default tend to look at their own achievements in a less-than-flattering light. I think the main reason for this is we tend to "forget" things as we get further in time from them. For example, if you had a really great day at work, but then had 2 weeks that were really bad, you won't see the really great day as the accomplishment that it was: instead you are overwhelmed with the most recent events (which in this case were not so great). I've decided to tackle both these problems by blogging things that I do shortly after I do them. This way I'll get two birds with one stone; more frequent updates, and a record of the cool and fun things I've done recently. Now having said all that, here's what I did in Januaray: 

## Raspberry Pi - ZNC

Last year I got 2 raspberry pi computers. Very cool little machines, they are about the size of a credit card and are only $35. But... what should I do with them? An answer finally hit me in the form of IRC. IRC seems to be making a comeback, a lot of interesting/cool people tend to hang out on it. So not wanting to be late to the party, I decided I would hang out there too. The problem is I could be connecting to IRC from one of several different machine (work machines, home machines, phone, etc.). The solution is to use an "IRC bouncer" like znc to keep my connection. Znc acts as a single sign on point, I log into it, and it keeps my connections to the IRC network alive. It also logs the conversations so I can scroll back on different machines and never miss anything. The only catch is that znc needs to be connected to the internet all the time to maintain the connection. Not wanting to keep my power-hog home PC running all the time, the flyweight raspberry pi suddenly seemed like the ideal server. It is low power (it runs off of a micro usb connection), and runs linux. The perfect combo! So with a little research (several other people had the same idea) and a little bit of time I was able to quickly accomplish the following: 

  * Setup a Raspberry Pi so it is on the internet 24/7
  * Setup a dynamic dns program so I can get to the Pi (even if my home network gets a new IP address)
  * Setup znc and have it connect to the IRC networks of my choice
  * Set up SSL so that everything on the IRC side is encrypted

The last one is my favorite so far. With all of the security talk going on, a little more encryption is a great idea. I've got a few more network-aware apps that I'm thinking about putting on the Pi, but this is a great start. And the next time I do something I'll have it posted here! A win-win.
