---
layout:     post
title:      "Using scanf in Sparc Assembly language"
date:       2004-05-07 20:55:56
categories: programming
tags:  
permalink: /2004/05/07/using-scanf-in-sparc-assembly-language/
---
  
 Recently I was in a class covering the Sparc architecture and assembly language. The book we were using was not the best, and as a result there was a lot of scrambling to [Google](http://www.google.com) in the hopes of finding answers. However, even Google wasn't able to help that much.   
  
 So, I'm going to share a few things I learned that hopefully will add to the knowledge. The main issue that everyone in my class seemed to run into was how to use scanf. scanf is used to read input from the keyboard. To use scanf, you have to supply it two things: information about what type of data is going to be read, and a destination where you would like it stored. This code snippet shows how this is done for a number (not this is not a complete program, just a snippet):   
  

    
    
      
    
    .section ".data"
      
    
     format_num:	   .asciz "%d"
      
    
     size:		   .long 0
      
    
    
      
    
    
      
    
    .section ".text"
      
    
     set format_num, %o0
      
    
     set size, %o1
      
    
     call scanf, 0
      
    
     nop
      
    
    

  
 What is going on here is the _format_num_ is a variable containing "%d" which is the scanf/printf marker for a number. This is set into %o0 as the first argument to scanf. This is being used in exactly the same way it is used in C/C++ programming, it is letting scanf know that the input we are going to be reading in should be treated as a number (an integer in this case). If we were reading in another type we would have used its appropriate marker:   
  
%d integer   
%s string   
%c char   
  
  The variable _size_ is then loaded into %o1. The catch here is to notice however, that what is being loaded in is the **address** of _size_. This is important because when you go to retrieve the value that scanf read from the keyboard, you have to remember that _size_ is an **address**. So when you go to use that value you have to to a load. This would look like:   
  

    
    
      
    
     set size, %l0	! Move the address of size to l0
      
    
     ld [%l0], %l0	! Move the contents of the address into l0
      
    
    

  
  
 At this point, %l0 contains the value pointed to by size. This is where myself and many in the class made a mistake. We simply tried to use _size_ without doing the load. This left us with an address and not a value. And when you are expecting a value, an address is not a good thing. Here's small program to demo all of this:   
  

    
    
      
    
    .section ".data"
      
    
     format_num:	   .asciz "%d"
      
    
    
      
    
    .align 4
      
    
     size:		   .long 0
      
    
    
      
    
    .align 8
      
    
    
      
    
    .section ".text"
      
    
    .global main
      
    
    main:
      
    
     save %sp, -96, %sp
      
    
     set format_num, %o0
      
    
     set size, %o1
      
    
     call scanf, 0
      
    
     nop
      
    
     set size, %l0		! Move the address of size to l0
      
    
     ld [%l0], %l0		! Move the contents of the address into l0
      
    
     cmp %l0, 0		! See if user wants out
      
    
     be end
      
    
     nop
      
    
    end:	restore
      
    
     ret
      
    
        
    
    

  
  
 It doesn't do much, it reads in a number from the input, then compares it to 0. But if you step through this program using gdb you should see that %l0 will be loaded with the same number that you typed in, but %o1 will not have the number, but the address.  

