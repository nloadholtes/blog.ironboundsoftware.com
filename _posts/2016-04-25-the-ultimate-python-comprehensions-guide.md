---
layout:     post
title:      "The ultimate python comprehensions guide"
date:       2016-04-25 11:09:42
author:     admin
categories: programming,python,software development,uncategorized
tags:  
permalink: /2016/04/25/ultimate-python-comprehensions-guide/
---
I came across this[ AMAZING guide on comprehensions in python](https://gist.github.com/bearfrieze/a746c6f12d8bada03589) the other day. Seriously, you should go check it out because it is great. It is Star Wars themed which makes it that much more awesome. [caption id="attachment_647" align="alignleft" width="420"][![comprehensions are like card tricks](https://ironboundsoftware.com/blog-imgs/uploads/2016/04/Display_Card_Flourish-420x349.jpg)](https://ironboundsoftware.com/blog-imgs/uploads/2016/04/Display_Card_Flourish.jpg) By ShahanB - who took the photo in 2012, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=23480947[/caption] Comprehensions are one of my favorite things about python. They are so useful for making lists (and other things) in a very small amount of code. There is so much you can do with them, especially when combined with some of the other "power tools" that python as, especially the functools. Having said that there are some downsides that should be taken into consideration. For example, there's always the temptation to use our newest shiniest tools where ever we can. And with comprehensions that can lead to one of the biggest problems: nested comprehensions. 

## Comprehensions can backfire?

Yes, you can put a comprehension inside of your comprehension. At first glance some would say "Sure, why not?" but those people are rarely the ones that maintain that software. I have seen nested comprehensions that spanned several lines in order to keep the column width to something reasonable. That should probably the warning sign number one. Splitting a comprehension to fit onto a second line is most likely ok, but the moment it starts to leak onto a second line you should stop and consider what you are doing with your code. 

## Too much memory?

Another downside of reckless comprehension use is using too much memory. Comprehensions allocate memory as they are building the list. If the number of elements being iterated over is small this will not really be a problem. HOWEVER, once your code hits production we all know what happens: you run into a user who submits something with 10,000 elements and suddenly your system grinds to a halt. Thankfully python has something to help us out with this: generators. [Generator comprehensions](https://wiki.python.org/moin/Generators) are very similar to regular list comprehensions with one major exception: The list isn't generated at that line of code, but rather once it is actually accessed (e.g. being iterated over). This prevents massive amounts of memory from being allocated and as a pleasant side effect your code will "typically" run faster. 

> I put typically in quotes there because as with all things in life, your mileage will vary. Things that work great for me might not work for you, yadda yadda, yadda. Be sure to measure and test your code in your environment.

## Wrapping up

Comprehensions are awesome. The article I linked to covers them is really great detail, and while I encourage all python developers to use them, you do need to know the limits. So go look at your code and see if you can use these today!
