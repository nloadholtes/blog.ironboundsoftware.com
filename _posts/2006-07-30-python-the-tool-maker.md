---
layout:     post
title:      "Python the tool maker"
date:       2006-07-30 20:51:39
author:     Nick
categories: programming,python
tags:  
permalink: /2006/07/30/python-the-tool-maker/
---
I've been busy with school, so my extra-curricular programming has been pretty low lately. I'm getting back into the swing of things and I noticed that I was going to need to do some work on an XML document. It occurred to me quickly that I don't really have a good XML tool on my system (loooong story on that one, it basically boils down to my pickiness). Since the data schema is going to be fairly static it occurred to me I could just whip up a small program to handle all of this rather than manually hack it all together. [Python](http://python.org) is really great for this kind of stuff. Small code, nimble and agile, it can get into places that other languages can't. So I decided to try and whip up something in python to edit my data files. I haven't really done a lot of GUI work with python before, so I fell back to my previous experience with tkinter, the python interface for TK. Which seemed to be a really good plan until I tried to run a previously working tkinter app on my Macbook. It started up, but nothing works right (boxes missing, save buttons not there, etc.). I figure this is a problem with the Intel chip and a library somewhere that is out-of-wack, but I don't really feel like hunting it down. So, instead I'm going to look into [wxPython](http://wxpython.org/), which seems to be getting a lot of press these days. At a glance it looks like most other GUI toolkits I've seen in the past, so hopefully I'll be able to get up and running quickly.
