---
layout:     post
title:      "Football, Fixed Width records, and Python"
date:       2004-06-09 20:53:43
author:     Nick
categories: python,statistics
tags:  
permalink: /2004/06/09/football-fixed-width-records-and-python/
---
    
Football season will soon be here (American football that is) and this year I am determined to be better prepared. And to that end I have decided to gather player and team statistics so that when I'm setting up my fantasy team this year, they won't fall apart after the first month. Hopefully.  
  
    
If you are looking for player stats, I found a great site that gives every player's stats on a week by week basis. This is exactly what I was looking for. Most stat sheets I have used in the past gave only the totals per player per year (or only career totals). [Quickstats](http://www.quickstats.com) has everything on a week by week basis. Good stuff. And a great price too. Check 'em out if you are interested in football stats at all.  
  
    
After getting some of the stats file, I found that they are in a fixed width record format. (Thankfully there is no HTML to have to parse through which is what I had been planning to do...) My goal is to take the stats that I have, and put them into a spreadsheet. If I could convert the records from fixed with to a delimited, I could import it in with no problem....  
  
    
Python to the rescue! [This recipe](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/65224) is just what I needed. Now that I have the column widths and python's struct I can reformat the records with ease. Pretty slick!  
  
    
Now if only I could actually use the data I've gathered to field a winning team... :)  

