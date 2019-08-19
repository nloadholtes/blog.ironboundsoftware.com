---
layout:     post
title:      "Curses and Windows under Python"
date:       2004-06-16 20:51:10
categories: python
---
    
[Remember](http://www.pycs.net/users/0000316/2004/6/7) how I was talking about how easy it was to use curses and Python? Well there is one little catch: Its easy as long as you don't try to run it under windows.   
  
    
Python has no native support for curses under windows. There are [a few packages](http://flangy.com/dev/python/curses/) to try and bridge this gap, but they are not complete (and by that I mean as complete as the unix Python curses package). This little revelation was a surprise for me when I tried to run my [sliding puzzle](http://www.pycs.net/users/0000316/2004/5/25) on a windows box yesterday. While the Flangy.com package looks good, it doesn't support the curses.ascii module. :(   
  
    
Oh well, I guess the program will have to be unix only. At least until I get the gumption to go and do a GUI version of it.  

