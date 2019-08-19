---
layout:     post
title:      "Running python tests randomly with randomize"
date:       2013-07-02 15:07:44
categories: python
tags:  
permalink: /2013/07/02/running-python-tests-randomly-with-randomize/
---
Recently I was having a conversation with a co-worker about some test problems we were having. While we were brainstorming the idea of running the tests randomly came up. A quick search showed that someone else had been thinking about this issue too, but it looked like it never went anywhere. The code that we found was here[ on google code](https://code.google.com/p/python-nose/issues/detail?id=255) but from the discussion it seems like the code was never included in nose, nor was it submitted to [pypi](https://pypi.python.org/pypi). There was what looked like one repository on github that had this code, but it too wasn't in the best shape. So... I decided to grab the code from the Issue on Google Code and start up a new Github repo for it. I added several tests and fixed 1 little bug that I found and today I released it to the world. If you are doing testing with nose in python, you can check out [randomize, a nose plugin for running tests in a random order](https://github.com/nloadholtes/nose-randomize). The main reason you would want to do this is to ensure that there are no dependencies between your tests. This is very important for unit tests, they should be isolated and independent. This plugin helps confirm that isolation. How it works: Basically as classes are read into the testing framework the plugin gets called and it will apply python's random.shuffle() to the tests to produce a random order of the tests. One shortcoming of the plugin is that is only shuffles the tests, not the classes that hold them. (If anyone is interested in implementing this, please feel free to send me a pull request!) Installation is simple. On the command line just type in: 

> pip install randomize

and then you'll have it installed and ready to run. To use the plugin, all you will need to do is this: 

> nosetests --randomize

And that will invoke it. When it runs it will print out a seed number and then begin executing the tests. If for some reason you need to re-run the tests (say to troubleshoot a test failure), all you need to do is run: 

> nosetests --randomize --seed=<the seed number>

and that will re-run the tests in the same order.
