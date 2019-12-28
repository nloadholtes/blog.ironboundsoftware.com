---
layout:     post
title:      "Example of great documentation in Python"
date:       2017-12-11 09:04:37
author:     nick
categories: python
tags:  
permalink: /2017/12/11/great-documentation-python/
---
Documentation is one of those tasks and programming that does not get as much attention as it probably should. Great documentation is even more rare. We live in an age of unlimited free information in the form of blog posts and YouTube videos, but sometimes finding a simple example of how to use a library is one of the most difficult things to do. I ran into this situation a few weeks ago when I was trying to find a way to use sampling in a small concise manner. After a quick search online I found the Python 3 [random module documentation](https://docs.python.org/3/library/random.html#examples-and-recipes). 

## Great documentation just when I needed it

At the bottom of the page there is a section called examples and usage which shows a bunch of quick examples of how to use the library. The examples demonstrate various statistical operations (some of which I personally don't fully understand). It does this in a very short and concise manner that is very useful. The important thing is the one operation I was searching for was right there, and very nicely done.  Most documentation around topics like statistics tends to be pages and pages of dry academic math speak. It's refreshing to come across an example of something that is short and to the point. This documentation was so concise I was able to immediately apply it in my code. After getting it working I was able to show it to other people and explain what it was doing. As you write your code, particularly if you're writing library modules, be sure to think about not only explaining what your code does but including examples of how to use it. People who use your library will greatly appreciate this. Including comments on what the code is doing is really good but sometimes an example is worth a thousand lines of code. As you write your documentation, particularly if it is HTML, be sure to include anchor links in your document. This will allow search engines to get to the specific content more easily. It will also make your users very happy because they will be able to jump immediately to that section instead of having to dig through tons of text to get to the examples. _(You are writing documentation, right? If not, STOP reading this now, and go write some.)_ If you need an example of **what not to do** , look at the man pages that come with many Unix utilities. These man pages tend to include examples of usage, but they are often at the very bottom of the page. This is forcing you to search all the way down past pages and pages of test. It's good that the documentation is there but it would be better if it was more accessible. That's the advantage we have with HTML based documentation pages.

## Conclusion

Make your docs work as hard as your code does. Clear examples will make your code stand out in a good way. Great documentation is out there, lets make more of it. Here's what you need to create: 

  * A plain language explanation of what your library does
  * The shortest possible code example
  * A quick list of any common issues
  * Links to where you can learn more details

If you can create that for your code, you are doing a great service to us all.
