---
layout:     post
title:      "Making a special string with __str__"
date:       2017-10-02 09:32:29
categories: python
tags:  
permalink: /2017/10/02/making-a-special-string/
---
**“Reuse!”** \-- _The battle cry of Object Oriented_ _aficionados_ Occasionally you really want to use a library so that you don’t have to write your own version of whatever the library provides. But, there’s just one little thing that it doesn’t do. Here’s a story of when this happened to me and how I managed to get around it in a creative manner! At work we are using [Elasticsearch](https://www.elastic.co/) as a datastore for some logging. For “reasons” Elasticsearch [doesn’t encourage the use of TTL](https://www.elastic.co/guide/en/shield/current/limitations.html#_document_expiration__ttl) (time to live) on its records, instead they encourage you to just name your indexes after today’s date and then delete the index when it is past your TTL. And this is ok. But... if you want to use a library like [logzio-python-handler](https://github.com/logzio/logzio-python-handler) this can be a problem. That library has some awesome capabilities but one limitation it has is that expects the index you are writing to is going to be static and unchanging. If you have a long running server process this can be a problem. You don’t want your logs from August 4th being written into the July 14th index because that was when you started the server. You want your logs written to their daily index! But you have to supply a string to the library for it to know where to write to. What?!?!? It would be really impractical to create a new logging handler object every time I needed to write to a logging message! 

## I need a magic string

So when I was faced with this problem recently I thought about it for a few minutes. It occurred to me if I could pass a function to the library and let that function get called and generate the correct string, that would solve my problem. See, a string is an object. And when an string is being printed out Python calls the **str** () method on the object to get that string. So all I needed to do create my own object with its own special **str** method! Here’s what I did:  When the logzio logging handler runs it is going to call that MagicURL’s **str** () method which is going to figure out today’s date and plug it into the URL, and then return that to the framework. At that point the the messages will write to the correct index. The advantage of this is that as you app stays up for days and weeks (it does, doesn’t it?) the logging messages will automatically roll forward into the new index every day. The other huge advantage here is that you don’t have to change the library in any way. You are simply passing in an object with special behavior and letting the library be a black box. Here’s what it looks like to call this in action:  The end result is that we got to use this library (instead of trying to re-implement it ourselves) and we got the behavior we needed out of it. A win-win! 

## Wrapping up

The next time you see something that “just takes a string”, remember that you can define the string with a little bit of magic. The **str** method lets you inject more runtime logic into places it wouldn't normally go!
