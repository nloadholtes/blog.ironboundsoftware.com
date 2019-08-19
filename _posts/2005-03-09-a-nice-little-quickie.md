---
layout:     post
title:      "A nice little quickie"
date:       2005-03-09 04:29:06
categories: python
tags:  
permalink: /2005/03/09/a-nice-little-quickie/
---
    
Along the lines of doing any amount of coding in any amount of time you have, I wanted to share this little nugget. I'm sure everyone who's been using python for more than 10 minutes knows this, but I find it so useful.  
  
    
Say you want to test something out like an HTML parser. Instead of hammering th sever 5 million times while you figure out what data you want to pull of the page, save the page to you local machine. Then in the directory where you saved the HTML file start up python (from the command line) and type in:  
  

    
    
      
    
    import SimpleHTTPServer  
    
    SimpleHTTPServer.test()  
    
      
    
    

  


  
  
    
This will start a small webserver on port 8000 (so you url would be http://localhost:8000) and then you can get to the page that way. I did this with the Beautiful Soup stuff a while ago and it worked liked a champ.  

