---
layout:     post
title:      "Python Debugging"
date:       2017-09-25 09:36:36
categories: debugging
tags:  
permalink: /2017/09/25/python-debugging/
---
[![cool beetle from https://pixabay.com/en/bug-insect-beetle-wasp-yellow-34375/](https://ironboundsoftware.com/blog/wp-content/uploads/2017/09/bug-34375_640-420x327.png)](https://pythondebugging.com)Python is an awesome language and environment to work in. And thanks to some great tools Python debugging can actually be fun! Let's look at some of the things that separate Python debugging from debugging in other languages: 

## Interactive debugging

Compared to other languages like Java, Python values interactive tools like the REPL. The REPL (Read-Evaluate-Print-Loop) allows Python developers to “experiment” on code without having to go through the usual write/save/compile/run cycle. This feature carries over into the built in Python debugger pdb. With pdb you can do all of the normal debug operation like stepping into code, etc, but you can also run simple arbitrary Python code! 

## Command line first

With everything moving to “the cloud” these days things the command line is becoming more important than ever. Since most Python debugging tools are build off of pdb, it is now super convenient to use the debugger on a remote machine. Simply ssh into your remote machines and boom, you can start using pdb just like you would on your local machine. Hopefully this isn’t something you will need to do often, but as we all know sometimes things happen in production that just don’t happen on your local dev machine. It is great to have this option! 

## Choices!

While pdb is pretty cool as it is, there are other choices and options to make it even more awesome! Here are some command line tools that can make your Python debugging experience more enjoyable: 

  * [pdb++](https://pypi.python.org/pypi/pdbpp/) \-- Just `pip install pdbpp` and you will get a new coat of paint on pdb with tab completion, colors, and more!
  * [PuDB](https://pypi.python.org/pypi/pudb) \-- A cool text-based GUI for debugging
  * [better_exceptions](https://github.com/qix-/better-exceptions) \-- A pretty printer for your exceptions

And of course there are more visual oriented tools, for those who prefer working in Integrated Development Environments (IDE’s). Here’s some great ones that I have used: 
  * [PyCharm](https://www.jetbrains.com/pycharm/) \-- My preferred Python IDE. Lots of great things in this tool, and I highly recommend it to everyone.
  * Wing IDE -- Another popular IDE I have used off and on over the years.
  * Eclipse -- Is there anything Eclipse can’t do? With the installation of a few plugins it becomes a decent Python IDE.

Each of these offers the ability to set breakpoints, examine the stack, and all kinds of other debugging goodness all in a nice and easy to look at format. If you are just starting out with Python I highly recommend checking them out to help guide you as you learn the language. 

## More on Python Debugging

I've collected my best tips on Python Debugging into an e-book called "Adventures In Python Debugging". Check it out over at [PythonDebugging.com](https://pythondebugging.com). There's a free 5 day email course if you would like to get a sample of the book and learn more![![Adventures In Python Debugging book cover](https://ironboundsoftware.com/blog/wp-content/uploads/2017/09/Cover-1b-420x339.png)](https://pythondebugging.com)
