---
layout:     post
title:      "Why you need tests instead of comments"
date:       2012-12-17 15:52:18
categories: programming
tags:  
permalink: /2012/12/17/tests_vs_comments/
---
Today I saw this blog post from Timothy Fitz:[ I hate comments](http://timothyfitz.com/2012/12/17/I-hate-comments/) My first reaction was to dismiss this as another anti-documentation post by a coder who prefers doing nothing but coding. But... Timothy makes some really good points. His intent isn't to downplay documentation (something that programmers are notorious for skimping on), but rather to play up the need to keep your code honest. The best example is when he notes that a unit test could replace a comment about what a function "should never do". That is a really insightful statement. Instead of leaving a comment, leave a unit test. If you are using a continous integration system, it should detect if someone ever violates the intent of the function. A broken test is much more likely to be seen than a potentially out-of-date comment. I still think comments aren't the "trash" that many programmers believe they are, but I do think that a unit test would be of more value to the code base overall. The funny thing is that if you get into an argument with a programmer about comments and you counter with "Well, lets replace it with a unit test!" I think you will find the programmer suddenly back peddling. If there's one thing a lot of programmers like less than writing comments it is writing unit tests. Which is a shame, because unit tests that give you high code coverage are so useful when you want to keep your system running correctly.
