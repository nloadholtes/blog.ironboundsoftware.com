---
layout:     post
title:      "Comma Separated Values"
date:       2009-04-11 12:04:49
author:     admin
categories: productivity
tags:  
permalink: /2009/04/11/comma-separated-values/
---
Question: How much does python rock? Answer: More and more every day. Today I was writing (for what seems like the millionth time) a little script to read CSV (Comma Separated Values) file. After running into the same issues over and over (picking a delimiter, escaping delimiters, etc.) I decided my sanity is worth the 30 seconds it would take to see if someone else has already written a CSV library. It turns out python has one built in. Since 2.3. D'oh. 

> import csv lines = csv.reader('myfile.csv')

That's all that's needed to read in a csv file and have it properly handle the delimiters, even when they are inside of escaped text (i.e. something like "$3,000" will be read as $3000 instead of $3 and 000). Python rocks again.
