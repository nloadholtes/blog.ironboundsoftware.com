---
layout:     post
title:      "Making MPG’s out of JPG’s"
date:       2004-05-14 07:30:20
categories: programming
---
[Dr. Dobb's Journal](http://www.ddj.com) never ceases to amaze me. Every time I pick up the magazine, be it the new issue or an old issue that I found behind my desk, there is always something interesting to read. The April 2004 issue is no exception. There's an Article called "Time-Lapse MPEG Animations" by Stephen B. Jenkins that really caught my eye. Mr. Jenkins writes about how to take the images collected from a web cam (i.e. the jpg) and convert them into a movie (i.e. mpg). The program he present was so simple I was blown away by it. It was short, easy to understand and very simple. In fact the only thing I didn't like about it was that it was written in perl! :) So I took it upon myself to try and turn it into a python program. [The code](http://www.geocities.com/nloadholtes/code/mpgmaker.py.txt) is pretty simple, which is mostly because I'm still new to python. I've tried it out in windows and it seemed to work pretty good. (Except don't collect too many images, the convert program seems to break pretty easily) The program goes out to a web cam (a NASA web cam that is watching a satellite picture of Florida) and ever minute or so grabs the picture and saves it to the disk. Once you hit Ctrl-C it will then launch convert (a program provided by ImageMagick) which takes the jpgs and glues them together to make a MPG (basically 1 image = 1 frame). Its not the most useful program in the world, but it is kinda neat to see what things look like over time. If you want to plug in other web cams, check out [Google](http://www.google.com) to see what the most popular ones are these days. 

  * [mpgmaker.py](http://www.geocities.com/nloadholtes/code/mpgmaker.py.txt)

 
