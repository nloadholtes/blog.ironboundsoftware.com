---
layout:     post
title:      "Lightweight TDD"
date:       2009-05-25 16:10:18
author:     nickadmin
categories: programming,software development,thinking
tags:  
permalink: /2009/05/25/lightweight-tdd/
---
The more I used Unit Testing (particularly JUnit) the more I like it. It is a great way of tracking progress in your code, and more importantly making sure you haven't broken something in the process. I'm not a huge fan of traditional Test Driven Design (TDD) though. My biggest complaint is writing a battery of tests before writing the actual code feels like putting the cart before the horse. I've been experimenting with it, and most of the time I've found  that if my code is structured "correctly" (i.e. a well defined API/interfaces, dependency injection, etc.) TDD will work pretty well. However I have found that I like to use TDD one test case at a time. Basically I will get the basic framework of my class(es) together, and then as I refine the capabilities of the class, add in a few tests to catch one or two conditions. Then I work on my code to make sure that it is performing as expected. Once everything is going well the tests pass and it is time to move on to the  next part of the class. The big advantage for me in this is that I only have to worry about getting a small number of tests to pass instead of all (or a large number) of them. By breaking the tasks down into smaller pieces I find that I spend less time "dreaming" about how my code would work (and writing tests that don't accomplish much or have to be re-written as reality sinks in). Instead I'm able to focus on a single problem and solving it. This is a similar approach as to what is advocated in the unit testing community: When a bug is found, create a test that exposes it. Then fix the code and the test should prove that the underlying problem is gone. I really like that approach and I have begun doing that as often as I can. So far it has really paid off in terms of making sure my code doesn't have bad case of "but-I-already-fixed-that!" type of bugs.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc1Nzg2ODk4MV19
-->