---
layout:     post
title:      "Your Cocoa/XCode tip of the day"
date:       2006-12-02 23:23:13
categories: apple
---
When working with a Cocoa project (in XCode), if you decide to add a .cpp file (and it's .h file) to the project you might notice a problem when building. I banged my head into this for about an hour before figuring it out. When I added the file(s), I did so by clicking on "New" and selecting a C++ file under "BSD" because it was the first option that I saw. It turns out when you do this, the Cocoa project settings will attempt to compile the files as Objective-C files (which they are not). This results in cryptic messages about a "parse error before" in you .h file. The solution is to right click on the .cpp file, select info, then change the file type to "sourcecode.cpp.objcpp". This tells XCode to use the Objective-C++ compiler to build the files, and from then on everything *seemed* to work ok. I've never worked with Objective-C (or Obj-C++), so I'm figuring this out as I go. If something bad seems to happen, I'll post a follow up to let everyone know.
