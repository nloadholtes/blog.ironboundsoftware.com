---
layout:     post
title:      "awk just f’n rocks…."
date:       2004-08-31 06:42:17
categories: programming
---
    
Every few years I am stuck trying to process some textual data. At some point I'll say to myself "Didn't I do something like this in awk once?" Then I'll but out my refrence book and any old code I can find. Usually within about 5 minutes I'm slapping my forhead shouting "Of course! It is so simple!"  
  
    
Tonight was one of those nights. I had many. many megs of text data, and I needed to print out all but 2 fields in each row. With a quick refrence on google and a little bit of experimenting I concocted this awk script in about 10 minutes that produced exactly what I wanted.  
  

    
    
    #       Print out everyting but columns 3 and five (no matter how many fields there are)  
    
    #  
    
    BEGIN { FS="|" ; OFS="|"}  
    
    {  
    
      printf $1"|"$2"|"$4"|"$6  
    
      for(x=7; x< NF; x++)  
    
     {  
    
       printf "|"$x  
    
     }  
    
      print "|\n"  
    
    }

  
  
    
This is why scripting languages rock.  

