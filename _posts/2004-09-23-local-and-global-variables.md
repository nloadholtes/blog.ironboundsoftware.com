---
layout:     post
title:      "Local and Global variables"
date:       2004-09-23 07:03:37
author:     Nick
categories: programming
tags:  
permalink: /2004/09/23/local-and-global-variables/
---
    
Honestly, I really do like the ability of being able to declare a variable and run with it right there on the spot. Python is really great about that. But what I don't like is when I want to access a member variable of a class and I have to put "self." in front of the variable name to ensure the correct variable is called (and not created). That gets to be a pain. Especially if you have more than two member var you are messing with. That's one thing I really like about statically typed languages (i.e. Java).  
  
    
Also, I really stubbed my toe the other day on making a global variable work in two different files the other day. I eventually got it working, but it just seemed like I had to work harder than I have had to before. In fact, it reminded me of trying to make a global variable/class in Java, which makes me long for C++. Well, ok, maybe long is a bit strong... ;)  
  
    
Someone out there (I think I might have read it on [zephyrfalcon.org](http://42.blogs.warnock.me.uk/2004/09/zephyrfalconorg.html)) was mentioning what a pain it can be to refactor dynamic languages like python (because you don't have a compiler to complain about things not being there as you move stuff around). I can identify with that, so that's why I'm planning on checking out the pylint project. Hopefully it can shed some light into what I've done on my RPG engine that I'm working on. (I have a ton of code that I'm pretty sure isn't being called, but I don't want to do anything to it yet until I finish refactoring other parts of it first).  

