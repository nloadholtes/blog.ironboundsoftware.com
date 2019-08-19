---
layout:     post
title:      "Being subversive with Subversion: Mercurial in the middle"
date:       2010-02-25 20:41:52
categories: os-x
---
DVCS is a popular topic these days on the internets, but for those of us who code for our day job find that more often than not we have to use the tried-and-true standard of something like CVS. Or if you are lucky, SVN. Personally I think SVN is pretty good (especially compared to CVS), but the other day a feature of DVCS's caught my eye. The ability to branch quickly and in a lightweight manner is one of the major selling points of systems like Mercurial and Git. Recently I've been thinking about trying out some refactorings and that can be difficult to do when you need to make sure that you can have a build-able version of your code at all times. Some things just take time, and the whole point of refactoring is to improve your code so rushing through it to meet an unrelated code deadline just doesn't make a lot of sense. Enter [Mercurial](http://mercurial.selenic.com). There's a project for Mercurial called [hgsubversion](http://mercurial.selenic.com/wiki/HgSubversion) that will allow you to pull from a subversion repository and make a mercurial repository locally. (Yes, git has something similar) Then you can hack away to your heart's content using hg to branch and keep track of changes without pushing the changes out globally to the other SVN users. This is exactly what all of the cool kids using hg, git, and bzr have been doing for years. Now those of us who talk to SVN can leverage this technique to bring a little more awesomeness to our day-to-day work, and no one is the wiser. At least that's my theory. Installing hgsubversion on a Mac or in Cygwin is like pulling teeth. I take that back, pulling teeth is not as painful. Plus you can leave your teeth under your pillow for some cash... but I digress. The best way to install it (for me at least) is to do the following: 

  * Have the following installed: mercurial, easy_install, the XCode tools (command line tools like gcc)
  * Get a copy of the python swig bindings for Subversion. [Collab](http://www.collab.net/downloads/community/) has prebuilt binaries that seem to work best. I just copied the bindings from /opt/subversion/lib/svn-python/ to my python site-packages directory. I installed Python 2.6, so for me that path is: /Library/Frameworks/Python.framework/Versions/Current/lib/python2.6/site-packages
  * Get hgsubversion by typing at the command line: _`hg clone http://bitbucket.org/durin42/hgsubversion/ ~/hgsubversion`_
  * cd into ~/hgsubversion/ and type in _python setup.py install_
  * For me, the system had to download a few things and build them, so make sure you have XCode and the 10.4 SDK installed. (I'm running XCode 3.2.1 for this exercise)
  * Hopefully everything completes normally. If it does, do a victory shot. If it fails, do 2 shots and then try to figure out what went wrong.
  * Next make a file in your home directory called .hgrc
  * Inside the file put the following:



> [extensions] rebase= svn=/Users/<YOUR USERNAME>/hgsubversion/hgsubversion

  * This **should** tell hg that you've got something extra for it. I went blind sometime during my attempts to get this working and had a typo in that line that kept me from getting it working for an embarrassingly long time.
  * If you have done everything right, the moon is in the proper phase, and the wind is blowing from the NW at 7 mph, then this command should let you pull down a project from Google code:



> hg clone svn+http://<A PROJECT OF YOUR CHOICE>.googlecode.com/svn <WHATEVER DIR>

  * The end result should be a mercurial repository on your local machine. Refer to the link for hgsubversion for more details about commands and links to other installation instructions. (Some are older than others, and the commands have changed a little bit over time.)

So, that's what I'm up to. Hopefully this will let me do some interesting experiments locally without sacrificing the safety blanket of using version control.
