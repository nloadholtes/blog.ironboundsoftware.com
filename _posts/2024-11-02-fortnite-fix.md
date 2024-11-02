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

> Side note: There are some letters that might not be in the set of possible letters. For example, it can be hard to tell the capital letter O from the number zero (0), so it is totally possible that they aren't using those. But for this problem even if we eliminated I and O, we would still be looking at 34 different characters per position which is a lot. Especially when we don't know where the "you've tried to many" limit is.

They use large numbers like that to help keep people from guessing the code and getting free stuff. Thankfully we only need 2 characters. Are there any hints on what these characters could be?

I used my phone and a bright light to zoom in and take a closer look.

![[2024-11-02-first-4-zoom-zoom.jpg]]

The font that was used on these cards is a huge help: it tries to be unambiguous about what the character is. For example, the 5 and a capital S do not look alike. So because we have some partial marks in the red and blue squares, we can made some educated guesses.

Let's start with the easy one, the blue square. It looks like it could be a U, or maybe even a J. In the rest of the pin that I redacted we had some other example of characters that has a similar shape like the number 0. We felt pretty confident we could eliminate a bunch of "impossible" characters and reduce the size of our search space from `36*36` (1,296) down to `36*2` which is only 72. Progress!

The red box was a little more challenging. We were convinced at first that it was a "4". But we had a 4 elsewhere in the pin and saw it had a different shape because it was angled. Also, that horizontal piece looks darker than the other lines, and is angled slightly differently. Could it just be part of the letters that were scratched off? 

We went through the alphabet and numbers and narrowed it down to 11 that we thought it could realistically be based on the shape. This is what we wound up with:

```python
possible_a_chars = "5BDEFHKLPRU"
possible_b_chars = "JU" # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

Which is 11 and 2, or 22 possible combinations. Much better than trying 1,296 we could manually try this quickly. I did add a `random.shuffle()` to mix up the numbers a little bit, I was concerned if we looked like we were trying them in order that the system might ban us sooner.

So with my shuffled list of 22 I logged into my son's account and tried them one by one... and on the 18th try it worked! That sounds like a big number but it only took me about 3 minutes to get to it. So pretty quick overall!

It turned out the missing characters were `KJ` which now seems obvious when we look at the card, but at the time we didn't see that.

So, in the end my son got to see:
* How to analyze a problem
* 2 different unsuccessful approaches to solving it (manually, asking the AI to analyze the image)
* A simple python program to generate the combinations
* How to reduce the scope of the problem with a better heuristic rather than brute force guessing

But all he probably cares about at the moment is that he has a bunch of V-Bucks that he can now spend in Fortnite.

---
## So where's the code?
I'm publishing this code kinda incomplete. I don't want to just hand everyone the complete code because if you try and run through all combinations (e.g. you are trying to get free V-Bucks) **you will get banned.**

So here's a Python function that demonstrates the ideas in this post without actually producing a full pin.

If you use this and get banned, that's on you.

```python
def generate_combinations():
	# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
    possible_a_chars = "5BDEFHKLPRU"
    possible_b_chars = "JU"
    combinations = []

    for a in possible_a_chars:
        for b in possible_b_chars:
            code = f"7{a}{b}S"
            combinations.append(code)
    return combinations

# Generate and print all combinations
codes = generate_combinations()
for i, code in enumerate(codes, 1):
    print(f"{i}. {code}")
```

To run this, copy and paste into a file (`gen.py` for example) and then run from your command line:

`python3 gen.py`

And you should see output that looks like this:

```
1. 75JS
2. 75US
3. 7BJS
4. 7BUS
5. 7DJS
```