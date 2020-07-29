---
layout:     post
title:      "python __debug__"
date:       2017-01-09 09:31:36
author:     nickadmin
categories: python
tags:  
permalink: /2017/01/09/python-__debug__/
---
The other day I stumbled upon Python __debug__ and I thought I would share some interesting things I learned about it. 

## What is python __debug__?

It is a constant that Python uses to determine if calls to assert should result in code being generated. If you have the -O optimization flag  set, then assert calls will not be "triggered" in your code, even if the condition it is testing is true. Interesting fact: [according to the documentation](https://docs.python.org/2/library/constants.html) it is one of two constants that will raise a [SyntaxError](https://docs.python.org/2/library/exceptions.html#exceptions.SyntaxError) exception if you attempt to assign something to it. (The other constant that does this is None.) For example, in python you can do this: [caption id="attachment_987" align="aligncenter" width="229"][![How to assign false to true in python](https://ironboundsoftware.com/blog-imgs/uploads/2017/01/true-is-false.png)](https://ironboundsoftware.com/blog-imgs/uploads/2017/01/true-is-false.png) Totally legal. Not smart, but legal.[/caption] And that is totally legal in Python 2.x. (Python 3 wisely does not allow this!) I would not recommend doing this, as your co-workers will hunt you down to express their "displeasure". But if you try that with __debug__ or None, you'll get an error: [caption id="attachment_986" align="aligncenter" width="380"][![can't assign things to __debug__ or None](https://ironboundsoftware.com/blog-imgs/uploads/2017/01/debug-and-none-assignment.png)](https://ironboundsoftware.com/blog-imgs/uploads/2017/01/debug-and-none-assignment.png) The only two "true" constants in python[/caption] Normally I'm not a fan of these types of language tricks, but this looked pretty cool to me and I thought I would share. I do find it interesting that in Python 3 they have True and False locked down to be true constants. Honestly, I thought there would be more language keywords that would be protected like that.  
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk2NzQ1NTgxM119
-->