---
layout:     post
title:      "Using Python argparse and arguments with dashes"
date:       2018-01-20 10:30:20
author:     nickadmin
categories: python
tags:  
permalink: /2018/01/20/python-argparse-arguments-with-dashes/
---
Have you ever been soooooo close to putting a puzzle together only to discover at the last minute that you are missing a piece? This happens to me all the time when I'm coding and I hit that last little bit that isn't covered in a tutorial. Here's a recent example with the Python argparse module. Recently I have been using Python to create a bunch of command line tools. It is really useful to use the [argparse](https://docs.python.org/2.7/library/argparse.html) module to help create the parameters that you can pass into your scripts.  But one thing that I've noticed that was a problem  that you can't easily have a variable with a dash in the name on the command line. Most Unix utilities have some kind of option like --dry-run but with argparser it is not clear how to do that. The way that argparse works is by letting you define variables that command line parameters are passed into. This means that the variables that you define for the command line have to match the format of Python variables. So all the rules that would normally be used for python variables have to be used for your command line variables.  The issue is that most Unix-like operating systems allow you to have a dash in a variable name. I really like this because it allows for more descriptive variable names. But those do not work in Python because the dash means subtraction. So it is not an allowed character for variable name.

## Enter the metavar

This restriction made my arguments look weird when I needed to use a multi word variable. After some research (see below) I discovered the “[metavar](https://docs.python.org/2.7/library/argparse.html#metavar)” parameter. Using this allows you to specify what the command line version of that variable looks like. I use this to help to define variables like “src-dir”  on the command line but had to translate into “src_dir” inside of my python code here's an example of how this would look.  This code just sets up a basic argparser object, and then defines 2 parameter, src-dir and dest-dir. With the metavar field set in the code, when we run the code with no params we get a very nice error message: [![python argparse no parameters passed in](https://ironboundsoftware.com/blog-imgs/uploads/2017/12/no-args2-744x91.png)](https://ironboundsoftware.com/blog-imgs/uploads/2017/12/no-args2.png) Just to expand on how awesome argparse can be, you get a "help" section for free! If you repeat the command but with the -h flag you will get a nice little help screen: [![python argparse help example](https://ironboundsoftware.com/blog-imgs/uploads/2017/12/help-detail2-744x262.png)](https://ironboundsoftware.com/blog-imgs/uploads/2017/12/help-detail2.png) And just for completeness, this is what it looks like when code is successfully run: [![python argparse success](https://ironboundsoftware.com/blog-imgs/uploads/2017/12/success2-744x49.png)](https://ironboundsoftware.com/blog-imgs/uploads/2017/12/success2.png) The metavar parameter can also let you define multiple names for a variable which can be useful in some situations. You should really check it out! 

## Further reading

As always the Python documentation is a great place to learn more. While trying to discover this missing piece, I found this mailing list posting. It's the really useful discussion of this problem. Thanks to it I was able to make my script have much more expressive command line flags. [https://mail.python.org/pipermail/docs/2012-July/009292.html](https://mail.python.org/pipermail/docs/2012-July/009292.html) The Python argparse module rocks! :)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2MjI5MTEzNV19
-->