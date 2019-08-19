---
layout:     post
title:      "Pickle Danger!"
date:       2009-01-11 19:17:43
categories: python
tags:  
permalink: /2009/01/11/pickle-danger/
---
I've been poking around with a little python based web crawler/robot/scrapper that I've written. Its a pretty simple script and over time I've added little bits and pieces to it in order to try improve, etc. etc. etc. One thing I added was an ability to track the URL's I've already visited. Trying to be a polite, I decided that this was a good thing to keep from hammering the same web sites over and over needlessly. Basically, I put the address into a dict, and then after a successful visit to the address I set the value of the address to 1. (This way I could collect addresses, but no visit them right away, but always make sure I got back around to visiting them. Or if I needed to visit them multiple times I could keep track of how many times I'd been there.) Python provides a really simple way of serializing data by using the [pickle module](http://docs.python.org/library/pickle.html). Just open a file, then call the dump() method with the file and the data as parameters, and boom, all done! Going in reverse and reading serialized data is just as simple. Except..... What happens if there's an exception thrown in your code? (Bad URL, unicode that you're not prepared to handle, network down, etc.) And what happens if this happens to occur while it is trying to dump the data your interested in? Well friends, I can tell you: It ain't pretty. Because I had already called file() on the data file, the old data was gone. *poof*. Since the new data was being written out when the new the problem occurred, the new data file was corrupted. There are several lessons that can be learned from this: 

  1. If you are going to re-use a program/script more than once, go ahead and build it right.
  2. If you are going to write out data make sure it is either a) Backed up first (i.e. write to a different file first, then after the file is closed successfully, overwrite the old one) b) Written to something like a database which is designed to not get corrupted at the drop of a hat

And as a bonus tip: You should always back up code (and data) that you generate. As I said, this was a quick-and-dirty program at first, but it had obviously grown in it scope and importance. My new metric for "needing to back this up" is if I have checked the code into a repository: If you are willing to check in the code, you need to save the data (config, output data, etc.) as well. Fortunately I didn't loose that much or anything that was earth shattering. But all it takes is one time...
