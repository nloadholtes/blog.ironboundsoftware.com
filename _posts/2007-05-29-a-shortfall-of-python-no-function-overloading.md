---
layout:     post
title:      "A shortfall of Python: no function overloading"
date:       2007-05-29 19:27:55
author:     Nick
categories: programming
tags:  
permalink: /2007/05/29/a-shortfall-of-python-no-function-overloading/
---
I'm a big fan of [Python](http://python.org). It has little quirks that can be annoying (like having to specify self.method() instead of using scoping rules to look at the class first), but overall I really like the language. But today I ran into a shortfall that I really stubbed my toe on: Python (as of 2.5) doesn't support function overloading. For example, this snippet of code won't run: 

> def a(): print "This is a" def a(x): print "This is a(x)" a()

Instead it will just tell you that _TypeError: a() takes exactly 1 argument (0 given)_ presumably because the second function (a(x)) seems to overwrite the reference to the first one. Further reading on the topic shows that a fix for this might be coming in the future (see [Guido's blog entry](http://www.artima.com/weblogs/viewpost.jsp?thread=155514) for details).  The strange thing for me is I never noticed this until recently. The only reason I ran into it was because I wanted to do some refactoring where it made sense to have an overloaded method. Or at least that's what I would have done in Java. Not having this option available is having an interesting side effect in that it made me step back a little bit and evaluate the "big picture" a little bit more than I normally do. Which in this case isn't a bad thing, hopefully it will cause some me to stretch in new directions and discover my inner OO-Architect...
