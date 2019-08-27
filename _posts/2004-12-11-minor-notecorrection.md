---
layout:     post
title:      "Minor note/correction"
date:       2004-12-11 04:39:58
author:     Nick
categories: programming
tags:  
permalink: /2004/12/11/minor-notecorrection/
---
    
The [thumbnailer post](http://www.pycs.net/users/0000316/2004/12/6) does have a slight flaw in it, if you have a a jpg file that ends in .JPG the program will totally ignore it. I just discovered directory it completely passed over. Quick fix is to modify the code where it says ".jpg" to say ".JPG".   
  
    
Yes, a better solution would be to pass in the file type at the command line or to have the program determine the type of file at run time.... But since I'm done with my thumbnail/gallery making for the moment, it can wait till the next time I use it.  

