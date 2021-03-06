---
layout:     post
title:      "Processing large JSON files on small clouds with python"
date:       2016-03-21 11:40:49
author:     nickadmin
categories: programming,python
tags:  
permalink: /2016/03/21/large-json-small-clouds-with-python/
---
[caption id="attachment_599" align="alignright" width="222"][![Clouds as a metaphor for JSON](https://ironboundsoftware.com/blog-imgs/uploads/2016/03/5506788169_77cc7ccb2a_b-744x484.jpg)](https://ironboundsoftware.com/blog-imgs/uploads/2016/03/5506788169_77cc7ccb2a_b.jpg) Clouds are pretty. If only our JSON looked looked like this.[/caption] I am a huge fan of cloud computing. Its easy to get new machines up and running and it also forces you to think more about distributed computing earlier in your projects. Also, it is great that you don't have to go into a noisy cold data center to change out a broken hard drive. 

_Yes, it also means you are running on someone else's computer. Be sure to take that into account as you design you system._

For me, one of the ironies of the cloud is that most cloud machines (EC2, [Digital Ocean](https://m.do.co/c/76f9b19dc762), etc.) tend to have relatively little RAM, at least compared to our desktop development machines. In a production environment this usually isn't aproblem, most applications will run in a fairly narrow band of RAM usage. For example, on most of the small cloud machines you will get 512MB of RAM. (Hey, I thought 640KB was enough for anyone!) But... occasionally you will run into a situation that requires more RAM than usual. Like when you have a JSON file that is kinda big. If it is too big you might not be able to use the typical JSON methods to handle this because the code will error out as it runs out of RAM. This is a situation I ran into recently, and thankfully there is a fairly simple solution that will let you keep running in the cloud. 

## An XML file, a JSON parser, and Micro EC2 instance walk into a bar...

A client of mine had a situation where they were getting XML files on a daily basis. These files were large (typically over 2GB) and being parsed using a streaming parser. The data was then being fed into a Mongo database. The problem was that occasionally we needed to re-process a subset of the file. Processing the whole file could take a few hours, but if we could just process the subset we could be done in a few minutes. I'm pretty anti XML and since the destination for this data was a Mongo database it made sense to me to convert the XML into JSON as we were extracting the subset of data. Then the JSON file could be processed when we were ready. 

_Side note: Instead of writing out the JSON we could have just put the elements into a queue like RabbitMQ and then had a consumer process the data on another machine. But, due to some other constraints and issues I opted to just stick with the JSON file. The queue would have eliminated the memory problems completely, but then this blog post wouldn't have been written. :)_

On a micro EC2 instance or a small [Digital Ocean droplet ](https://m.do.co/c/76f9b19dc762)you are limited to 512MB of RAM. If there's no swap space setup then this becomes a hard limit and your program will crash if it tries to load to much into memory... just like when you call json.load() on a 100 MB JSON file. As it is parsing the JSON file, python is building up objects in the background. This causes your process to consume a lot of memory as it keeps track of everything. On a cloud machine I would start my code and it would just stop running after a few seconds. In the Java world, when you have an OutOfMemoryException it will print that out to the console. Python didn't do that, I had to run the code (on the cloud machine) with the verbose output turned on, and even then it took me minute to understand what was going on. When I ran the code locally on my desktop, I kept an eye on the process to see how much RAM it was using. Turns out it was about 2GB. Whoops! That's 4 times as much as the cloud machine could offer. 

## The wonderful world of streaming

This is actually a pretty common problem in the XML world. XML is pretty verbose as a format, and when you add in some of the other options it has (namespaces, etc.) I can only imagine how much RAM it must use for a standard DOM parser. Thankfully, you can help beat this problem by using the Streaming API XML parser (SAX Parser). But this is JSON. JSON doesn't really have a built in SAX-like parser because... well JSON doesn't have these problems as much because it isn't as verbose as XML. The constraint here is the amount of RAM in the production machine. So can we stream JSON? The answer is YES! There is a wonder pip install-able library called [ijson](https://pypi.python.org/pypi/ijson/) that will provide us with what we need. The code necessary to support stream is a little bit different than what you would normally write for JSON code, but that is because we are now responsible for more of the parsing. Basically we are going to be looking at tokens from the JSON stream and building our objects on-the-fly one at a time, instead of letting the standard library give us a large fully-formed chunk of data at once. The sample code on the[ ijson github page](https://github.com/isagalaev/ijson) sums it up nicely: You make a function that basically does a bunch of if-then statements on each token coming in on the stream. For my situation, my input was a list of objects, so what I needed to do was materialize the objects one at a time and then put them into mongo. In this situation I had a great deal of control over the shape of the JSON. I was able to make it fairly flat, with minimal nesting (e.g. there were no objects-within-objects). That helped simplify the ijson function that I had to write. It was about a dozen or so if statements (this is a spot where a switch/case construct in python would be useful!) and they were pretty vanilla, just assembling the object. The only tricky spot was making sure that we could batch up a couple of objects in memory before sending them over to mongo. I did this because: 

  * We have limited RAM so storing all of the object in memory would just lead to another crash
  * Writing the objects to mongo each time through the loop would be very slow.

Figuring out the batch size was a bit of trial-and-error, I knew the rough size of an individual object so the goal was to find a nice balance between throughput and time. Make sure you measure your data! Here's what my code wound up looking like. For readability I've chopped out a lot of the if statements, but this should be enough to show you how I was building the objects, and how they were being batched off to mongo:   

## In conclusion: JSON + Python = <3

Big JSON can eat up a lot of RAM. In a cloud machine, RAM is one of your most precious resources. But thanks to the ijson library Python can work just fine with a little bit of creative coding. Thanks for reading and leave me a comment if you've got any questions!
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjYzNDM0MjQwXX0=
-->