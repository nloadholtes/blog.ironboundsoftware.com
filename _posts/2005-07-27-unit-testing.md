---
layout:     post
title:      "Unit Testing"
date:       2005-07-27 16:25:25
categories: programming
tags:  
permalink: /2005/07/27/unit-testing/
---
Lately I've been on a Unit Testing kick with my code. Unit testing is one of those topics that I agree with in principal, but have a hard time taking action with it. A lot of the proponents of unit testing talk endlessly about how they write tests that go down into the lowest levels of their programs. I don't like that kind of testing, I find when I try to do it I wind up spinning my wheels and fretting over small things.  
  
I tend to try and test more at the "business logic level" because I think this is where I get more bang for my development buck with unit testing. Testing at this level also allows me as the developer to get a firmer grasp on what the program is doing and trying to do in the big picture. I think a lot of customers/end users will appreciate that; there is nothing worse than a techie trying to snow you with an overly complicated report of their activities that you'll never understand. Keeping it at the business level allows everyone to feel more confident that the final product is going to be what is needed.  
  
And every now and then you'll come across a story where unit testing some code saved the day. [Ned Batchelder](http://www.nedbatchelder.com/blog) had a story in his blog the other day about how he had almost 100% code coverage in his unit test. He was down to only having one line that was not tested. He finally wrote a test for it and lo-and-behold it found a bug! It was a small bug, but still a bug. Check out the story [here](http://www.nedbatchelder.com/blog/200507.html#e20050726T080754).  
  
Tags:[Software Development](http://technorati.com/tag/software%20development), [Unit Testing](http://technorati.com/tag/unit%20testing)  
  

