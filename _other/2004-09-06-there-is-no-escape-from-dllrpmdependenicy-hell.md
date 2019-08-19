---
layout:     post
title:      "THERE IS NO ESCAPE FROM DLL/RPM/DEPENDENICY HELL"
date:       2004-09-06 21:20:04
categories: linux
---
    
Yesterday I was extolling the virtues of living outside of the Microsoft world to a friend. One of the things I do miss is being able to install something and have it work on the first try.  
  
    
Today I decided to try and install Spambayes. I'm tired of the spam, and I thought it would be neat to play around with for a few minutes. That was an hour ago. Here's how my morning has gone so far:  
  
1\. Tried to install Spambayes. Won't install because python doesn't have a configuration (or a make, I can't remember which now) file.  
2\. Check python. It is the default 2.3 install that came with the OS. Go download 2.3.4  
3\. Make python. Install python. Fix all of the pathing/link issues. Now using python 2.3.4  
4\. Install Spambayes. Configure Spambayes. Won't configure, there is no bsddbm package.  
5\. Download bsddbm. Try to install bsddmb. Won't install, Berkeley DB isn't installed. (Of course! grrrrr......)  
6\. Download and build Berkeley DB. Install Berkeley DB.  
7\. Build and install bsddbm.  
8\. Try to run Spambayes again. Discover (after 20 minutes) that there is a missing libdb.so file. Install that.  
9\. Discover I have downloaded a new version of Berkeley DB. So new that there are no python bindings for it. (Or at least that the bsddbm package only supports up through 4.1)  
10\. Download the proper version of Berkeley DB.  
  
    
At this point I'm thinking it must be miracle that my system even runs. Maybe I would be more interested in clicking on the spam links than trying to torture myself with this installation...  
  
11\. Build the older version of Berkeley DB. Install.  
12\. Attempt to test bsddbm. Found out it was compiled against old DB, still looking for non-existent lib file. Remove bsddbm, Untar and try again.  
13\. Test of bsddbm finally works. Still doesn't look correct, the info that popped up on the screen seems to think that the version is still 4.2.4. Oh well... If it runs, I'm not going to try and correct it.  
14\. Test ran ok!   
15\. Spambayes still doesn't see the db.  
16\. Look around on google. See other people have had the same problem. Don't see how they got it resolved.  
17\. Give up. Curse everyone. Kick self from trying to be different and running linux.  
18\. As a last gasp effort, I went back to the Spambayes dir and tried to run the sb_server.py file. To my surprise, not only did it run, but it also read in and processed my spam folder. When I tried to get it to read my regular inbox, the machine locked up. :(  
  
Grrrr....  
  
\-- _Update_  
    
Well it looks like what was wrong was when I compiled python there was no Berkeley DB, so it didn't build anything for it. As I was blowing away everything to try and clean the slate I ran make on python 2.3.4 and saw that it was compiling something called _bsddb. Now call me sick and twisted, but I'm going to give Spambayes another go around. But not tonight.  
  
    
I've had enough.  

