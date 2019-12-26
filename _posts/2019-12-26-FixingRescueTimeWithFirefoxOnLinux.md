---
title: Fixing RescueTime with Firefox on Linux
layout:     post
date:       2019-12-26
author:     Nick
categories: linux
tags: linux
---
Over the years I've been a  big proponent of tracking my time in some fashion. I really want to know if I'm being productive, and tools like [RescueTime](https://www.rescuetime.com/) have been a huge help with that!

A couple of months ago I ran into a strange problem where RescueTime wasn't recording the websites I was visiting in FireFox (which is now my primary browser thanks to their attention to privacy). 

I recently discovered a way to resolve this, and thought I would share it with the world in case there are other FireFox users on Linux that are seeing the same issue.

## The problem
I was running Ubuntu 16.04 (and 17.04 I think, but I haven't confirmed this in a while) and the latest version of Firefox, with the up-to-date RescueTime plugins and desktop app. At the end of the week I would get my weekly report and it would show hours-and-hours of time spent on "Firefox", and no time spent on any websites. Firefox was marked "Not Productive", so my weekly report always had a ton of "red" on it.

For me, this was a problem because as a software developer I spend an outrageous amount of time using a Firefox: I'm going to Github, Trello, Jira, wiki's, etc. All of those are good and productive uses of my time. But if I go to gmail or twitter... well, I want to know if I'm spending too much time there. And the browser plugin was just not reporting that.

I contacted RescueTime support and we ran through some debugging. The end result was that something was preventing the browser plugin from talking to the desktop app (specifically, it couldn't make a websocket connection). 

I have a couple of privacy plugins going in Firefox, and I tried to whitelist everything I could, but we just couldn't get  anything to connect. (I'm also running a VPN, so there's was a thought that could be the source of the problem too.)

Eventually I had enough spare time I was able to do some more debugging and eventually I found a way to make it work!

## The solution
Here are the steps I used to get Firefox on Linux to report websites correctly:

1) Updated Firefox, made sure the plugin was up-to-date, and also updated the desktop app. Everything seemed to work for a day.  

2) Firefox was restarted, and then the problem (not logging sites that Firefox was visiting) started again.

3) I noticed on the apps page ([https://www.rescuetime.com/get_rescuetime](https://www.rescuetime.com/get_rescuetime)) that the "Last Data Sent" for the browser plugin was last week.

4) In the browser plugin, I unchecked the "I'm already using the full Rescuetime application on this computer".

5) Sites started being logged again, but I had a huge mark for "firefox" since it was counting the time twice.

6) I went and changed Firefox to be ignored. This removed the double entries but seems to keep the sites. (Which I'm ok with, I want to track the sites)

Doing step #6 is important because otherwise the weekly report would continue to show a huge red streak of "unproductive time". By marking the firefox app itself as something to be ignored, it is preventing the time as being double counted and allowing the actual websites to surface in the report.

So now at the end of the week I have a nice clean report of where I ~~wasted my life~~ did important computer related research.
