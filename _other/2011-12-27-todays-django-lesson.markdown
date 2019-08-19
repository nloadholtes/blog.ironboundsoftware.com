---
layout:     post
title:      "Today's Django lesson"
date:       2011-12-27 18:37:16
categories: django
---
Today I was working on re-doing [my main website](http://ironboundsoftware.com). I have built the site in [Django](https://www.djangoproject.com/), and then when I'm ready to publish I use the static generator module to create an html snapshot of the pages that I then upload to the server. Basically I wanted the fun of using Django, but the ease of serving up static html pages. The last time I did this, the version of Django was 0.9 and today's version is 1.3.1. As a I started work on the site I discovered some things here and there that had changed in the years in-between those version. The one that bit me the hardest was this: I could view the main page (/), but any other page (including index) would give me a 404 error. This was really weird because the mappings existed in the urls.py file, but a 404 error means it couldn't be found. If it was a programmatic error you would expect a 500 error, but I never saw one. Slowly but surely I tore the system apart looking to see what could cause mapped urls to disappear in Django. Eventually I discovered the root cause was how static resources are handled. One of the changes in the new versions of Django was to add functionality for handling static resources. The biggest change (at least as far as my ancient code was concerned) was in introduction of the STATIC_URL variable. According the documentation this is the prefix for static resources (like css, javascript) that are referenced by the web page that is being built by Django. In my laziness many years ago, I just plopped the main CSS file (and everything else) in the root of the web directory so that in the html pages didn't have to have paths on them. So when I was adding the STATIC_URL variable to make sure my CSS file would actually load, I set the variable this way: 

> STATIC_URL = '/'

...because it wouldn't let me put an empty string of ''. Well, it turns out that this was wrong wrong wrong. Django was looking at the incoming requests as I tried to visit the pages of the site and checking the static directory to see if there was anything there (which there wasn't, just my CSS file). Once I realized this, I changed it to: 

> STATIC_URL = '/static/'

...which basically forces you to create a directory to hold your static files. Which is right right right right. Basically Django was forcing me to clean up my act and code the site in a much cleaner manner. As soon as I did that all of the 404 errors went away and I was able to hit every page in my urls.py file.
