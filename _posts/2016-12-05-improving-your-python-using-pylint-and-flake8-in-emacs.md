---
layout:     post
title:      "Improving your python: using pylint and flake8 in emacs"
date:       2016-12-05 09:30:38
author:     nickadmin
categories: emacs,python,python
tags:  
permalink: /2016/12/05/improving-your-python-pylint-and-flake8-emacs/
---
[![python using pylint flake8 in emacs](https://ironboundsoftware.com/blog-imgs/uploads/2016/12/Screenshot-from-2016-12-04-193943-420x512.png)](https://ironboundsoftware.com/blog-imgs/uploads/2016/12/Screenshot-from-2016-12-04-193943.png)In a previous post I mentioned an issue I had with some [python code that failed in a way I hadn't expected](https://ironboundsoftware.com/blog/2016/11/07/on-moving-from-java-into-python/). Long story short, I was in the wrong which does happen from time to time. Aside from the actual bug, there was another failure: I thought my tools were checking my work. It turned out this was not the case! I've been a big fan of [flake8](http://pypi.python.org/pypi/flake8) for some time. Its ability to find PEP8 issues is a big help, and most of the time I find that it tends to root out problem code before it gets too bad. When I was dealing with that bug I was using [PyCharm](https://www.jetbrains.com/pycharm). I've since started using [emacs](https://www.gnu.org/software/emacs/), but would that have made a difference? It turns out if I had been using [pylint](https://pylint.readthedocs.io/en/latest/) I **might** have caught this issue. I'm placing the emphasis on might there because there's a bit of overlap between flake8 and pylint that I wasn't aware of. Let's explore them a little bit more.

## What is flake8?

[Flake8](http://flake8.pycqa.org/en/latest/index.html) is tool for checking your python code against the [PEP8 standard](https://www.python.org/dev/peps/pep-0008/). It combines several tools together into one easy to use package. It is a very useful tool and every python developer should be familiar with it. There are other PEP8 tools, but over the years I've found the flake8 seems to be the best. So I always tend to have it installed and my IDE configured to use it. 

## So what is pylint?

Pylint is a tool that checks the source code for certain errors. ([Linters](https://en.wikipedia.org/wiki/Lint_\(software\)) are pretty, awesome, you should use one no matter what language you are working in!) After reading [this great blog post about pylint ](https://codewithoutrules.com/2016/10/19/pylint/)I realized I am not running pylint to its fullest potential. While pylint can look at PEP8 things, its powers seem to be more in the realm of "is this software correct" which is what I'm in desperate need of. Just take a look at the .pylintrc file vs the .flake8 config file. It is amazing how much you can customize pylint! After reading Itamar's blog I followed his advice and wound up suppressing most of pylint's output just so I could get a handle on what it was looking at. In the end, I have decided to let flake8 handle all of the formatting issues (line length, overhanging indents, etc.) and let pylint handle everything else. This way each tool gets to play to their strengths, and I get the best of both worlds (hopefully). 

## Running this all in emacs

_Quick note: I'm assuming you are running a recent version of emacs and have followed the[excellent suggestions in this article about how to setup emacs as a python development environment](https://realpython.com/blog/python/emacs-the-best-python-editor/). There's a LOT to this topic, and I'm only skimming the surface of what is possible with this setup._ So, if one is truly hardcore, one would set up pylint to run every time you save a python file. I'm not quite at that level yet, so I'm settling for manually invoking it as I go. 

> Another alternative would be to have it run as a git pre-commit hook. This way you can clean before your commit.

To run pylint, all one has to do is invoke "M-x pylint" and pylint will fire off and report its results in a new buffer. The cool thing here is that the buffer can link the results to a specific line in your source. Clicking on that takes you right to the spot, just like any other IDE. Since I'm leaning on flake8 to handle the "formatting" issues, the pylint output should take me straight to the true code issues. 

## So how well does this work?

Getting a "truthy" answer out of these tools is a little bit of an art. Following Itamar's suggestion of making .pylintrc that blocks everything and slowly brings in specific warnings is a good start. But you run the risk of getting tunnel vision and only enabling rules that make sense in the module/project that you are looking at. For example, I have 2 legacy projects that routinely crash pylint because of huge modules (several thousand lines of code, and the formatting is all off). Making a pylintrc file that works on one project might mask issues in the other file.  _The real answer is that those files should be refactored and broken up, but that isn't feasible at the moment so I've got roll with what I've got._ An additional perspective I've really enjoyed recently is "[Static analysis will not save us from broken software](http://www.drmaciver.com/2016/10/static-typing-will-not-save-us-from-broken-software/)". I won't sum it up, you should just go read it. :) 

## Wrapping up

I've skimmed the surface of a lot of different things here. If you would like to hear more about how I'm using emacs to do development with python, please drop me a comment and let me know!
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg3ODkyNjg5OF19
-->