---
layout:     post
title:      "Moving from Django to Flask"
date:       2016-06-13 11:11:11
author:     nickadmin
categories: django,flask,uncategorized,web
tags:  
permalink: /2016/06/13/moving-django-to-flask/
---
Recently I was working on a project that involved breaking up a Django app into smaller services. As we looked at the new services it occurred to me that we might be able to use Flask instead of Django. It was pretty straight forward to move things to Flask, but there were a couple of little gotchas that I thought I would share on moving from Django to Flask. 

## Why Django to Flask?

Django is nice! Its got everything a python developer could ever want. But for this project as we broke apart our monolithic app it became apparent quickly that we didn't need a lot of the features that Django brought to the table. Particularly our new micro-services (buzzword alert!) didn't need: 

  * A full HTML templating system (most of the services will just be serving up JSON)
  * A DB ORM layer (nothing is being persisted to a DB in the service, its just passing the data along)

Flask is pretty lightweight compared to Django. I personally like Flask's approach of "plug in what you need", so after talking it over with the team we agreed to try Flask out on some of these new services. 

## So what changed between Django and Flask?

We were able to take a lot of the code out of the monolith and drop it into the new repo/projects without much of a problem. In fact we took this as an opportunity to create some libraries for common code, etc. Overall it was a great experience. The web code was of course where most of our issues occurred. Flask has a different architecture when it comes to the request object. It has a request context that looks a LOT like a global variable, but it isn't. (Check out [the documentation here](http://flask.pocoo.org/docs/0.11/reqcontext/) for more details on this.) Django on the other hand passes in the request to the view when it is invoked. So most of the the work there involved removing the request from the view's parameters. [The Django documentation for the request object is really great.](https://docs.djangoproject.com/en/1.9/ref/request-response/) The next difference we ran into had to do with getting HTTP  headers out of the request. In Django the request.META object has the headers of the HTTP request, but some of them are slightly mangled. The old app had referenced to "HTTP_CONTENT_ENCODING" which was confusing at first. It turns out that maps to "Content-Type" in HTTP Header-speak. The very cool thing is that in Flask this is directly accessible on the request object. You can do "request.content_encoding" to get that value, as opposed to request.META["HTTP_CONTENT_ENCODING"] in Django. Getting the IP address is also very easy in flask, it is just a field on the request object. In the code base I was working on getting the IP address in Django was a little bit more involved. I won't go into detail about how it was being done (just in case that was old code), but it was nice to see its something that's just there in a Flask request object. 

## What about the tests?

We got lucky with the tests, they were pretty easy to move over! In fact I spent more time working on the biz logic than the mechanics of the web framework setup. But that also might due the low-complexity of the tests: Since there was no DB involved in the code's operation there was no need to set up mock DB's or things like that. Sometimes things just go your way! :) 

## Wrapping up

Moving from Django to Flask was relatively painless and we wound up with a smaller set of micro-services. Additionally the "developer overhead" to run the apps locally seems to be smaller as we are able start the apps and go. If you have a large webapp and are interested in smaller services, I'd recommend looking at moving from Django to Flask.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNDk4MTU2OTddfQ==
-->