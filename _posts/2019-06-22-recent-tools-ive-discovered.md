---
layout:     post
title:      "Recent tools I've discovered"
date:       2019-06-22 10:15:46
author:     nickadmin
categories: programming,tools
tags:  
permalink: /2019/06/22/recent-tools-ive-discovered/
---
Every now and then I come across a new software tool that makes me stop and say "How in the world have I made it this far without this?!??" Today I'd like to talk a little bit about some recent discoveries, maybe they can help you too! 

## I no longer ack, I ag

I'm a long time lover of grep. When I was first introduced to it I thought it was pure magic. For _YEARS_ grep was my go-to tool for any kind of text searching. A few years ago someone showed me `ack` which is advertised as a better/faster grep. It took some getting used to, but I pretty quickly decided that it was pretty impressive. Especially as I started working on larger codebases. Its speed combined with the colorized output won me over and it became my standard text search tool. But... there was also another tool that was claiming to be even faster than `ack`. This tool is called [`ag`](https://github.com/ggreer/the_silver_searcher) (also known as "[The silver searcher](https://github.com/ggreer/the_silver_searcher)"). In my first tests with it (years ago) I found it to either be the same speed or slower than `ack`, so I never really paid much more attention to it. 

### Enter a huge codebase

Eventually I wound up working on an enormous codebase that was peppered with a bunch of different languages and data formats in it. With this new project I quickly discovered that `ack` would bog down and take a long amount of time to return results on my searches. Since it had been a while, I decided to try out `ag` and see if things had changed. Oh my, things have changed. `ag` is **BLAZINGLY** fast for me on this massive application. It took me a few days of concentrated effort to force myself to type `ag` when I did searches, but with every lightning fast results I found myself loving it more and more. It is now my default tool for searching text. It is awesome. **The lesson here:** Try out new tools every so often. You'll be surprised that sometimes there's better solutions out there, and don't be afraid of the learning curve! If it improves you daily workflow, it is worth investing some time to get it setup and into your skillset. 

## Instead of cat, use bat!

Speaking of new tricks, I'm intrigued by the language Rust. I'm not quite ready to learn it (I have no good use cases for it at the moment), but I did discover a utility that is written in Rust that is very awesome: The paging utility [`bat`](https://github.com/sharkdp/bat). A paging utility is a program that can show one screenful of text at a time. Most people use something like `cat` or `less` for this. If you are an unfrozen caveman such as myself you might use `more`. At any rate, `bat` is a new take on these utilities and is incredibly beautiful to use. Screen fulls of text can be pretty plain, and if you are looking at something like json, xml, or yaml files it can get kinda confusing quickly. `bat`can recognize certain file formats and apply syntax highlighting rapidly so you see something resembling what you would see in your IDE. I like syntax highlighting so much that I decided to alias `more` to be `bat` so that I'll use it when ever I need to look at file, `bat`will try to interpret it for me to make it more legible. For all my raving about it, I have had some relatively minor problems with `bat`, specifically with very large files or certain extensions I've found that `bat` can run really slow. Thankfully these are few and far between and the developer of the tool has been very helpful with troubleshooting these issues. 

## Chat everywhere with weechat

IRC is one of those technologies that I've alaways felt like I should be more into. I love text based chat programs. Over the years I've used ICQ, AIM, Yahoo, gChat, and now Slack. But for some reason IRC just never really stuck with me. Well thanks to [weechat](https://weechat.org/), I've now got an interface that I can use that makes IRC more usable. Color coding, a good layout, and the ability to write plugins make weechat a joy to use. One of my favorite uses of weechat is to put certain Slack groups in there. This way I can keep an eye on them without having to to load them into my desktop Slack app (or open yet-another-Slack-tab in the browser). I'm not doing a good job of explaining why this is so awesome... I think it comes down to reformatting. Slack has a lot going for it visually, but sometimes I just need something similar. As in less flashing emoji or animated gifs. Weechat does a good job of condesning these messages down to a more simpler format (just colored text). One powerful advantage of weechat and Slack: You can have multiple threads open at once, and have them split across different window panes in the UI. Slack doesn't let you do that, and honestly most of the time you wouldn't want to do that. But... when you have one of those times where there's 2 important conversations going on (or god forbid you are being @ mentioned in multiple spots at the same time) it is _really_ useful to be able see everything going on at once. 

## Next level weechat: Glowing Bear

For a while I've thought that to support my desire to get more into IRC I would need to setup a bouncer like ZNC and everything else to support that. Long story short, I wasn't winning that battle. I had one setup for a little bit, but failed to backup my configs and when I had re-setup everything it proved to be too much of a pain in the ass. Recently I discovered a project called [Glowing Bear](https://www.glowing-bear.org). At first I thought this was another client/bouncer, but then I discovered it is actually a clever way to interface with an existing weechat session. It basically turns your text-based weechat into a living webpage! (Think of it as accessing a slack group via a web browser vs the Slack app.) Because of the effort I had gone to in setting up weechat the way I wanted, this seemed to be something worth trying. And I was so happy I did try it, because it is dirt simple to use, and look **ABSOLUTELY BEAUTIFUL.** It can display tweets and images inline (and collapse them back!), and it is fast and responsive and just plain looks good. It also works great over a mobile phone connections (its just a simple webpage), so now I can access my IRC and Slack conversations on the go, just like I can at my desk. That's really awesome. And the best part? I can cut out the ZNC middle man and just have it talk to weechat! Simplicity! 

## Final thoughts

Every year you should take a look at the tools you are using and ask yourself "Is there a better way of doing these things?" and spend a little time investigating. I'm not saying through out your tools, but you should look at them make sure they are as sharp as possible. And if they are dull, go find new ones.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgyNDUxMTU4M119
-->