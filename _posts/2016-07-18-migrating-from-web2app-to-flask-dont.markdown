---
layout:     post
title:      "Migrating from web2app to flask? Don't"
date:       2016-07-18 09:20:09
categories: api
---
[caption id="attachment_728" align="alignright" width="320"][![train of moving web2app to flask](https://ironboundsoftware.com/blog/wp-content/uploads/2016/07/train.gif)](https://ironboundsoftware.com/blog/wp-content/uploads/2016/07/train.gif) Me moving an app from web2app to flask[/caption] Recently I decided to pull an old project out and use it as the basis of a new exciting thing I'm working on.  _More on that later!_ The old code was running on [Google App Engine](https://appengine.google.com) (GAE) and was written using the python web2app framework. Let's take a look at the why and how of converting from web2app to flask. 

## Why web2app?

GAE is pretty generous when it comes to letting developers run small apps on their service. That is a great way to get developer buy-in on your product. For years I've been running a couple of small projects for free on GAE and then talking about them in interviews. The documentation for GAE used to use web2app as the Python sample code. Over the years they have evolved the service and documentation and today they tend to show Flask and Django when they are displaying sample code. As a result of this, all of my GAE hosted projects have wound up being on web2app. And in the case of my current project, this is a problem. 

## Why switch to flask?

I'm a big proponent of making things simple, and [flask](http://flask.pocoo.org/) makes me feel like I'm living that creed. It is a small lightweight framework that lets me get small things done quickly. Don't get me wrong, Django is nice, but when I want a simple API flask feels like a better choice. Compared to web2app, flask feels easier to work with. Obviously your mileage will vary, but for me, flask is a better choice. GAE used to require developers to "vendor" 3rd party libraries when deploying python code. This seems to have changed and now you can simply supply a requirements.txt file and it will install everything you need. This is a similar approach used by other services. This new approach on GAE allows for more modern development practices and since flask is pip install-able... it just made the decision to port the code from web2app to flask that much easier. Couple that with the documentation now uses flask to show how to make a GAE web app... it just seems like the right thing to do. 

## So its pretty smooth to convert web2app to flask right?

Actually...  **no.** Some things were just a matter of simple search-and-replace (example: the swapping out the request references and the base class). Other things were more annoying (changing the URL routes). But one thing killed all motivation for me: the tests. I had written a nice little test suite to exercise the code base. And in doing so I wound up tightly coupling it Google's datastore API and the internal structure of my views. Now these are bad engineering practices done exclusively by your truly. They alone are not a reason to give up. But... when combined with the amount of work it looked like I was going to have to do in moving from web2app to flask, it really made me stop and evaluate the code and the amount of time I'd spend working on it in the hopes of making it eventually work. I decided to throw the code out and start over. 

## So what about all of that code?!??!

The data being operated on is the most important part of the old code base. That was something I was able to rescue and put in a nice neutral format. The 2nd most important thing is the API that the code was providing. API design is something I've always struggled with. It is difficult to create something that is both simple and useful. When I surveyed what I had created (both the code and the actual API footprint) I realized I had neither. Since this API isn't public, this is the perfect time to burn it to the ground and rebuild it the right way. The right way, as I eluded to above, is to have a solid API design. For me, this means writing a [swagger/Open API](https://openapis.org/) document. I now have a central point of truth for both my code and anyone who utilizes the API because I did this design document first. And as a bonus there are tools out there to generate working flask code from the swagger document. 

## So what does that accomplish?

There are several awesome benefits of generating the code based off of this document: 

  1. The code will do what the document describes. (Which means the API and the code will match up with each other.)
  2. By generating the code from the document we are forcing a separation of concerns in our code: the web layer code should only make simple function calls to the business logic. This way if the API changes, the web layer will be regenerated the impact will be minimal.
  3. I'm letting someone else make the "boilerplate" decisions

#3 might be a little controversial for some developers. "I need to make all of the decisions! I can't trust the computer to Do The Right Thing!" many will argue. Well, I disagree. That's the same argument that has been used to defend the poor decisions that have lead to all manner of security bugs over the years. It just doesn't hold water. Those boilerplate decisions are a 90% solution. Using them will get you 90% of the way there. And for 90% of the people, 90% of the time this is exactly what is needed. The"boilerplate" code is **not**  where developer should be spending 90% of their time and effort. Think about it: If you truly treated the web layer as a disposable asset that can be re-generated at will, then suddenly it doesn't matter what web framework you are using. Moving from web2app to flask becomes a moot point. The business logic (and the data it supports) are the most important things in your project. Those are now isolated into their own modules that are separate from the web specific code. This helps tremendously with #2, if I ever need to switch out the web layer again, the impact of that change on the tests should be minimal. 

## Wrapping up (and unwrapping from the axle)

When I started this project I was convinced that web2app was what was holding my project back from being a great success. To my surprise after some analysis it became clear that moving from web2app to flask was not the problem I need to focus on. It is focusing on the design of the API and data, and then letting a tool help with gluing those together. Don't let the [Sunk Cost Fallacy](http://www.lifehack.org/articles/communication/how-the-sunk-cost-fallacy-makes-you-act-stupid.html) hold you back from making the right decision. At times it will be hard, but in the end you will end up with a better product and code base.
