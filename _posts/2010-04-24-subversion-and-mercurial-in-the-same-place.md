---
layout:     post
title:      "Subversion and Mercurial in the same place"
date:       2010-04-24 14:35:30
categories: java
---
In a previous post I talked about trying to use [Mercurial](http://mercurial.selenic.com/) (hg) in a Subversion (svn) world. Its been almost 2 months, and I've learned quite a bit about hg and how to use it in a svn based environment. At the time it seemed like the obvious choice was to get something ([hgsubversion](http://www.bitbucket.org/durin42/hgsubversion/)) that would let hg talk directly to the svn server, but still allow me to explore DVCS workflows. It turns out that this isn't the case. Luckily there are several different approaches that can be used. 

# I coulda been a contender...

The idea behind hgsubversion is to use hg as your version control tool. This extension lets it "talk" to svn servers, so you only need one tool. It sounds like a really great idea, but I ran into some stumbling blocks that while not necessarily show stoppers, they did cause me to look around for alternatives (more on that later). Here's the issues, good and not-so-good, that I had with this extension: 

  * **Poor support in cygwin -** Installing this on cygwin was a bitch-and-half. Getting all of the pieces to compile and install was a major act that I just couldn't pull off. Which is a bummer, I do love me some command line. However, [TortoiseHg](http://tortoisehg.bitbucket.org/) to the rescue!
  * It works great on the mac - I usually have the most trouble installing new stuff on my mac, but hgsubversion works like a champ with no problems.
  * **TortoiseHg rocks -** This program is amazing. It worked correctly right out of the box, and took no effort to get up and running on my windows machine. It really let me get started on this little experiment.

**

# "Other than that Ms. Lincoln..."

Once I  got rolling with TortoiseHg it was time to rock.  My main goal was to use hg to spin off branches of my main code tree to do things like experimental refactorings, playing with some unit tests, and to try and work on bugs in isolation. And I have to say after getting past a few growing pains, it really works well for that. I was off to the races, committing and rolling back my work with out a care in the world, knowing that there was a versioning system watching my back. Everything was going to great until I went to commit my changes back to the svn repository. Then I discovered a problem...

# Too many dicks on the dance floor!

It turns out that hgsubversion is pretty literal in that it converts hg to svn. It took all of the changes I had made in my branches and pushed them upstream to the svn server. The result was a ton of intermediary messages (from my hg checkins) being dumped into the svn log. Now please note that the code was ok. Nothing bad happened, it just looks like I committed a ton to the svn repository. I was under the impression that it was going to just take the diff of the last svn update and the head of the hg and push that. I wasn't thrilled with this, so I decided to look for an alternative that would let me do this. It turns out its really easy to do, simply do an hg init in you svn working directory.

# Say whaaaaa?

According the [Mercurial wiki for working with subversion](http://mercurial.selenic.com/wiki/WorkingWithSubversion#With_MQ_only), there's a couple of different ways to do this. The easiest is to just do a normal _svn co_ and then in that working directory do an _hg init_ and just let the two share a workspace.  This sounds just short of insane, but it works out really well. Just make sure to tell both to ignore the other's special directories (.hg, .svn). Once you do that the two get along really well. As you spin off hg branches locally, they won't know/care that their parent is actually a svn directory. This allows you to check in to your heart's content, but when it is time to push back to the svn repository, there will be only one change! Of course, with the good there is also the not-so-good. Here's somethings to be aware of. They aren't necessarily bad, but like with hgsubversion you need to make sure you are using the right tool in the correct manner:

  * One svn commit is one commit. - When you make your commit into svn, the hg history disappears. 20 checkins? Svn only sees 1. This can be both good and bad, so make sure that your commit message relays all of the important messages your checkins express.
  * Only one commit message to svn - If you are like me, you hate re-typing the same shit over and over. Committing to svn doesn't involve the hg messages at all, so you will need to either copy-and-paste the last hg message, or type something new.
  * You need disciple with branch/directory names. - Make sure you know what that directory is. This goes for most dev activites, but with the wild free for all that hg allows it gets really important. You can get turned around really easy, especially if you have multiple svn checkouts (i.e. different branches, etc.)

** Overall I really like using hg. Making it work with svn has been a big bonus because now I can get the best of both worlds without having to abandon svn. (That's a big bonus as most day jobs rely on svn!)
