---
layout:     post
title:      "Installing OpenCV for Python on OS X"
date:       2014-11-09 20:09:18
author:     nickadmin
categories: os x,python
tags:  
permalink: /2014/11/09/installing-opencv-for-python-on-os-x/
---
[OpenCV](http://opencv.org/) is a computer vision library. It is a really powerful library and has bindings for Python. The only thing that it doesn't have is a good explanation of how to make the python bindings work! Here is how I got it to work on my Mac (running OS X 10.9.5) inside of a virtualenv. 

  1. Install cmake (brew install cmake) and the normal development tools
  2. Download and unzip the OpenCV code
  3. Change directories into the OpenCV directory
  4. Type in "cmake CMakeLists.txt"
  5. Type in "make -j5" (this will use 5 threads and make the code build pretty fast)
  6. Type in "make opencv_python2"
  7. Type in "sudo make install" (to install all of the code)

At this point the python code has been installed to the main system python in /usr/local/lib/python2.7/site-packages which is not very helpful if you are using a virtualenv (which is what you should be using if you are working in python!) The next step is to copy the OpenCV files from the global directory into your virtualenv. This is done by typing in the following: 

cp /usr/local/lib/python2.7/site-packages/cv2.so <path_to_your_virtualenv>/lib/python2.7/site-packages/

This will copy the .so created during the build to your virtualenv which will make it accessible to your python code. At this point you should be able to fire up the python interpreter in you virtualenv and type in: 

> import cv2

and it should work. Happy Computer Visioning!
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MzkxNzk2NTldfQ==
-->