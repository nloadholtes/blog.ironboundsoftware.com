---
layout:     post
title:      "Quick network troubleshooting tips"
date:       2016-05-09 11:24:06
author:     admin
categories: linux
tags:  
permalink: /2016/05/09/quick-network-troubleshooting-tips/
---
Network troubleshooting is an essential skill here in the age of the cloud. As systems become more and more distributed (hello microservices!) the network connection between them becomes more and more important. Let's look at some quick and basic techniques you can use to try and understand what is going on with the network. [caption id="attachment_656" align="alignleft" width="420"][![a network card for network troubleshooting](https://ironboundsoftware.com/blog/wp-content/uploads/2016/04/640px-ForeRunnerLE_25_ATM_Network_Interface_1-420x280.jpg)](https://ironboundsoftware.com/blog/wp-content/uploads/2016/04/640px-ForeRunnerLE_25_ATM_Network_Interface_1.jpg) This was state of the art not too long ago. A whopping 2.5 Mbps! [Credit](https://commons.wikimedia.org/wiki/File:ForeRunnerLE_25_ATM_Network_Interface_\(1\).jpg)[/caption] 

## Linux: Your best friend/worst enemy

I have found that linux (or some other unix environment) is the best tool with which to do network troubleshooting. It has very powerful tools with installed by default, or they are only a quick "apt-get install" away. Windows does have good tools also, but it seemed to me that linux had the edge for many years. At any rate, I recommend using linux for anything development related. One thing to be aware of: while the linux tools are powerful, the documentation around them can be a little bit... difficult. This is partly because the tools are being written and used by experts, and partly because its difficult to make some of these topics accessible in a quick manner. Let's dive in! 

## The best network troubleshooting tools

Here are some of the tools I've gotten the best results from over the years: 

### ping

Ping is awesome and dirt simple. What it does is send a packet over the network to a destination. The destination responds and that will tell you lots of useful information like: 

  * Is the destination there? (Assuming it is configured to respond to pings)
  * How long does it take the ping message to get there (useful to know if there's a routing issue that is slowing packets down)
  * Are all of the packets getting there? (sometimes packets will get eaten by the network)

For me, ping is a first step to establish that my network is there, and that I can actually reach the remote machine. If that isn't the case, then pretty much anything you do in your python code isn't going to matter, it will never get to the destination. 

### netstat

As you write networking code you'll run into weird messages about ports being already bound. Or questions about who is connecting to your service. (I've had that question about whether a boss has looked at some flask service that I've written!) The purpose of netstat is to show you a poll of what is connecting to your machine and on which points. netstat has a lot of useful flags, I tend to use "-an" the most. That specifies "all protocols" and "no name resolution". That will show you a listing of what ports on your machine are being used (for example, is your [flask app](http://flask.pocoo.org/) running and LISTENing on port 5000) and which remote machines are connecting to your machine. 

### curl/wget/nc/telnet

Sometimes you just need to see what the remote service is sending down the wire. These tools are very useful for connecting to those remote services and then sending some data. With curl and wget, you are basically sending high level commands (HTTP for web, FTP for ftp, etc.) and then seeing the response. This is very useful for network troubleshooting of API's to see what they are returning. The verbose flags are a life saver with these, they will show you the HTTP headers that are normally hidden/handled by your web browser. 

> As a side note, you can also use the "Developer Tools" in your web browser to get similar information. In fact, there's a lot of times where that would be a better course of action: the GUI there is nicely tied to the assets you see on the screen and can really simplify debugging.

If you are wanting to talk to a service that isn't speaking HTTP or FTP protocols, nc and telnet are great little tools to user. They allow you to open a "raw" connection to the remote end and then send what ever text you want. This is a great little hack for talking to SMTP servers, you can open the connection and manually exercise your handshake to see what the remote server sends. 

### ab

Sometimes you just need to see what happens when you send a bunch of requests to a web service. The Apache benchmark tool (known as ab) is great for this. It can send a configurable amount of traffic to a destination and report back a lot of interesting stats concerning speed, packet loss, and other interesting things. 

### python

Python makes this list because sometimes I just need a simple HTTP webserver to respond to some request. Using "python -m SimpleHTTPServer" on the command line will quickly start up a very simple webserver that is perfect for responding to requests (say from a tool like ab). 

## Other tools and resources

Linux has no shortage of fun tools for network troubleshooting. Here's a quick list of some more that I've seen used, but haven't personally had to use too much. 

  * nmap -- For mapping out a network
  * iptables -- For doing all kinds of routing magic on a linux box (imagine you want to manually configure a router, this is something that will let you do that)
  * ifconfig -- I do use this one occasionally, its useful if you [need to change a MAC address](https://en.wikibooks.org/wiki/Changing_Your_MAC_Address/Linux) or make sure your network connector/connection is up.
  * wireshark -- A great little tool for watching what is happening on the network at a very low level.

Additionally, I would highly recommend reading this [awesome blog post about using tcpdump to watch what is going on in your network.](http://jvns.ca/blog/2016/03/16/tcpdump-is-amazing/)

## Why and how would you use these tools?

I've personally used these tools for the following glamours reasons: 

  * To find out if I'm really connected to the network
  * To find out if I'm really connected to the  **right** network (VPN's can be a killer if you aren't connect to them!)
  * To find out if everyone is speaking the right protocols (you would be surprised how easy it is to mismatch http and https with something else)
  * To test the health of a network connection (not all are created the same, and some are very noisy)

As a unique example of using ping: One time I was working on a machine that we had to connect to via a dialup line. Doing the initial telnet would timeout while waiting for the modem to dial and bridge the networks. So I wrote a script that would spawn a background ping (which would cause the modem to start to dial), then pause for a few seconds before kicking off the telnet command. The end result was I could enter one command once, and be connected to my destination. Also the ping would serve as a keep-alive mechanism so I didn't loose my telnet session if I had to get up and go to the bathroom/lunch/whatever. 

## Wrapping up

Hopefully these tools will give you the insight into what's going on with your network. I know they have helped me with my network troubleshooting over the years (and as recently as yesterday). Are there any tools I left out? I'd love to know about any awesome and useful power tools out there. Leave a comment or tweet at me: [@nloadholtes](https://twitter.com/nloadholtes) and let me know!
