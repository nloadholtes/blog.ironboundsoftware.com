---
layout:     post
title:      "Testing AppEngine cron jobs locally"
date:       2018-03-19 08:30:18
categories: programming
---
Lately I've been doing a lot with [Google AppEngine](https://cloud.google.com/appengine/). It has a lot of great features, but to get those you need to give up a few things. Sadly I discovered that included the ability to locally run "protected" API endpoints. At least until I discovered this one strange trick to make everything work... 

# The setup

So AppEngine applications need an `app.yaml` file that defines a lot of things needed to run the code. It is also defines the routing for the app's endpoints, and who is allowed to access them. _(Basically either administrators, or the whole world)_ My app is making use of the [cron.yaml](https://cloud.google.com/appengine/docs/standard/python/config/cron) file to periodically ping certain endpoints in the app. The catch is that I don't want just anyone hitting those endpoints, a bad actor could hammer that sensitive endpoint and kill my API access. 

> ![Did someone say "Bad Actor"?](/blog/wp-content/uploads/2018/03/bad-actor.gif) _Did someone say "Bad Actor"?_

Thankfully, Google recognized this and allows you to setup endpoints in the `app.yaml` file with a `login:` parameter. Setting this to "admin" tells AppEngine that only logged in users who have admin rights to the domain are allowed to hit that end point. Yay! I don't have to write any custom login/user management code. But.... 

# The problem

If you are running the code locally, say doing **development** , you are probably going to need to hit those end points to make sure the damn thing is working. Right? Well, the `dev_appserver.py` script doesn't know about who is and isn't logged into Google... because it is only running on localhost! Therefore having the login set to "admin" means you will **never** be able to access that endpoint. _Boo Hoo, HTTP 302 for you._ So, what do we do? Commenting out the `login:` field will let you access it locally, but what if you _accidently_ deploy that into production? (Spoiler alert: You are :screwed:) 

# Run to the console

Although `dev_appserver.py` is the cause of our problems, it also turns out to be the solution too! When `dev_appserver.py` boots, it not only starts your app, but it also starts a lightweight admin app too. This app by default runs on `localhost:8000` and provides all kinds of useful tools like a DataStore viewer and... a cron utility! Going to `localhost:8000/cron` brings up a page that lists all of the (AppEngine application) registered cron jobs, what schedule they are setup to run on, and.... wait for it... a.... button to kick off that job! Yes, by clicking on that button the admin console will trigger your cron job for you so that you can run and see the results locally! Yay for debugging ~~locally~~ **not in production!**

# Other tricks

The admin console is pretty awesome and has lots of other useful tricks up it sleeves. Here's some of what I use it for: * Doing quick checks on entities stored in the DataStore * Faking incoming XMPP and SMTP messages (I've never tried this, but it looks pretty cool for one off testing) * A memcache viewer/editor * An interactive console That last one is pretty sweet. Since I can't seem to startup an IPython terminal AND connect it up to my app, this is the next best thing. From the webpage it will let you type in some Python code and it will execute it for you. Perfect for those times when you just want to delete all of your entries because you had a horrible misspelling in one of the field names. Not that I've ever done that. 

* * *

> _If you are curious to see the app I built using AppEngine, check out[RemoteMatcher](https://RemoteMatcher.com)! It is a remote job aggregator that scans a bunch of job sites and only emails you the ones that match your interests. No more scanning tons of boards, instead just check your inbox for the best matches._
