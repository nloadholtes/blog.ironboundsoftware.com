---
layout:     post
title:      "Slide Puzzle 1.0"
date:       2004-07-09 19:22:42
author:     Nick
categories: programming
tags:  
permalink: /2004/07/09/slide-puzzle-10/
---
I have reached a point where I have decided to release the slide puzzle I've been working on (off and on, but more off than on) for a while now. It's a curses (i.e. text based) program that allows to you have a board ranging in size from 1 to 81 squares. And it allows you to move the space using the arrow keys. I have not implemented the check for win feature yet, so you are on the honor system when it comes to figuring out if you have won. ;) This code uses the basics of the curses library to do the drawing of the board (and for the user input). As far as curses programs go, I think this is about as basic as it can get. There are no windows or pads, no fancy animations. I learned a lot while writing this program. Hopefully anyone looking for an example of curses programming in python will be able to look at this program as an example. In the next release of this program I will finish up the checking for a win. It isn't a hard thing to do, I've just been swamped lately. I haven't been able to spend much time writing/testing the program. But again, if someone is looking for an example of a sliding puzzle (or a NxN puzzle) program, this program might be useful. As always, this code is provided with no warranty. [Here is the code](http://www.geocities.com/nloadholtes/code/slidepuzzle.py.html), have fun with it. Also, here are some other [chunks](http://www.geocities.com/nloadholtes/code.html) of sometimes useful code.
