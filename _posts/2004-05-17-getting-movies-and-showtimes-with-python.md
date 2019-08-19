---
layout:     post
title:      "Getting movies and showtimes with python"
date:       2004-05-17 18:26:39
categories: python
---
    
Recently I was looking into a way to find out movie times for my local theater over my cell phone using SMS text messaging. (Actually it is using the AOL IM for connectivity, but that's another article.) Looking at [Yahoo's](http://www.yahoo.com) movie listings and the [Python Mechanize](http://wwwsearch.sourceforge.net/mechanize/) module I was able to come up with a pretty cool little function to strip out the movie titles and the times.   
  
    
Because I'm sending this out to a cell phone which has a pretty limited screen size, I used a regular expression to strip out vowels from the titles and to strip out the : from the times. A bit of a hack, but it really managed to compress things down well enough that it will all fit on phone's screen yet still be readable.   
  
    
At any rate, be sure to check out the [Python Mechanize module](http://wwwsearch.sourceforge.net/mechanize/), it is really useful for doing all types of web-related programming (i.e. programmatically simulating a user sitting at a browser). Right now I'm using it to try and implement some of the things I read in O'Reilly's [Spidering Hacks](http://www.oreilly.com/catalog/spiderhks/).   
  

    
    
      
    
    from mechanize import Browser
      
    
    from mechanize import Link
      
    
    
      
    
     def getMovies(self):
      
    
      print "Starting the movies"
      
    
      output = "nothing"
      
    
      response = b.open("http://movies.yahoo.com/showtimes/theater?id=1246")
      
    
      output = response.read()
      
    
      links = b.links()
      
    
    
      
    
      # Get the links. Go through them, looking for movies and the times.
      
    
      showtimes = ""
      
    
      for link in links:
      
    
       if (link.attrs[0][1][0:29] == "http://movies.yahoo.com/shop?"):
      
    
        showtimes += "\n" + re.sub(r'a|e|i|o|u', '',link.text)
      
    
       else :
      
    
        showtime = re.findall(r'[0-9]{1,2}:[0-9][0-9]', link.text)
      
    
        if(showtime):
      
    
         showtimes += " " + re.sub(r'(:00)|(:)', '', showtime[0])
      
    
    
      
    
      output = showtimes
      
    
      response.close()
      
    
    
      
    
      print "Done with the movies"
      
    
      return output
      
    
    

  

