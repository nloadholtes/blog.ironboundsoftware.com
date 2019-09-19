---
layout:     post
title:      "Global variables and my confusion"
date:       2004-05-28 01:27:16
author:     Nick
categories: programming,python
tags:  
permalink: /2004/05/28/global-variables-and-my-confusion/
---
    
I have only been programming in Python for about 5 months, so I am still fumbling my way through things. Last night I discovered that my understanding of global variable scope was way off. This code snippet illustrates my problem: 
    
    
    amount = 12
    price = 23
    
    def function1():
            amount += 1
    
    def function2():
            amount = price
            amount += 1
            print "Amount is: ", amount
    
    def function3():
            global amount
            amount += 1
            print "Amount is: ", amount
    
    if __name__ == "__main__":
            function1()
            function2()
            function3()

  
    
When I would try to run code like function1, I would get an error about "local variable 'amount' referenced before assignment". And this confused me to no end. From my C/C++ and Java background, it certainly looked like amount was in global scope, yet this error clearly stated that it wasn't. Instead of looking it up in my handy python book, I implemented something like function2. 

    
In function2 I would basically assign amount to be some other global value and then go and do my operations on amount. Yet when I left function2 and tried to use amount somewhere else I would not get the value I was expecting. Amount was not being used in a really critical section of code and there were other issues to deal with so I commented it out and decided to come back to it later. 

    
Well, last night was later. After about 5 minutes of looking at it (catching up on what the issue was) I pulled out the book and discovered to my surprise that you have to _declare that you are going to use a global variable_. function3 is an example of the proper usage of the amount global variable. 

    
At first this really irritated me, I thought that by virtue of the variable being suddenly assigned a value would cause Python to look into other scopes to see if the variable was defined in other places. That's what Java and C/C++ seem to do. 

    
But I can't decide which way I think is better. In layman's terms, Java is assuming the variable is global and Python is assuming it's local. Ok, that is an big oversimplification, but that was how it seemed to me at first. Strong typing vs weak typing. Static vs Dynamic. Compile time vs Runtime. I've never really thought about these issues in this way before. There are [arguments](http://www.artima.com/intv/strongweak.html) on both sides. 

    
At any rate, I've got much thinking to do about this topic. That and I need to go look through my code to make sure I'm not "getting away with murder at compile time" as Josh Bloch put it.
