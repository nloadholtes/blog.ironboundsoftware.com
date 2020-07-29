---
layout:     post
title:      "Linking against Python on the Mac"
date:       2010-05-29 07:00:12
author:     nickadmin
categories: os x,python
tags:  
permalink: /2010/05/29/linking-against-python-on-the-mac/
---
Today while working with [swig](http://swig.org) I kept running into problems trying to get python to read the generated output files. The error I finally wound up with was: 

> Fatal Python error: Interpreter not initialized (version mismatch?)
> 
> Abort trap
>
>> Fatal Python error: Interpreter not initialized (version mismatch?)
>
>> Abort trap

It turns out that on the Mac (OSX 10.6) that you have to pass gcc a special flag if you want to link against the python library. Traditionally you would do something like this:

> gcc myfile.c -l **python** -shared -o mylib.so

But on the Mac is you have the Mac specific installer version of python (I think as opposed to building it at the command line), there is no libpython.so on your system, so the _-lpython_ flag never works.

The solution is to use the _-framework_ which tells gcc to look into the framework directory where OSX stores all of its specially configured tools/utilities/programs. (If you are wondering the python 2.6 framework is kept at this location: /Library/Frameworks/Python.framework/Versions/2.6/)

So using the example above, the proper incantation to produce a useable shared library linked against python is:

> gcc myfile.c - **framework python** -shared -o mylib.so

That should produce something useable.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI1MjA1NjQzNF19
-->