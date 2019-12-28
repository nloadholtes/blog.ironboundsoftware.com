---
layout:     post
title:      "Getting rid of getters and setters"
date:       2007-06-28 19:35:01
author:     nick
categories: java,programming,python
tags:  
permalink: /2007/06/28/getting-rid-of-getters-and-setters/
---
Today I read an interesting post about mistakes Java programmers make when they start writing Python code. The one that really caught my eye was "Don't create getters and setters!". Apparently a lot of other Python newbies are doing that. I started out creating getters and setters in python a while ago and in the last month or so (while refactoring) it occurred to me that it was a waste of time since you can't make member variables in python private like you can in Java. The more I thought about it, the more I started to wonder why I was doing straight getters and setters in Java. I mean, if all I'm doing is assigning a variable (no format checking, etc.), the having that extra code doesn't really make much sense does it? So, I'm on a fact finding mission to discover the what happens when getters and setters are left out in Java code and the class field is accessed directly. Yes, I know, its not OO. But if the object is just a bean and its only reason for existence is to be an member of an abstract data type (like a struct in C), then why not just let it run free? Aside from situations where you are manipulating the field in some way (like formatting, or whatnot), all the getters and setter get you is more code on the screen.
