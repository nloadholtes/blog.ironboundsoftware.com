---
layout:     post
title:      "The curse of knowledge: Finding os.getenv()"
date:       2017-09-18 10:24:26
categories: python
---
Recently I was working with a co-worker on an unusual nginx problem. While working on the nginx issue we happened to look at some of my Python code. My co-worker normally does not do a lot of Python development, she tends to do more on the node.js side. But this look at the Python code lead to a rather interesting conversation. The code we were looking at had some initialization stuff that made my coworker said "Hey why are using os.environ.get() in order to read in some environment variables?" She asked “Why aren’t you using [os.getenv()](https://docs.python.org/3.5/library/os.html#os.getenv)?” I stared blankly for a second and said “huh?” I was a bit puzzled by this question because this developer is really good with node and also with Ruby. Perhaps they were thinking of a command in a different language and not Python I thought to myself. Together we looked it up real quick and much to my surprise I discovered there actually was a command there in the standard library called os.getenv() and it does exactly what you think it would. It gets a environment variable if it exists, and returns None (or a specified value) if it doesn’t exist. Using os.getenv() is a few characters shorter than using os.environ.get() and in the code we were looking at it just looked better. Since the code didn’t need to modify the environment variables, it just made sense to use it. But it got me thinking: I’ve been working in Python for a few years now, _how did I not know about this?_

## You don't know what you don't know

For me this was a real educational moment. It is very easy to think that we know it all, especially with things that you use day-in and day-out. But, you should never think that you know everything about a language even if you are an expert. There are people around you who, even though they might be experts in different languages or technology, still have something interesting to offer to you and your code. Have a conversation with someone who is either junior or senior to your skill level. Very quickly one of you will discover something new. For example, the junior person could discover a new approach to solving a problem. And a senior person can get a new perspective. [![The curse of knowledge: how I discovered os.getenv](https://ironboundsoftware.com/blog/wp-content/uploads/2017/09/Mr_Pipo_thoughts.svg_.png)](https://commons.wikimedia.org/wiki/File:Mr_Pipo_thoughts.svg)The second situation is one that I really identify with. As you become more "senior" in most things you begin to suffer from “[the curse of knowledge](https://en.wikipedia.org/wiki/Curse_of_knowledge)”. This means your knowledge advances to a point where you can no longer realize that something is beyond a beginner. The danger with that is that you develop a new set of assumptions about everything and you stop questioning things in the manner you used to. If you are not aware of this, it can lead to some nasty things. (Think arrogance, blind spots in the code/system, etc.) It also can lead to conversations that unintentionally intimidate others from participating in your development process in an effective manner. No matter how you slice it, this is a very bad thing. Having a second set of eyes, especially those that come from a different background, can really help surface issues in your code. That is always useful. In this case I was very fortunate and was able to get some insight into code that was working but perhaps a little bit inefficient. Now I have code that looks a lot better when it gets to the code review. 

## Learn from this

So, today go and talk with someone who has different areas of knowledge or experience levels than you. Something good will probably come of it soon.  