---
layout:     post
title:      "Petit DosBox Setup"
date:       2006-03-03 19:34:03
categories: apple
---
I had the [Petit DosBox from OS X](http://web.jet.es/guilly/slouc/software_petitdosbox.html) up and running a while ago, but today when I went to run it I kept getting an error about libSDL not being found. Last year I had an "incident" that basically required me to re-run the 10.4 installation. I think when I did that it must have wiped out the symbolic link I had made to get Petit to run. If you are finding yourself in this situation, here's what I did to get it up and running (Mac Mini running OS X10.4.5): 

> **WARNING** : Only attempt this if you are confident of your computer skills **_*and*_** you have backups of your important data. This is a fairly safe thing I'm describing, but you are doing it at your own risk. I'm merely pointing out what I did and how it worked for me. Your mileage may vary. Proceed at your own risk. 

  1. Open up a terminal window.
  2. Type in _cd /usr/local/lib_ and press return.
  3. Type in _ls_ and press return. Odds are there is nothing there.
  4. If you don't see anything that says SDL, type this in: _sudo su_ and press return
  5. Enter your system password. (Basically you are going to run as root for this next command)
  6. Your prompt should now say "root". Type in (or cut-n-paste) this line: _ln -s /sw/lib/libSDL-1.2.0.dylib libSDL-1.2.0.dylib_ and press return.
  7. Type in _ls_ and press return. You should now see **libSDL-1.2.0.dylib**. At this point try running any Petit dos program. If it works, yaa! If not, you might be missing the SDL installation. I'm not sure if it comes with the Mac by default or ifI had installed it manually.

If you have success or failure with these instructions, please leave a message in the comments. I'll try to help out if I can (but no guarantees). 
