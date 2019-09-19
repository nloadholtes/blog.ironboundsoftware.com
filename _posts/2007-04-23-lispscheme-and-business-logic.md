---
layout:     post
title:      "Lisp/Scheme and business logic"
date:       2007-04-23 19:27:14
author:     Nick
categories: lisp,programming,software development
tags:  
permalink: /2007/04/23/lispscheme-and-business-logic/
---
I've been thinking about business logic lately. Specifically about how to make nice flexible rules without hard coding them in the code itself. This has led me to look more at Lisp-y languages like Scheme and [Erlang](http://erlang.org). (I've got some more to say about Erlang, but that's a topic for a later post.) At any rate, today on [Reddit](http://reddit.com) there were a few really good postings on this topic and one of those postings led me to more really good articles on the topic. (As a side note, I'm really glad this happened today, lately reddit has been a dumping ground for picture links and other uninteresting things.) While none of these links shows exact methods for implementing business rules, they are a great starting spot. 

  * #### [Stevey's Home Page - The Emacs Problem](http://steve.yegge.googlepages.com/the-emacs-problem)

  * #### [The Fishbowl: Dear XML Programmers...](http://fishbowl.pastiche.org/2003/05/05/dear_xml_programmers)

  * #### [SISC - Second Interpreter of Scheme Code](http://sisc-scheme.org/)


These links also mention a lot about XML and the associated headaches that come with working with it. As one of them pointed out when you (modern programmers) think about storing data, XML usually springs to mind first. Past experiences with XML and XSLT have left a weird taste in my mouth: They seem like they are on to a good idea, but the execution and use of it just feels so contrived. These articles enlightened me to think about the data with more of a functional "lisp" frame of mind. Lots of food for thought. Lately I've been thinking a lot about the MVC pattern and how it is trumpeted all over the place, yet sometimes it doesn't seem to solve the core problem of getting the application out the door to the user in a timely and maintainable manner. (And when I say that, I am thinking mostly of web apps.) Perhaps this is a better way...
