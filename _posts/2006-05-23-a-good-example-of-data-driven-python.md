---
layout:     post
title:      "A good example of data-driven Python"
date:       2006-05-23 20:56:04
categories: programming
tags:  
permalink: /2006/05/23/a-good-example-of-data-driven-python/
---
Have you ever had something on the tip of your tongue, but you just couldn't get the words out? I felt that way with a Python program I've been knocking around with for a while now (its an RPG that I swear I'm going to finish some day...). Every time I looked at the code I kept thinking that there must be a way to make it more data driven (like in the book [Game Programming with Python](http://amzn.to/2gTguwt)), but I just kept hitting sticking points. The other day on the [Pygame](http://pygame.org/) Mailing list, I saw this post describing a [simple, elegant, data driven solution for an RPG](http://aspn.activestate.com/ASPN/Mail/Message/pygame-users/3136283). I was floored. This code helped me bridge a couple of different ideas together. I had read about making items flexible by making them via "[instance relationships](http://www.amazon.com/gp/sitbv3/reader/104-0939561-6656763?%5Fencoding=UTF8&keywords=instance%20relationship&v=search-inside&asin=0761532994)" (i.e. damage objects can inflict damage onto breakable objects). I thought it was a really interesting idea, but hadn't really thought much about how to bring it to life. At any rate, this chunk of code was a real inspiration and I thought I would share it in case anyone else is curious about integrating data driven concepts into their code. Check it out!
