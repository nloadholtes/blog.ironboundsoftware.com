---
layout: post
author: Nick
title: Fortnite giftcard fix with Python
date: 2024-11-02
categories: python
tags:
  - python
summary: Using Python to help my son fix his Fortnite gift card
---

My son got a Fortnite gift card recently, and in his excitement to cash it in he scratched too hard and rubbed off some of the characters. Because it was a gift, we didn't have a receipt so I was concerned that customer support might not be to help us.

![[2024-11-02-pin-redacted.jpg]]

_I've redacted the whole PIN to help us focus in on the first 4 digits._

My son was pretty sad when he realized he probably wasn't going to be able to cash in this gift card. My wife tried contacting the friend who gave us the card, we weren't sure they would have the receipt either.

I started thinking about it and realized if we were smart and careful, we could probably recover the missing characters and cash in the card!

## Examining the problem
So a Fortnite gift card is 24 characters. The font used to print them on the card is very readable, in fact there were other "missing" characters that were were able to figure out what they were because enough of the character was there. For example one missing character was a "4" and we could tell because the cross at the bottom right was all that was left of the character.

So my first thought was we can just try the combinations for those two missing characters. My son had tried that though, and had no luck. I tried to explain to him that manually typing in things was a very error prone process, but he wasn't having any of my fancy explanations.

So I said "Let's write a program to help us out".

## Phone a friend/AI
After asking [Claude](https://claude.ai) what the characters were (it couldn't figure it out, and actually mis-read some of the other characters!). So instead I asked it to make a Python program to generate all strings that could be in those 2 spots.

A split second later I had a really short nested loop that would generate all of the possible combinations, and surely our pin would be in there... right? Kinda.

This initial program generated all `36**2` combinations, which is almost 1,300 different pins! The good folks at Epic/Fortnite would not like me just trying all 1,296. Since you have to be logged in to redeem a card, I was sure they would probably ban our account long before we got to the right pin.

So, how do you reduce the problem space?

## Looking harder
So a pin for these gift cards seems to be the (capital) letters A through Z, and the numbers 0 to 9. And there seems to be 24 characters per pin code. So that is 36 raised to the 24th power which has 38 digits. That's a huge number!

> Side note: There are some letters that might not be in the set of possible letters. For example, it can be hard to tell the capital letter O from the number zero (0). But for this problem even if we eliminated I and O, we would still be looking at 34 different characters per position which is a lot. Especially when we don't know where the "you've tried to many" limit is.

They use large numbers like that to help keep people from guessing the code and getting free stuff. Thankfully we only need 2 characters. Are there any hints on what these characters could be?

I used my phone and a bright light to zoom in and take a closer look.
