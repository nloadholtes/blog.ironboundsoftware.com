---
layout:     post
title:      "The advantages of protoyping"
date:       2004-05-04 01:32:45
categories: programming
---
(Note: This is a reposting of something I wrote last week. I switched over to bzero from PyDS and the transition was not smooth.) 

I'm taking a class in computer architecture and assembly language on the SPARC platform. For our last assignment the professor decided to give us a bit of a challenge and had us implement a sliding puzzle game. (You know the kind, 15 numbered blocks that can be moved around one at a time.) 

Pretty much everyone in the class got nervous right away, what was being asked of us was a lot more than we had done on our previous assigments. I did my usuall routine of sketching out pseudo-code on paper when an idea hit me. Prototyping. 

I've never really sat down an prototyped before, more often than not, the "prototype" wound up being the code that was submitted to the teacher/boss/client/etc. But this time the prospect of mucking around with assembly code to test out my ideas for the project just didn't sound right. Python seemed like an ideal tool. 

And looking back on it, I feel it was the right tool. Why? The best way would be to examine the other tools/langauges that could have been used: 

  * **Assembly:** Too difficult to debug, besides I was having enough "fun" getting things to work. Trying to seperate algorithm prooblems from language problems would have been too much.
  * **C:** Too tempting to pass the "-S" flag to gcc and have it spit out the assembly source. :) 
  * **UML or someother high-level descriptor:** I like to get my hands dirty and play with the code. These approaches (while great for documentation) are too high level for my tastes when starting a design like this.
  * **perl:** I prefer to have something that is readable
  * **python:** Though I don't have a debugger for python (or know how to use one) the write-compile-run cycle for python is so short, I felt I could overcome any errors pretty quickly (which was true).



The prototype that I made worked really well for me. While others in the class where still struggling on how to use random numbers to generate thier puzzles, I had already proven a method to myself using this easy-to-read block of python: 
    
    
    def getNumberFromRange():
    	return random.randrange(1, (size * size) )
    

That gave me such a great headstart on tackling the other thorny issues (displaying the board) that I was able to crank out my program without worring about the algorithms behind it, I had already proved them working so I could focus on the actual coding. (And by focus I mean trying to make sure I was running with out causing a bus fault, or a seg fault, or any of those other fun things that make a core file.) 
