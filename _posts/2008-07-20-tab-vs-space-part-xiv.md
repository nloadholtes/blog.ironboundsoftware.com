---
layout:     post
title:      "Tab vs. Space, part XIV"
date:       2008-07-20 13:51:50
author:     nickadmin
categories: apple,os x,programming,python
tags:  
permalink: /2008/07/20/tab-vs-space-part-xiv/
---
So, lets say you are working in XCode 3, and you are trying to build a PyObjC app but for some reason the python code you wrote isn't getting called. If you are seeing weird errors in the console when you run the application (specifically "Could not connect the action <your_action> to target of class <your_AppDelgate_class>"), here's what it probably is: In the AppDelegate python file that XCode creates it uses spaces to do the indentation of the methods. I hail from a land where tabs are used for such tasks, and the use of spaces is look down upon in much the same way that pick ones nose in public is. At any rate, what's happening is when the code is compiled/run the python interpreter is not recognizing the new methods that I put in (using tabs to indent) and instead of giving me a warning about inconsistent indention, it fails somewhat silently in that it groans it can't hook the action up to the class and that's it. It wasn't until I turned on the invisible characters that this occurred to me that it might be the root cause of my problems. Once setting all of the indentions to be the same, I chose tabs, everything worked like a champ. By the way, if you are looking for some tutorials for PyObjC in XCode 3 (there are a ton of XCode 2 tutorials out there, but things have changed ever so slightly in 3), be sure to check out these links: 

  * [PyObjC Hello world for XCode 3](http://orestis.gr/en/blog/2008/05/17/pyobjc-hello-world/)
  * [PyObjC Resources](http://vstock.free.fr/pyobjc.html)


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYwMzE4MTkwNF19
-->