---
layout:     post
title:      "Unicode: Feel the burn"
date:       2009-01-18 19:15:27
categories: django
tags:  
permalink: /2009/01/18/unicode-feel-the-burn/
---
There's nothing worse than having a program that has been running great for X amount of time suddenly start crashing. Especially when you discover that its choking on unicode characters you didn't expect. With web addresses (or URLs if you prefer) starting to have unicode values in them, this is a problem that will probably be more common. I noticed this problem when trying to get to web pages that had special characters in them (for example, URLs that feature characters with accent symbols such as in the Spanish language) would cause urllib2.open() to fail. Several website suggested url encoding these special characters, but I didn't have much luck with it. Also today I was using Django's model layer to store some data (web pages) into a database so I could try some things out. Even though Django is unicode friendly, if there's the slightest problem in mapping text it will pull out the dreaded UnicodeDecodeError at some point. To get around this I wound up just using unicode(text, errors='ignore') to make sure that the text that was being passed in was indeed unicode, and to ignore any errors that cropped up. Not ideal, the better solution would be to map correctly, but better than being stuck with data you can't load/process.
