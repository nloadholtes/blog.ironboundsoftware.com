---
layout:     post
title:      "Faster Flask: Why you need gunicorn"
date:       2016-06-27 10:22:33
author:     nickadmin
categories: flask,python,uncategorized,web
tags:  
permalink: /2016/06/27/faster-flask-need-gunicorn/
---
While doing some performance test on a new flask microservice, I noticed it was not handling very very many connections per second. Additionally, nginx (which we are using as our front end webserver) was reporting a ton of errors. 

WTF?!? I thought flask was fast. I need a faster flask! [caption id="attachment_710" align="alignright" width="640"][![faster flask](https://ironboundsoftware.com/blog-imgs/uploads/2016/06/8736451330_e38fe86a77_z.jpg)](https://ironboundsoftware.com/blog-imgs/uploads/2016/06/8736451330_e38fe86a77_z.jpg) Racing to make a faster flask[/caption]  

## Making a faster flask

The investigation of this took a little while because there were so many new variables at play. Not only was the flask service "new" to the stack, but the deployment environment was as well. (We are using[ AWS ElasticBeanstalk](https://aws.amazon.com/elasticbeanstalk/) to run this particular service.) After a few hours we narrowed down our list of suspects to nginx and [flask](http://flask.pocoo.org/). 

Nginx is a well known and well respected web server, but there were questions about how it was configured. We were using a "stock" BeanStalk AMI that was supposedly setup as a webserver... but it wouldn't be the first time a vendor told me a lie. 

Flask was a suspect as well because... well, there's just nothing else to point at after we eliminated the network, the EC2 instance type, the phase of the moon, and the code itself. 

Some quick googling revealed that pretty much anytime flask is mentioned uWsgi and gunicorn are said in the same breath. Why is that? 

## Oh, this seemed familiar...

The "webserver" that ships with flask (e.g. "app.run()") is really great for local development. And that's about it. It isn't designed to take the abuse that a normal webserver receives. 

Our microservice was using that runner. A WSGI HTTP server like [gunicorn](http://gunicorn.org/) (or uWsgi)  **is designed** to take that kind of abuse from the web. It turns out that it is a widely known best practice to use gunicorn to run your flask app when you deploy to production. The crazy thing is... I've had this problem before and completely forgot about it! 

On a previous project we had the  _exact same problem_ , but with [Turbogears](http://www.turbogears.org/). In that situation we had a very low-traffic internal website that worked for quite a while until the performance issues came to light. 

With this new flask project, it saw the problems immediately due to volume of traffic it was seeing. On all of the previous projects I had worked on someone else had done this step early-ish in the project so I had never seen it setup before. This isn't an excuse so much as it is a testament to the power of gunicorn (and the smartness of my past co-workers). Everything just worked, and I never even noticed gunicorn sitting in our stack. 

Gunicorn works by internally handing the calling of your flask code. This is done by having workers ready to handle the requests instead of the sequential one-at-a-time model that the default flask server provides. The end result is your app can handle more requests per second. 

Faster flask FTW! Setting up gunicorn to run your flask project could not be any simpler:   

## But wait, there's more!

It turns out that with gunicorn in place the errors that we were seeing in nginx virtually disappeared. This is awesome because I was not looking forward to having to tune a supposedly tuned nginx installation. 

In hindsight, the errors were probably due to the flask process not pooling connection and doing any of the magic that gunicorn is doing. As soon as we started to see improvements in performance we turned to look at our EC2 instance type. 

We "downgraded" to a cheaper type that happened to have 2 cores. This instantly increased our performance! And if that wasn't enough, our CPU utilization went way down, and the throughput (overall) went up. The system became so stable we have found that our scaling events are fewer and farther between. 

Translated into business English: we are spending less money while handling more traffic! 

## Wrapping up

Flask is awesome. Using gunicorn will make it even more awesome. 

For next level awesomeness, throw it all onto Amazon's ElasticBeanstalk. 

The end result? Faster flask, more traffic.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NzU5Mzc0NDBdfQ==
-->