---
layout: post
author: Nick
title: Vibe Coding Review
date: 2025-03-12
categories: programming,ai
tags:
  - building
  - programming
  - ai
summary: I tried making a game by using the power of Vibe Coding
---
Vibe Coding is a new fad that is sweeping the programming world. Basically it is letting an LLM AI (like ChatGPT or Claude) write an entire program via prompts. You as a developer never really look at the code it produces or try to understand it, instead you guide it via "vibes". But can this really work? Is this the future of software development?

As I write this the most visible example of this is [Pieter Levels' flight simulator](https://fly.pieter.com). Pieter simply asked ChatGPT to write a fight simulator that would run in the browser. He did this as a reaction to the bloat that is in a lot of games these days: Large downloads that are needed to "patch" the game on an almost daily basis, long load times, etc. 

The game that was written will never be mistaken for a "professional" game. Blocky graphics, clunky physics, and a multiplayer experience that is... well it reminded me a lot of the early internet (e.g. security holes, but a lot of fun). But at the end of the day the game was shipped incredibly fast (less than a week), it is making money via ads (over $80k per month!), and Pieter didn't have to become an expert on the code but was still able to iterate and add new features.

And this is where Vibe Coding shines, the ability to just do things. A lot of programmers are opposed to this style, they claim that one must understand what is going on under the hood in order to make sure the right choices are being made. They point to the XSS and multiplayer bugs in Pieter's game as the prime example of not understanding. They are not wrong, but they are missing an important point.

Quick iteration is something that separates so called 10x programmers from mere mortals. Those that can try out an idea quickly are the ones who seem to be able to win the day. If they hit on a bad idea, they find out sooner and change course. Regular programmers tens to get bogged down either trying to make it work, or trying to figure out the optimum solution.

Being a regular programmer who wants to improve, I decided this was something I should try to get better at iterating quickly.

This past weekend I decided to vibe code up a game to exercise this muscle. One of my favorite games is an RPG from the late 80's called [Wasteland](https://www.gog.com/en/game/wasteland_the_classic_original). It is a low-resource game for modern machines so it would be perfect to implement it in Javascript (a language I am not nearly comfortable enough with). The [code](https://github.com/nloadholtes/valley-escape-rpg) and the [game](https://valley.ironboundsoftware.com) if you are interested

The experience was interesting: I got up and running very quickly. Going back and forth with Claude we quickly a v1 up and running of the basic UI. I tried not to look at the code beyond a few broad strokes, and instead relied on Claude to fix the issues as I found them via playing the games.

At this point things got interesting... My initial prompts where ok, but they missed a lot of nuances that quickly came up as I tried to do things in the game. Thankfully I quickly asked Claude to split the game into 2 files because it was clear that I could cut down on the amount of code back-and-forth by isolating the trouble spots. Especially when I found it was breaking the working code while trying to fix the bugs.

And in real life this is what I would have done if I was writing this. And this is also what I've been telling people about using LLMs. If you do a good job of decomposing the problem and breaking it down into small chunks, your LLM is going to have an easier time.

For me this is where one has to be smart when it comes to vibe coding. Doing the ideation and getting up and running is a great thing to do with an LLM. But at some point things will get too complicated for the LLM to sanely handle. Before you get to that point you need to step in and start applying some software engineering best practices.

For me this would look like:

* Breaking the codebase into files/modules based around functionality
* Identify which functions are starting to have problems
* Concentrate on learning what the code is doing in those areas
* Ignore parts of the codebase that are "working normally"

Learning what is happening in the trouble spots is important. Just like with a human programmer, this is where the definitions or specifications are weakest. By understanding what is trying to be accomplished here, you can help guide the LLM to a more correct solution, either by editing the code or by prompting.

This is a good thing! We are still iterating quickly, finding a dead end in our knowledge, exploring an isolated area, and then moving forward to repeat the cycle.

I know many programmers who love to complain that other programmers "don't understand the code they are using", but I also know the dirt secret... Most programmers don't know/care to look at the libraries they are using because they trust it to work. Which to be fair it usually does.

Do programmers run into trouble because they don't fully understand 100% of the code they are using? Absolutely. All day, every day. Does that mean they should not be coding? Absolutely not. No software is perfect, bugs are always present.

So the secret to success with vibe coding is to only let it take you so far, and then you need to take the wheel. Treat the process just like you would working with a junior programmer: Let them get going, but do frequent check ins to make sure the train is still on the tracks.

Back to my game... I was not planning to do a whole re-creation of the original game, so after an hour of struggle to get the basic combat working I decided to call it done. I had positive vibes from the experience and most importantly, I had fun coding. And it had been a little while since I'd experienced that.

And isn't a positive vibe all that we really want?