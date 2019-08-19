---
layout:     post
title:      "Debugging like Elon Musk"
date:       2016-10-10 10:25:05
categories: productivity
tags:  
permalink: /2016/10/10/debugging-like-elon-musk/
---
Every time I think I'm doing pretty good with my projects, I take look over and see what Elon Musk is doing. Then I instantly feel like I'm wasting my life. That guy does such huge things and he does them so quickly it is mind boggling. What is his secret? Can I be like that? The answers is yes, if you use "First Principles" reasoning. I have found that when you apply first principles to debugging software that you will get to better solutions. So what is first principles? Here's Elon explaining the how and what of it: [embed]https://www.youtube.com/watch?v=NV3sBlRgzTI[/embed] So here's the take away: 

  * What is the most fundamental truth or truths in this system?
  * Build up from there

Pretty simple huh? Let's walk through an example where we debug a computer program. 

## Debugging with first principals

Here's scenario #1, "Dude, where's my page?". Say you have a [flask app](http://flask.pocoo.org/), and you are trying to add in a new page to show off your latest feature "Self driving cars". But when you visit the the URL  ** _http://example.com/self-driving-cars_** you get a 404 error in your browser. WTF? Here's what the code might look like:  Let's tackle this with first principals reasoning: 

  * Is the program running?  _Yes, otherwise we wouldn't get the 404 because nothing would be served up._
  * What do the error logs say?  _404, page not found. Duh!_
  * Is there a route for the URL "self-driving-cars"?  _Uhhh, whoops. It is "self-driving-car"_

That is a very simple example, but it illustrates the line of thinking that we need to use. Start with the basics, even if they seem painfully basic, and make sure those are "true". Then build up from there. I'd strongly urge you not to skip out on these basic steps. I've found that most of the time you can run through them pretty quickly, and when there is an error in that layer you do tend to surface it pretty quickly. 

## Complexity? Break it down!

Let's think about a more complex situation. Scenario #2: "The page is blank" In our [flask app](http://flask.pocoo.org/) we have a page that is supposed to display the inventory of our electric cars at our dealerships. But when we visit the page to see how many cars are at the Atlanta dealership, the page is blank. What gives? Debugging with first principals to the rescue! Let's try this without even looking at the code. 

  * Is the program running?  _Yes, we get a page, its just blank._
  * Is the database running?  _Yes_
  * So the page is sending a query to the database, and the database returns data to the program?  _Hmm... I see the query being made, but an empty set comes back. There should be a data in here!_
  * Interesting! Is the query correct? Check to see if there is data in the database.  _Yes, there are entries in the tables. The query looks correct. It looks like there is no inventory for that particular dealership. They must have sold out all of the cars._
  * So is the program supposed to display a different message to the users?  _Whoops! It looks like there's a bug there: When there are no results from the database we are supposed to display a "Sold out" message, but the if statement was coded incorrectly...._

Boom. Problem solved.  [via GIPHY](https://giphy.com/gifs/mQG644PY8O7rG) In this scenario we had the possibility of a bunch of different systems having problems. The flask code, the database, the network, permissions... anything could have contributed to the error. But by breaking it down to the first principals we were able to get to the expected "truth" for each step of the process. Debugging with first principals can help save a lot of time while helping you narrow in on the root cause of the problem. 

## Other applications of first principals

This is also a great way to think about your unit tests for your code: by testing each individual function, you can build up to a bigger truth. Notice I didn't say anything about correctness, but rather truth. I have seen too many unit tests that were consistent when it came to how they handled data, but were incorrect in that they were testing the wrong situations. Take scenario #2 for example: The unit tests might have always focused on the query returning data. Or if the query returned no data, the test only checked that a page was displayed, not that it was displaying a message about being sold out. By stepping through the code with first principals we get to the correct version of the truth, not the truth that the unit tests were displaying. 

## Wrapping up

Debugging with first principals is a powerful tool to add to your repertoire of skills. Use it to get down to the root of your problems faster!
