---
layout:     post
title:      "A big list of Flask resources"
date:       2016-04-04 09:43:08
author:     nickadmin
categories: flask,python,web
tags:  
permalink: /2016/04/04/a-big-list-of-flask-resources/
---
[caption id="" align="alignnone" width="3000"]![Flask web framework logo, flask resources](http://flask.pocoo.org/static/logo/flask.png) The Flask web framework, the best python web framework[/caption] Over the last year I have spent a lot of time with [Flask which is a python web framework](http://flask.pocoo.org/). It is commonly referred to as a micro-framework because it tends to be lightweight and make use of plugins (as opposed to having everything built in like Django). These plugins are what makes Flask great, there is a great variety of common programming tasks that can be accomplished using these plugins. This helps you the programmer because now you don't have to reinvent the wheel. Without these flask resources you would wind up recreating a lot of code. So here are the Flask plugins and tools that I have found really helpful while  developing websites for my clients. 

## Flask Resources and Tutorials

The best place to start  when learning something new is at the beginning. Flask is pretty easy to learn and there are lots of tutorials out there to help programmers of any skill level get up and running quickly. [The Flask homepage](http://flask.pocoo.org/) \-- Because this is a micro-framework, the code to demonstrate "Hello World" is very small. In fact, it is only 7 lines of code! That is so small they actually have it on the front page of their project's website! [The Flask Quickstart](http://flask.pocoo.org/docs/0.10/quickstart/#quickstart) \-- I like this one because it gets you up and running quickly. [Learn Flask in your PJ's](https://youtu.be/xdwwo9xk4u8) \-- This is a great series of 4 YouTube videos that walk you through creating a flask app from scratch. The video also covers other topics like Git and using the[ Cloud 9 IDE](https://c9.io/). 

## Flask Plugins

As I said earlier, one of Flask's strengths is its ecosystem of plugins. These plugins are what makes Flask a micro-framework: Instead of Flask shipping with a million options that might never get used you can go out and get these small chunks of code to do specific tasks. Quick side note: Another benefit of the plugins is that if one doesn't work for you for some reason you have some really interesting options available to you: 

  * You can swap out the plugin to see if a different one works better
  * You can dive into the plugin code and see what it is (or isn't doing)

The first option is great if you want try out a plug-and-play option really quickly (e.g. does this other plugin have this same bug?), or if you want to try out a completely different technology (e.g. can I use [Mongo](https://www.mongodb.org/) instead of SQL as my data store?) So having said all that, here's the plugins I have found to be really helpful (these are pip install-able): 

  * Flask-DebugToolbar -- This is awesome for debugging your app. It is some extra javascript that gets injected into your webpages and it displays all kinds of information about time to download, etc.
  * Flask-DebugToolbar-Mongo -- If you are using Mongo as your data store, then you really owe it to yourself to use this plugin. On each page load it will display some stats to show you the number and timings of your Mongo calls. This is very useful when you are trying to find the slow spots in your code.
  * Flask-Split -- This is a very easy to use A/B testing library. This is useful for testing out things like different "calls to action" so you can see what what works best with your visitors.
  * Flask-Security and/or Flask-Login -- These plugins will handle all of the user-login related code. No one should ever implement that kind of functionality on their own. ALWAYS use a library. Your future self will thank you.
  * Flask-RESTful -- If you are going to make an API with Flask, then you really should look at this flask resource as a way to eliminate a lot of boiler-plate code.



## Wrapping up

I'm a pretty big fan of Flask. It is powerful enough to handle a website that I worked on that got thousands of visitors a day, yet small and lightweight enough to not get in my way as I did my work. These plugins are the secret sauce that makes Flask such a pleasure to work with. Do you know of some great flask resources everyone should know about? Let me know in the comments!
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU0MDI5MDExM119
-->