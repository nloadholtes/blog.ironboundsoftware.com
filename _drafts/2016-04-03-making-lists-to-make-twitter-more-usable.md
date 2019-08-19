---
layout:     post
title:      "Making lists to make twitter more usable"
date:       2016-04-03 13:17:56
categories: uncategorized
---
I'm a huge fan of twitter. But at the same time I can't spend all day sifting through random tweets, I've got to get things done! So how do I keep up with everything that's going on? Personally, I like to use lists. You can create a list and name it whatever you want, and add pretty much anyone to it. I like to make lists on certain "themes" and then add people to those lists who match the themes. Two of my favorite lists at the moment are 5 and Developrenures. (See my [previous post about how I then read the lists](https://ironboundsoftware.com/blog/2015/08/17/mosh-tmux-and-twitter-keeping-up-on-the-go/)) This is a great idea, but who wants to go through the people you are following on twitter and dump them into buckets? What if we could write a program to do this for us? 

## Enter the Python

There are several great python libraries for talking to twitter and for doing some text analysis. Lets see about combing those together to make something really interesting that can group the people while follow based on their tweets, and then put them into lists. Basically, lets cluster the people we follow on twitter! _Quick disclaimer: If you are following people who are pretty similar (e.g. football related, or python related) then you aren't going to see a lot of groups pop up. This method is really most useful for people who are following a diverse group of people, especially if there are a lot of them overall._ The first step is to
