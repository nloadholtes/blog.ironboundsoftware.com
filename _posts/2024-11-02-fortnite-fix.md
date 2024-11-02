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

My son was pretty sad when he realized he probably wasn't going to be able to cash in this gift card. I started thinking about it and realized if we were smart and careful, we could probably recover the missing characters and cash in the card!

## Examining the problem
So a Fortnite gift card is 24 characters. The font used to print them on the card is very readable, in fact there were other "missing" characters that were were able to figure out what they were because enough of the character was there. For example one missing character was a "4" and we could tell because the cross at the bottom right was all that was left of the character.

So