---
layout:     post
title:      "Hacking around memory limits in the cloud"
date:       2016-03-14 12:04:09
author:     admin
categories: cloud
tags:  
permalink: /2016/03/14/hacking-around-memory-limits-cloud/
---
I love cloud instances. Easy to provision computers in a data center where I don't have to worry about the power or network staying up? Sign me up! But sometimes they have some limitations that can be a pain. Like a lack of memory. Small instances (which are perfect for hacking around) tend to have smaller amounts of RAM which can be an issue when compiling code or running certain "less than optimal" code. 

## Memory? But... its the cloud!

I recently ran into this issue while trying to compile some [go code](https://golang.org/) on a [Digital Ocean droplet.](https://m.do.co/c/76f9b19dc762) (that's a referral link for a $10 credit which is 2 months of a small droplet!) I don't have a lot of experience with the go language, so when the code didn't compile certain things, I was little bit puzzled. The compile output was... pretty minimal, just: 

camlistore.org/dev/devcam go build camlistore.org/dev/devcam: /usr/local/go/pkg/tool/linux_amd64/link: signal: killed

Most of the code (this was the [Camlistore](https://camlistore.org) project by the way) compiled with no problem. I had recently run into issues with limited RAM on cloud machines, so my first thought was that maybe that was what was happening here. So I restarted the build and fired up htop to watch what was happening. Here's a screen shot I took while the build was happening: [caption id="attachment_595" align="aligncenter" width="584"][![A screen shot showing memory utilization](https://ironboundsoftware.com/blog/wp-content/uploads/2016/03/Screenshot-from-2016-03-12-201534-1200x130.png)](https://ironboundsoftware.com/blog/wp-content/uploads/2016/03/Screenshot-from-2016-03-12-201534.png) No swap but lots of RAM being used. No one will like how it turns out.[/caption] The RAM was being maxed out during the build. Plus there is no swap space setup by default on these small droplets. Honestly, I don't normally think about swap space, on my dev machines I have lots of RAM so I rarely have to hit the swap space. But on a 512MB droplet... we've got a different situation. So, the choices are: 

  1. Get a bigger droplet (but this will cost more money)
  2. Since this is go, we could compile it somewhere else and just upload the binary
  3. Get some swap!

I really don't want to #1, just because its a pain to do for 5 minutes. Plus every time I need to recompile I'll have to do that. #2 is interesting because go is really flexable like that. But the whole point of this droplet is to allow me to do development from anywhere. So that is a no-starter. It turns out #3 is not very hard to do at all. I did some commands (more on those in a second) and then restarted the compile. Looking at htop: [caption id="attachment_594" align="aligncenter" width="1168"][![screenshot of memory utilization](https://ironboundsoftware.com/blog/wp-content/uploads/2016/03/Screenshot-from-2016-03-12-202136.png)](https://ironboundsoftware.com/blog/wp-content/uploads/2016/03/Screenshot-from-2016-03-12-202136.png) Now with some swap and lots of RAM used[/caption] This time the swap was present and it was used. And even more importantly, the build completed successfully! So by sacrificing a few MB of disk space I was able to "double" the amount of memory available to the system. Since the majority of the time the droplet isn't using most if its RAM, the swap will just sit there unused. So how easy was this to do? Very easy! Using the instructions I found on [this awesome page](http://www.cyberciti.biz/faq/linux-add-a-swap-file-howto/), I was able to get the swap created and running in about a minute. For the record, here are the commands I typed into my droplet:  And that's it! I was surprised how easy it was to do, and it solved so many problems for me. I went with a 512MB swap space, but the only real limit is the amount of drive space. If you are still having problems even after making this swap space, I'd recommend doubling it in size. If you are over 4GB of swap space and still having problems... then you might have a different problem. :) 

## Wrapping up

So, if you are on a cloud machine and things aren't working, look into adding some swap space. A little bit of swap can go a long way!
