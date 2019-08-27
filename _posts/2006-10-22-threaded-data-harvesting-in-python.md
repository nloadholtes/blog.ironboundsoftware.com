---
layout:     post
title:      "Threaded data harvesting in Python"
date:       2006-10-22 23:57:17
author:     Nick
categories: programming
tags:  
permalink: /2006/10/22/threaded-data-harvesting-in-python/
---
Before it slips my mind (again), I wanted to drop this link to this [awesome example](http://www.davidnaylor.co.uk/archives/2006/10/19/threaded-data-collection-with-python-including-examples/) of using python and threads to do interesting work. The article discusses using the threads to go out on the internet and gather data (i.e. RSS feeds), parse them, and store the results in a database. The "pattern" that is shown in the article is really good for any language that uses threads. I personally haven't had a chance/need to use python's thread capability, but I do use them in Java occasionally. Using a the work queues is a great way of making sure that the worker threads are fed (say that three times fast), and the idea of having the output work of the threads feed into a database thread (to help make sure that the database doesn't get slammed, but the workers can keep going) is really great. I haven't run into that situation yet, but this is one of those cool ideas to take note of and keep in your back pocket. You never know when you are going to need that ace in the hole.
