---
layout:     post
title:      "Mercurial: forking from one place to another"
date:       2010-11-06 19:57:52
categories: mercurial
---
Lets say there's a cool project that you want to make a fork of at http://hg.example.com/coolproject and you want to store it on [BitBucket](http://bitbucket.org). How do you do this? It is pretty easy to do! First clone the project to your local system: 

> hg clone http://hg.example.com/coolproject

You now have a local copy. Then go and log into your bitbucket account. Create a new repository, for this example lets call it coolproject-fork. To push your local copy to BitBucket you can do this: 

> hg push http://bitbucket.org/your_username/coolproject-fork

Then your local copy will be pushed out to BitBucket. But... what do you do if you want to pull from the original and push to your private fork? Doing an **hg out** (from your local copy) will show that it is trying to push to http://hg.example.com, not BitBucket. To fix this, you have to modify the _hgrc_ in the project and tell it the out path is different than the in path. Go into the .hg directory in the coolproject directory and open up the hgrc file. Make these changes: 

> [paths] default = http://hg.example.com/coolproject default-push = http://bitbucket.org/your_username/coolproject-fork

Now you can do **hg pull** to get updates from the original project (on example.com) and when you do **hg push** it will push your changes back to BitBucket!
