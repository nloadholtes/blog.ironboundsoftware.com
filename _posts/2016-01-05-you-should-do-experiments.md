---
layout:     post
title:      "You should do experiments"
date:       2016-01-05 05:12:50
author:     nickadmin
categories: statistics,web
tags:  
permalink: /2016/01/05/you-should-do-experiments/
---
Over the last few years I've learned that it is one thing to have a good idea, and it is something completely different to have an idea that someone will pay you for. Sadly the overlap between these two can be pretty small. But, there is a way to enlarge the overlap: find out what your customers really want and then give it to them. The best way to do this is with controlled experiments. 

> Please note that actually solving a problem a customer has is a really great approach also, and probably should be your first step. This post is going to work with assumption that someone (your boss) has already done that leg work and you are just trying to get more people using your solution, or to make them happier.

An experiment is a slight change to your app or website that is measured. If the thing you are measuring (time on the site) goes up, then the experiment should be considered successful and put into use. If the measurements go down, then the experiment should be discarded or modified and retested. So what is a "slight change"? Typically it is something like the color or position of an element on the screen (like the "buy" button), but it can also be text that is used to drive certain behaviors from the users. A perfect example of this is the text that is on a "buy" button on an e-commerce site. In the not-to-distant past, most websites had a button that said "Submit" that was clicked when the user wanted to buy something. That isn't the most enticing turn of phrase to get someone to hand over their money. If someone was on the fence about purchasing a product, seeing the word "Submit" didn't really give them any motivation to click the button. Ok, so if that isn't a friendly word, then what is? In pretty much any office you'll probably get 10 opinions on what that button should say. But those 10 opinions are just that... opinions. At the end of the day all that really matters is what phrase causes people to click on that button. So this is the perfect experiment: Gather up your phrases, and then try them all out. The one that gets the best response is the one you should go with! Well, that's the high level view. The more concrete steps would be: 

  * Set up an A/B testing framework in your code
  * Add the choices to the framework so that it will randomly (across all of your users) show those choices to customers
  * Sit back and let a  **statistically significant number of user** use your app
  * Once you have had enough users hit that particular test, look at the results. Hopefully there will be a clear leaders and losers
  * Pick the winning choice and start again with new choices

The idea here is that you are letting the customers vote with their actions: They don't know they are being tested, so their actions should tell you something. For example if you offer two choices, "GIVE YOUR MONEY NOW" and "Let's do this!", you should see a pretty significant difference between the number of clicks. The first one... well its what you want to happen, but it doesn't mean people will do it. The second one is more fun and light hearted. Depending on your app, you might find that you customers respond very well to certain phrases, and in that case you should then try to use that language at every important decision point in order to get the customers to... well, give you money. :) Some other things to keep in mind with experiments: 
  * **Statistical significance** : You need to have a certain number of people look at your test, and a certain number of those people go one way (or the other) before you declare a winner. Use a website like [Evan Miller's Sample Size Calculator](http://www.evanmiller.org/ab-testing/sample-size.html) as a starting point to determine what kind of numbers you might need. (His site has other very useful statistics calculators, be sure to check them out!)
  * **Limit the number of choices** : Earlier I mentioned 10 different choices. Unless you have a large number of users, I would not recommend testing all 10 out at the same time. Instead I would do something like a tournament bracket. Rank your choices and then pick the first 2 or 3 and let them duke it out. Let the winner then face some of the other choices in a later test.
  * **Why not just ask the users?** Directly asking the users might not always be the best way to find out what they really want. What people think they want vs. what they really want are usually two different things. Experiments allow you to discreetly find out what the users really want (or respond to).

This type of testing is the key to success in the field of advertising. Over the last few decades the professional marketers have been using this technique to determine the absolute best copy to use in their sales ads. (If you look closely at ads from different companies you will notice that there are a lot of similarities.) If this is working great for them, then you should definitely be doing it for you app too! Experiments are a great way to peek inside of your user's thought processes. In future posts I'll detail some ways I've used experiments to determine how to best change my apps and sites in order to get better results.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzgyNzgwMDM1XX0=
-->