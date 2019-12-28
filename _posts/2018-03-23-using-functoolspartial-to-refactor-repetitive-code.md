---
layout:     post
title:      "Using functools.partial to refactor repetitive code"
date:       2018-03-23 17:10:25
author:     nick
categories: python
tags:  
permalink: /2018/03/23/using-functools-partial-to-refactor-repetitive-code/
---
The other day a friend made a comment about iterative development and it got me thinking. In some situations this is a good approach to get things going, but there is a dark side to it: Crufty nasty code. Functions that we are fear to touch. Code that screams out to for a refactoring. It got me thinking about the code I hacked together for [Remote Matcher](https://remotematcher.com). It's shiny and new, but does it have a dark side? 

## How bad could it be?

For this project I developed "iteratively", and I decided I needed to stop and see what shape the code was in. In my `views.py` file, it definitely needed some attention, and not just because there were todo comments saying "THIS IS TERRIBLE. PLEASE CLEAN IT UP". (I literally put that in the code. Twice.) Here's a quick enumeration of the sins of this code: 

  * Repeated strings (like, we check for a string, then go and use that string again on the next line)
  * A bunch of `elif` statements that grows every time a new data source is added
  * There are several long constants that get `import`'ed (and they will grow every time a source is added)
  * The same 2 functions are called over and over, but with slightly differing parameters
  * Although this file is called `views.py` it sure looks like there's business logic that's starting to leak into the functions... even though we have a dedicated module that is supposed to handle that logic!

And that's in just 25 lines of code. 

## facepalm.gif

Clearly things need to change. I have 2 new sources I want to add to the system and the thought of that causing that function to grow  **at least**  4 lines really made me mad. The strings could be consolidated, but that wouldn't help with the leaking of logic, or the growth of the `if` statement. Usually I'm ok with a little bit of repetition in code, but at this point we clearly spiraling out of control. I kept thinking if I could get this code into a `dict` and then do a lookup I could probably help get this code under control. As I thought more about this I had a flash of insight: I could use Python's `functools` module to help with the function invocation! I decided to take a swing with the approach and it worked! Rather than try to explain what I did, I made a video showing my approach. Here's me walking and talking my way through this refactoring: 

## Parting thoughts

Although the total line count didn't go down tremendously in the video, the code in the `views.py` file is on the path to getting more streamlined and having less of business logic laced into it. The root cause of this was me hacking on it to "just get it working". Since I knew I was going to have 2 similar but different data sources I didn't put a lot of thought into "correct" software architecture principals early on. Thankfully I revisited this code before it got too nasty. So, the moral of the story: revisit your code and look for opportunities to simplify and consolidate things. That and Python's `functools` module is pretty awesome! A lot of things like [partials](https://docs.python.org/2/library/functools.html#functools.partial) sound like magic, but when you need them they work perfectly.
