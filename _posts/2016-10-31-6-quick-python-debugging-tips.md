---
layout:     post
title:      "6 Quick python debugging tips"
date:       2016-10-31 11:32:20
author:     nick
categories: debugging,python
tags:  
permalink: /2016/10/31/6-quick-python-debugging-tips/
---
[caption id="attachment_881" align="alignright" width="300"][![python debugging -- image of an actual bug from an old computer](https://ironboundsoftware.com/blog-imgs/uploads/2016/10/debugging-e1477661493656.jpg)](https://ironboundsoftware.com/blog-imgs/uploads/2016/10/debugging.jpg) Debugging with real bugs[/caption] Recently at work I discovered that everyone on my team had different approaches and tools they used for python debugging. Here's a quick run down of some of the favorite tips and techniques that we came up with. This list is ordered from simplest to more advanced.

> Please note: This is a quick run down of tips and tools. Some of these are big topics, so if there's something you would like more detail on, please leave a comment and let me know.

## The humble print statement

Yes, the cornerstone of most debugging statements is the simple print statement. It is dead simple: put some text to the screen. This is a great way to spot check that things are executing. While seeming too simple, it actually can tell you a lot. For example if you don't see any of your expected text, either: 

  * The code isn't being called
  * The stdout is being redirected somewhere

Both of these are useful to know, particularly the 2nd one. Many times I've seen people think code isn't executing because they were looking at the file where the output was going. For example, looking at a .err log file instead of a .out file (or looking at an apache or nginx log, etc.) Situations where print() really shines are when you want to confirm code execution quickly, or on a remote server. 

## import logging

One step up from using print() is to use the python logging libraries. This technique can be a little more complicated to setup than a print() statement, but it offers several advantages: 

  * Different levels of logging that can be used to control the level of detail (error vs warning vs debug)
  * Sending the output to different places

The last one is the most interesting: you can configure logging to other log file (such as the syslog for your computer) or even to other places with logging services like [logz.io](http://logz.io/). Logging services are awesome because they allow you to collect all of your logs in one spot where you can search or share them. 

## An IDE debugger

In this age of modern development the Integrated Development Evironment (IDE) has become an essential tool of productive developer. [There are many advantages to using an IDE](http://pythoncentral.io/text-editors-vs-ides-for-python-development-selecting-the-right-tool/) and one of the biggest is an integrated debugger. An integrated debugger allows a developer to execute their code and then inspect it as it executes. This is a complicated topic and is usually fairly specific to the IDE that is being used. Here is a blog post that talks about [how to use the debugger in PyCharm](http://pedrokroger.net/python-debugger/). If you are new to debugging I highly recommend starting with an IDE in general, and especially if you are going to be doing some python debugging. The tooling in the IDE is very helpful in keep you aware of what is going on in your code. 

## pdb: The command line debugger

Sometimes you can't use an IDE to debug your code. In these instances it is very useful to know about the pdb module that is built into the standard python library. pdb is the underlying tool that is invoked by most higher level tools like an IDE. Pretty much everything that you can do with an IDE debugger you can do with pdb. The biggest difference is pdb debugging tends to be done in a terminal, and the commands are more cryptic. Getting started with pdb is basically putting this statement in: 

import pdb; pdb.set_trace()

into your code at the spot where you would like to inspect things. When that line is hit, the interpreter will stop executing and present you with a prompt. From this prompt you issue commands such as: 

  * s -- Step into a function/method
  * n -- Execute this line and go on to the next
  * c -- Continue (e.g. stop debugging and let the program run)
  * <name of a variable> \-- this will let you see the value of any variables that are in scope
  * ? -- Display the help screen to see what other commands are available

Those are the commands I use the most. There are several more, I would encourage you to explore them to see if they can help you learn more about your code. Doing this type of debugging is especially helpful on remote machines. Although it is possible to connect an IDE to remote machine, it can be complicated. Most of the time if I can ssh into a machine, I find that using pdb is good enough to figure out the problem. 

## pdb++

Debugging in a terminal is my usual way. And as cool as pdb is, it does have a few shortcomings. Thankfully there is an awesome package that adds lots of nice extras to pdb. Let's talk about [pdb++](https://pypi.python.org/pypi/pdbpp/) pdb++ is a helper/wrapper for pdb that adds lots of cool extra functionality. Here's some of my favorites: 

  * Colorized output -- pdb is monochrome, but seeing syntax highlighting can be a huge help when you are trying to get oriented in the code you looking at. Particularly if you use the "l" command to list out the code you are examining.
  * Tab completion -- **This feature alone is worth installing pdb++**. At the debugging prompt you can hit the tab key and it will either complete the command/variable, or show you a list of potential things. This is extremely useful when inspecting objects at run time.
  * Ease of installation -- it is just "pip install pdbpp" to install it.Then in your code you just do the normal "import pdb; pdb.set_trace()" and it works.



> To learn more about pdb++ and debugging in Python, be sure to check out my new book: [Adventures In Python Debugging](https://gum.co/OitWH)

That last one is important. If you use an alternative debugger like ipdb (which is also great for python debugging), you typically have to have a different command to invoke the debugger. In the case of ipdb, this would be "import ipdb; ipdb.set_trace()" This is a disadvantage because if that code got checked into version control and someone else attempts to run it, they will get an error because they don't have ipdb installed. With pdb++, your invocation of it is the same as the regular standard library pdb debugger. So if it gets checked in, you are not "breaking the build" because you are using a non-standard library. 

> Having said that, it is a bad practice to check-in code with the pdb statements in it. If that code gets executed in a production environment it will stop the server from working normally and cause a huge headache. In other words, don't commit your debug work.

One potential downside of pdb++ is that it seems to work best in Python 2.x I have tried to use it in Python 3, but haven't had a lot of luck. To be fair, I also did not spend a lot of time researching this, so things may have improved (or I may have been doing something incorrect.) Here's a few more pdb++ tips I like to use: 

  * args or locals() -- These two commands will show you the arguments that were passed into the current scope, or the variables that are visible in the current scope.
  * cpaste -- If you have a chunk of code you want to paste in, use cpaste to put it all in at once instead of one line at a time. So awesome!



## Debugging from the REPL

All of the advice I've given about using pdb is great if you have the source code and put in the import pdb statement. But what if you are just curious about something while you are using the python REPL? _Note: this tip only works in ipython, not in the standard Python 2.7 REPL_ If you are in the IPython prompt you can type in: 

my_function("params")

to execute the function "my_function()". But if you wanted to debug that function you can type in: 

debug my_function("params")

and this will activate the debugging frame work. Then you can press "s" to step into the function, and viola! You are in the debugger. This is a really awesome trick to use if you want to take a quick look inside of a function. I have started using this trick when I'm messing around with some code in a REPL. The main advantage is that you don't have to modify your source code with import pdb statements. It is also very useful for peeking into how library code is executing. For example I was experimenting with[ Python Elasticsearch](https://elasticsearch-py.readthedocs.io/en/master/) recently and I used this trick to step into the bulk() call to see how it was handling a certain situation. It as very useful. :) 

## Other tools

I've briefly mentioned ipdb and ipython. Both of those are great tools for working with Python code. ipdb depends on ipython, so when you pip install it you will wind up installing both. Overall I like pdb++ better than ipdb, but be sure and try them both out. For a REPL, I do prefer ipython over the standard Python REPL. There are other REPL shells out there, but I haven't played with them as much. 

## Wrapping up: python debugging FTW

Writing python is awesome because of the ecosystem of tools available. Hopefully this guide will help you out as you explore the tools that are available to help make your code better.
