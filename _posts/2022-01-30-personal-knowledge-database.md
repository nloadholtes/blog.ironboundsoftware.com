---
layout:     post
author:     Nick
title:      "Person Knowledge Database"
date:       2022-01-30
categories: thinking
tags: thinking
summary: Taking note of taking notes
---

Over the last few years I've been working more on taking notes. Between work and home, we are inundated with tons of information. Not all of it is important enough to be remembered, but the pieces that should be are usually critical. I've spent some time investing in keeping track of my knowledge and I thought I would share some notes on this.

## Why take notes?
The older you get, the more you see. And the more you see, the pickier you get about what you want to remember. So, especially at work, write it down. There's almost no way to be sure in the moment what will be important down the road. If its recorded somewhere then you can search for it in the future. 

As an example, a co-worker needed to know an ID that we had used in a test run... 14 months ago. No one I know memorizes hex numbers, so this is a prime use case of looking it up in the knowledge base.

## Core values
So with that in mind, I have some core values I want to respect with my technology choices.

1. Open, future proof format -- Plain text is about as open and future proof as possible, so this made sense. Markdown is my preferred markup language and even with its variations I think that in 20 years it will still be able to fulfill #2 and #3.
2. Easily searchable -- Plain text can be manually read through, grep-ed through, or loaded into one of a million different search engines quite easily and with minimal translation.
3. Portable data -- The programs I use to take the notes are secondary to the notes themselves. Therefore, I want a copy of the data in multiple places for backups and preservation.
4. Not being tied to a vendor -- I'm tired of a company going out of business, or changing the terms of use and me getting locked out. My tools should work for me, not the other way around.

There's a million tools out there that can hit these 3 pretty easily. From that point forward everything becomes a matter of preference.


## Best tools
Emacs is where I started. With tools like org-mode and markdown-mode I can generate text files that are portable and searchable. Emacs has a legendary learning curve, but I was already familiar with it so learning a new mode was all I thought I needed to do.

After several months I transitioned from using org-mode to just plain markdown-mode. There's nothing wrong with org-mode, it just works best when you conform to its way of doing things. I gave it a good try, but in the end I wanted something different from my tooling, so I switched to markdown-mode.

My note taking flow got simpler in that I no longer had to conform to the org way of doing things. Because of the text-based nature of everything, this switch over was really painless: I can still manually scan my notes or use grep to do a deeper search.

For portability, I'm using git. By making the editing tools use plain text, the files become like any source code file that git would normally version. Combine this with a periodic cron job to commit the changes, and you've now got the ability to version your notes, and a large ecosystem of tools to help with backing up and distributing them (a la GitHub or GitLab).

Recently Obsidian has come to my attention. I tried it out early in its development, but it just didn't feel quite ready at that time. Now a year later it feels really good. I've now switched from emacs to Obsidian as my daily note taking tool. Since Obsidian understands markdown and files, I can keep my underlying git infrastructure in place.

## Why not...
In this space there's a ton of choices. This all deeply personal, but I thought I'd share some other tools that I looked at a decided against using.

* **emacs/org-mode** - A great desktop tool for doing everything. But using it on a mobile device? No thanks. Plus I think with things like org-mode you have to give yourself over to the tool a bit more than I would like. For example, I would love to use org-mode but with Markdown syntax. *
* **roam** - A big mindset shift combined with the need for connectivity made it hard for me to use this one. I know some people really like it, and there are some really great ideas in there that are leaking into other apps, but this just isn't for me. *
* 