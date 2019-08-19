---
layout:     post
title:      "Cleaning up legacy python code"
date:       2017-05-01 08:12:51
categories: python
tags:  
permalink: /2017/05/01/legacy-python-code/
---
Python is growing in popularity which is a great thing! And with that growth we now are seeing more and more legacy python project. Occasionally you are going to inherit one of these "legacy" projects. Here's some tips on how to get it under control. 

## What is a legacy project?

Over the years I have heard lots of definitions of what a legacy project is. Here's a few of the gems I've heard used to describe these projects: 

  * An "older" project that has been around forever
  * A code base without any kind of tests
  * The project that no one wants to work on
  * "Everyone who worked on this left the company years ago..."

And sometimes the code isn't old. A lot of times a project will be done real quick and put into production before everyone realizes that there's a better way. (e.g. using a different framework) By the time that happens the "legacy" project is doing an adequate job and management is afraid to touch it. This is a pretty legitimate concern to higher ups in a company: _"If it ain't broke, why try to fix it?_ " So, what are the best things to do with a legacy project? 

## Make sure it is in version control

Before you do anything, make sure the project is in some kind of version control system. Too often I have seen "proof of concept" programs that were thrown together and pushed into production without any thought given to making sure that the code was somewhere safe. This is doubly true if the code is anyway important to business operations: You do not want to be the last person who was seen with the only copy of the code. If for some reason this project is not in git/subversion/etc. put it in there NOW. If your company doesn't have a version control system, beg your manager to[ invest in one ASAP](https://gitlab.com). 

## Delete commented out code

Once a project is under version control, one of my favorite tasks is to delete any commented out code. The older the code base the more commented out code there tends to be. I'm not talking about 1 or 2 lines here and there. I encounter dozens to hundreds of lines of code commented out on a fairly regular basis. Commented out code is a waste of cognitive time. New developers (like you) who look at the code will see all of that code and try to understand why it is there but hidden in a block of comments. In my experience it is there because something in the project changed and someone is hedging their bets that the old code will be needed again. So it gets commented out and then haunts the code base forever and ever. Once the code is under source control, the fact that it got deleted will be recorded in the repository. If for some reason it becomes necessary to revive that code, any developer on the team can go and revisit the commit history and pull out just what is needed. ( _ **Spoiler alert:**_ Most of the time you will never need that commented out code.) 

## Running tests/adding tests

Now that your legacy python project is under version control, we can start do some more interesting things. One of the first things I like to do is to try and run any unit tests that might be there. 

> A WORD OF CAUTION: Sometimes a project will have unit tests that aren't quite "unit" tests. In other words, beware of any tests that might reach out and talk to a live system. I was bitten by this recently when I ran a set of unit tests that were doing destructive things to a _**production** cache_ system. Thankfully we were able to recover it quickly, but I still get grief about it every few weeks.

If there are no tests, this is a great time to add some. Most bosses are cool with test because they usually don't impact the existing code. Of course, check first before you add anything. As you are running the tests, consider using [coverage.py](https://coverage.readthedocs.io) to see how well the code base is being covered by the tests. If there are any "critical" spots where the tests aren't hitting, those should be the first spots you should write tests for. 

## Pylint/vulture

Something to consider doing at this point is running some type of linter over the code to see how "healthy" it is. A [linter](https://en.wikipedia.org/wiki/Lint_\(software\)) is a bit of software that examines code and looks for anything suspicious or "wrong". [Pylint is a great python specific linter](https://ironboundsoftware.com/blog/2016/12/05/improving-your-python-pylint-and-flake8-emacs/) that can look at python code and offer some suggestions. By default pylint is pretty verbose and will flag all kinds of things that might not really be that important (such as lines longer than 79 chars). There are ways to control the output, and you should check here for more information about that. So what should you look for in the pylint output? Personally I like to look for: 

  * Unused variables
  * Anything that is notes as a potential bug

If this project is going to be worked on, then these are things that you probably should consider fixing them as you add features. Removing unused variables is no brainer. It reduces visual noise and helps developers reason with the code. Things that are flagged as potential bugs: These need to be handled carefully. Sometimes the code is working in spite of the bug. 

## Flake8? Not so fast!

Since I've mentioned pylint and it's awesomeness, I should also mention formatters like pep8 or my favorite [flake8](http://flake8.pycqa.org/en/latest/user/index.html). These tools can be used to reformat python code to make it more pep8 complaint. While this is normally a good thing, _I don't recommend doing this on a legacy project right away._ My reason for saying this is because if the code is working (especially if it is in production) any changes made to it should be minimal so that you preserve the code as it is. While most of the time the tools will not modify the code in any destructive way, I have seen strings that were too long get mangled a little bit. This can lead to confusion about what the line was actually doing. My personal approach would be to have unit tests in place first, and then apply flake8. Also, if you are developing new feature to add to the code base then you should be using flake8. 

## More idiomatic python

By this point you probably have a really good grip on your legacy project. Depending on what the future holds for the project (new features, or just maintenance) you might want to consider revisiting some of the suggestions from pylint. One thing I have seen pop up in legacy code projects is code that is "unpythonic". This includes things like badly formed for loops, checking if "something == None", and other spots where things could just be more idiomatic. This is a topic I really enjoy learning more about as I feel I am still learning the true way. If you would like to learn more, I highly recommend reading [Effective Python](http://amzn.to/2pwAsyN) as it is full of great examples of pythonic coding techniques. 

## Wrapping up

With the exploding popularity of python we are now starting to see more and more legacy python projects. Thanks to some basic tools and the beauty of the language itself, this doesn't have to be a scary proposition like it is with other languages. _Java, I am looking directly at you._

* * *

#### **_Pssst... Quick favor?_**

I'm putting together a course on Debugging Python code. If you want to get in on this, sign up below to learn more! 

## Sign up to learn more!

Your best email address *

First Name 

Last Name 
