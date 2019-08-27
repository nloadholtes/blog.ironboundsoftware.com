---
layout:     post
title:      "Markov Decision Processes and the iPod shuffle"
date:       2007-07-04 16:57:07
author:     admin
categories: ipod
tags:  
permalink: /2007/07/04/markov-decision-processes-and-the-ipod-shuffle/
---
I just finished reading [Peter Norvig](http://norvig.com)'s article about the "[Martin Shuffle](http://norvig.com/ipod.html)". (By the way, if you are a computer programmer, you need to visit Mr. Norvig's site. It is chock full of good programming/lisp/algorithm stuff.) The Martin Shuffle is basically a search for a specific song by using the random shuffle feature of an iPod. Now I know what you are thinking, but its not a crazy thing to do. In a situation where you can't see the display or access the controls (for example with an iPod [Shuffle](http://www.apple.com/ipodshuffle/), or when I have my iPod mini hooked up to my car stereo and I have to control it with the CD changer controls which only allow skipping and turning the shuffle on or off) this "random searching" is actually a pretty good strategy. Basically you randomly skip through songs until you get to the artist you are looking for. Once finding the artist, turn off the shuffle part and search one song at a time until you find the one you are looking for! Pretty straightforward and a fun way, well ok, a way to pass the time while sitting in traffic. Norvig's article talks about the math behind this type of search. Specifically he solves how long it would take to find a song (on average). He describes the problem as a [Markov Decision Process](http://en.wikipedia.org/wiki/Markov_decision_process) that can be solved using a value iteration algorithm. Its amazing how something that sounds so complicated is actually pretty straightforward. The code that is used to implement the solution is in [python](http://python.org) and it is pretty short so it is doubly impressive, at least to me.
