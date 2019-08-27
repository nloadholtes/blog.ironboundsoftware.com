---
layout:     post
title:      "Python function overloading via multimethods"
date:       2010-07-21 19:13:57
author:     admin
categories: python
tags:  
permalink: /2010/07/21/python-function-overloading-via-multimethods/
---
One of my favorite features of OO languages like Java is the ability to overload a method, which is where you have several methods with the same name, but they take in different types in their arguments. I love the python language, but as I blogged about a while ago, [not having overloaded methods in python](http://ironboundsoftware.com/blog/2007/05/29/a-shortfall-of-python-no-function-overloading/) is kind of a bummer. But do you have to trade your dynamic freedom in for static types to gain this? It turns out that with a little ingenuity, you can get that functionality using the [generic dispatch pattern](http://en.wikipedia.org/wiki/Multiple_dispatch) and python's decorator syntax. The example on the above wiki page is nice and concise, but I think that [Alex Gaynor's blog post about multimethods is the best](http://alexgaynor.net/2010/jun/26/multimethods-python/) example of how to implement this useful idea. In leiu of an explanation of how it works, Alex gives us a unit test that exercises the mutimethod class and the dispatch/overloading idea that it brings to life. As long as you know what a [decorator](http://www.artima.com/weblogs/viewpost.jsp?thread=240808) is the code does make sense. There are other examples of using a [dispatch](http://mike.axiak.net/blog/2010/06/25/python-generic-dispatch/), but I feel that Alex's is more clear. These are of course no substitute for having function overloading built into the python language, but having the functionality wrapped up in a nice neat class like this is a very good thing.
