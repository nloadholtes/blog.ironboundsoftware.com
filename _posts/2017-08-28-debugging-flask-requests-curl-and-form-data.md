---
layout:     post
title:      "Debugging Flask, requests, curl, and form data"
date:       2017-08-28 10:09:40
categories: debugging
tags:  
permalink: /2017/08/28/debugging-flask-requests-curl-and-form-data/
---
Here's a recent situation I found myself in where some HTTP form data was not appearing like we expected. 

## Debugging Flask

The basic setup is this: A Django process is replaying some HTTP traffic to another system that is written in Flask. The issue was that some requests that were coming in had form data that wasn't making it to the other system. [![](https://ironboundsoftware.com/blog/wp-content/uploads/2017/08/html-1-420x315.jpg)](https://ironboundsoftware.com/blog/wp-content/uploads/2017/08/html-1.jpg) To help troubleshoot this, I created a simple [flask](http://flask.pocoo.org/) app that would echo out the headers, body, and form fields it saw on incoming requests. Let’s call this the receiving program. The idea was that we could point our relay app to that address and dump out everything so we could see what the issue was. The first thing that I noticed was that our form POSTs did not have any of the form fields I was expecting. There was nothing in the request.form or request.body fields. At this point I was concerned that there was something I was missing in how flask was either reading the request or in how it was sending it. To narrow it down I chose to use curl to send requests to my receiving program. This revealed what turned out to be the first problem: The receiving program was looking for form data, but the replay program wasn’t sending it. When I did a curl command like this: 

curl http://receiver/hello --data ‘{“my”:”form”,”data”:”blah”}’

I would see the receiver print out the data. So that pointed to my replay code as being a source of the problem. 

## Sending form data with requests

The replay code uses the most excellent Requests library to do its HTTP communication. Requests is very easy to use, most of the time just doing a requests.post(url, data=<your data to send>) is all you need to do. But for form data there is another option. It turns out you can also send multipart form data by swapping out the data parameter with the “files” parameter. This is where my debugging went off the rails for an hour. 

## The wrong path

My original code was using the data parameter but I wasn’t seeing anything pop out in the receiver. Putting 2 and 2 together I managed to get 153 and figured I must be using the wrong parameter so I replaced data with files and retested. To my surprise, the receiving program was still not seeing any form data! In the flask code looking at request.form revealed an empty string! After using [pdbpp](https://pypi.python.org/pypi/pdbpp/) to step through the code and inspect the request object closer I made a surprising discovery: The data I sent was in the request.files field! Thoroughly confused I killed the receiving program and replaced it with the nc command. [NetCat](https://en.wikipedia.org/wiki/Netcat) (nc) is a handy utility that can send or receive data on a socket. I had reached a point where I didn’t understand why or how Flask was getting the data and manipulating my HTTP request. Invoking the command: 

nc -l 5000

Makes nc listen on port 5000. As it listen it dumps out what it receives. Since HTTP is a plain-text protocol, I could see exactly what it was sending. In this case it was sending: [![](https://ironboundsoftware.com/blog/wp-content/uploads/2017/08/49e0ff83e6a744178097470d90c08bad-2.jpg)](https://ironboundsoftware.com/blog/wp-content/uploads/2017/08/49e0ff83e6a744178097470d90c08bad-2.jpg) Which looks pretty different compared to what curl was sending: [![](https://ironboundsoftware.com/blog/wp-content/uploads/2017/08/45307360650a44159c76983333aa7ad2.jpg)](https://ironboundsoftware.com/blog/wp-content/uploads/2017/08/45307360650a44159c76983333aa7ad2.jpg)The big difference is that one has the markers for multipart and the other doesn’t. What gives? The [multipart](https://en.wikipedia.org/wiki/Multipart/form-data) is just that: “Multiple Parts”. As when you are sending things mixed together in the same requests like HTML and images. The plain form (the 2nd example) doesn’t have that because we are declaring in the header that the entire request is going to be one type. For my replay code, this is what we were doing in the first place, and it was correct. 

## Where’s the beef?

So at this point we have walked in a giant circle. It turns out I was sending the data correctly, but it wasn’t being seen. What gives? Going back and investigating the original replay code I focused on logic where we handle form encoded requests. It turned out we had a nasty bug in how we detected and handled form data. To identify requests with form data we were looking at the Content-Type field and looking for “form-data”. The code looked like this: 

If request.content_type == “form-data”

This is a bit of a problem because the accepted Content-Types for form data have a lot more text in them. (Specifically “application/x-www-form-urlencoded” and “multipart/form-data”) This resulted in us never looking at the request.form field to get the data! For the morbidly curious, the next few lines took data from request.body which is blank if the Content-Type is set to some kind of form data. Further down the line when it was time to replay the data, we took what happened to be a properly formatted Content-Type and then passed along an empty string in the data field. As soon as I changed the logic to: 

If “form” in request.content_type:

The code started working as expected. It detected the form data properly, and then put it into the correct spot before transmitting to the receiving program. 

## The lessons learned

First and foremost, make sure you are sending the data you think you are. :) Other lessons: 

  * Even though form data can look like the body of an HTTP request, Flask will treat it differently if the Content-Type is set correctly
  * Using curl to send “correct” requests is a great way to confirm your code is sending the data you think it is.
  * Debugging flask sometimes means using other tools. Using netcat/nc to dump out the data is an even better way to make sure you are really sending what you think you are sending.


