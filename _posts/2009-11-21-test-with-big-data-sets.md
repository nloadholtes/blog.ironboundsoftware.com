---
layout:     post
title:      "Test with big data sets"
date:       2009-11-21 17:01:36
author:     admin
categories: programming
tags:  
permalink: /2009/11/21/test-with-big-data-sets/
---
Every so often I re-learn this lesson: Make sure you test your code with the same amount of data that your users will use. Developing with small data sets is fine, and most of the time that is what you want to do as you work out the kinks of the code. But when it is time to ship the code, you must test with a large data set. For rent my resume.com I've been testing one portion of it with 4 different size documents. This is a fluke however, I chose the documents based on the contents not the size. Today I made a simple change that turned out to have some unforeseen ripple effects. When I write unit tests, they seem to fall into two categories: Tests where I just do a simple check on the size of a return (i.e. did I get 21 items in the list?), and tests where I check the contents of the resulting data. 

> As a side note, you should really do both kinds of tests, not one or the other. Simply checking to see that the right number of things was returned is no substitute for making sure that the correct data was actually returned!

Today I was re-running my pyunit tests and one of the four failed because the size of the returned list wasn't what was expected. By coincidence this happened to be the biggest data set I was testing with. If I had not had this test, I would have thought everything was ok, but it truth my modified function is returning questionable data! There are of course other benefits of using larger data sets, mainly seeing how your code works under stress. What works fine for 10 items might not be so great with 1000 items. Testing with a large data set at the end will help catch these problems and will also help you adhere to Knuths' advice to not optimize code prematurely. So, now I'm off to learn how to trace through python code to find out how such a seemingly simple "fix" to my code could so subtly break it...
