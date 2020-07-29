---
layout:     post
title:      "Adventures with minimongo"
date:       2016-08-15 11:03:06
author:     nickadmin
categories: mongo,python
tags:  
permalink: /2016/08/15/adventures-with-python-minimongo/
---
[caption id="attachment_802" align="alignright" width="240"][![python minimongo is the best choice](https://ironboundsoftware.com/blog-imgs/uploads/2016/08/3009281516_cbdb542932_m.jpg)](https://ironboundsoftware.com/blog-imgs/uploads/2016/08/3009281516_cbdb542932_m.jpg) Too many choices! https://flic.kr/p/5zVmy5[/caption] Over the last few years I have wound up using [mongo](https://www.mongodb.com/) as my data store on several projects. In fact, it has been a while since I have written any SQL! For my latest project I again reached for mongo to hold my data, but this time I decided to use the Python minimongo project as my ODM (Object Document Mapper). 

## What is minimongo?

An ODM is to no-SQL what an ORM (Object Relation Model) is to a SQL database. For Python, [minimongo](https://github.com/slacy/minimongo) is a small lightweight wrapper around mongo. Minimongo is built on top of pymongo which is a leading ODM in the python world. The main appeal of mongo is its ease of use. Python minimongo also has this, particularly if you are already familiar with mongo's query syntax. My favorite feature is how you can access the fields in your document. Minimongo provides the traditional dict-like access, but it also provides field-like access! Here's an example: 

## Why minimongo?

Honestly, all of the python mongo libraries out there are pretty nice. There's little differences between them, but most of the time I feel it comes down personal preference. For example, I worked with [Ming](http://ming.readthedocs.io/en/latest/) on one project. My boss happened to be one of the authors of Ming. I found some of the practices (the session creation and the calls to compile_all()) to be a little... well, not my cup of tea. They aren't bad, but they just didn't feel like the right choice to me. On a later project I inherited a code base that used [mongoengine](http://docs.mongoengine.org/tutorial.html). Mongoengine is nice, and I liked it better than ming, but it still felt... well, just too much. That project was using embedded documents which might have tainted my view of mongoengine a little bit. Over all it is great library, but for my new project I felt like going a different direction. Minimongo is built on top of pymongo. A quick search for the best python library for mongo shows that [pymongo](http://api.mongodb.com/python/current/) is highly regarded. The requirements for this project are pretty basic and pymongo's feature set is impressive. With its ability to add field-like access and minimal code needed to get up and running, minimogo really spoke to me. Querying for documents feels more natural with minimongo than it does with mongoengine. One basically puts in a mongo query (which itself if is just Javascript/JSON) and boom, you've got documents. Other ODM's queries feel more heavyweight to me. Knowing that I can play with a query in mongo's shell and then just drop it into my python code gives me confidence that I'm getting the data I want. 

## So what's the downside?

Being a layer on top of a library has its advantages and disadvantages. With minimongo the biggest disadvantage I've run across so far is with authentication. In my production environment I'm using a username and password. Which is security 101. The issue is that when I establish my connection to the database it doesn't seem to invoke the auth() command. So when my first call to mongo happens, it fails. The solution is pretty simple, it is adding a call to Document.auth() right after the connection is made. But... that also feels like a huge hack. Calling the connection() should in my opinion do the auth for you. After all, you are connecting! This seems to be an issue with pymongo, and since minimongo rides on top of it, that's where I'm seeing the issue. It is a quirk, but comparatively it is not the worst thing in the world. And since my needs are rather modest in this project, this isn't a showstopper. One more interesting feature: no schema declaration. You just define a class and map it to the collection in mongo and then go. It is an interesting approach. My data schema is in flux a little bit, so having this flexibility is pretty useful right now. I can go do whatever, and minimongo just goes with the flow. How this will work once I hit production might be another story though. I am a huge fan of declaring your types. 

## In conclusion: Try python minimongo

In the world of the startup MVP, ease of development is king. Minimongo is a very useful tool to help you get up and running fast. Try it out and let me know what you think!
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI1OTA3MDYzMl19
-->