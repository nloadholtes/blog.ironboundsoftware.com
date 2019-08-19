---
layout:     post
title:      "Important Lesson: Ask if you aren’t sure"
date:       2004-11-29 09:01:06
categories: gtd
---
    
There's a [contest](http://linuxonpower.com) that's going on this month that is pretty interesting. Its a contest to port (or develop or optimize) an application for the powerpc64 linux platform. The prizes are a new car, 100 G5 Macs, or 100 $1000 prizes. I think it would be cool to have a G5, so I entered.  
  
    
To save myself some embarrassment, I won't tell you which application I picked to port/optimize. Needless to say it was AI related. ;) Anyways, I dove head first into the project. I was really happy at first, the code was pretty clean, and very portable (it compiled on the first try!).  
  
    
But as I began trying to profile it to find its hotspots and apply what I had learned about the PowerPC64 chip, I found that my optimizations were making the run time slower. Anyway, yesterday I decided that altering this good codebase (that is already portable across several platforms) wasn't the answer and instead I focused on the build process and making sure it produced the correct type of files. It turns out that just compiling something on a 64 bit platform doesn't mean you have a 64 bit object. Especially if the tools (make/gcc/etc) are compiled as 32 bit apps. You have to pass in specific flags to make sure the object files are 64 bit, and linked to the correct 64bit libs.)  
  
    
I wasn't feeling really strongly about my submission, it just seemed weak. But I kept telling myself that all of my "improvements" just made it perform worse, therefore they weren't improvements. So since the contest is over on the 30th of this month, last night I decided to zip up the code and submit it hoping for the best.  
  
    
This morning I had an email telling me my submission had been rejected by the maintainer. I was stunned that I was shot down so quickly. My gut reaction was to write an email to the maintainer of the project asking him/her exactly what they were looking for in an "optimized PowerPC64 port" of their project.  
  
    
And that's when it hit me I should have sent that email a week or so ago when I first had my doubt about where I was going. I started having flashbacks to college and high school, thinking about all the times I heard a teacher say "If you have a question about the assignment, don't hesitate to come talk to me about it."   
  
    
Needless to say, I feel kinda dumb. That's **exactly** what I should have done with this project. As a penalty for not thinking to do that, I am now without a chance of winning a G5.  
  
    
But I'm thinking I will email the maintainer to find out what they are thinking. I think I would like to take what I've learned and try to contribute to the project, even though I am now out of the running in the contest. Sort of an atonement for my mistake. This way everyone wins (more portable software).  

