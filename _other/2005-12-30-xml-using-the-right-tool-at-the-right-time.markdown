---
layout:     post
title:      "XML: Using the right tool at the right time"
date:       2005-12-30 10:35:30
categories: blogging
---
The other day I was whipping together a quick little program and it occurred to me that it could stand to have some of its configuration settings written out so that the next time I ran it I would be able to pick up where I left off. And then the weirdest thing happened: I thought to myself I need to make an XML file to store those settings. This is weird because I usually take the quickest and easiest path for finishing something, and in this case it would be a properties file (or an ini file, or a key-value pair). For some reason I slipped into the fad of "make it use XML!". The moral of the story is to take a step back and look at what you are doing. If something doesn't seem to fit in with the rest of the code, you should ask yourself if you are going in the right direction. If you aren't, change it.
