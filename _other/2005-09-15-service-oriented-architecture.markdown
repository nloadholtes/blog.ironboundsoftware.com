---
layout:     post
title:      "Service Oriented Architecture"
date:       2005-09-15 21:53:48
categories: programming
---
There's a great article on IBM's DeveloperWorks website about SOA and code reuse. Check it out: [Reuse engineering for SOA](http://www-128.ibm.com/developerworks/webservices/library/ws-reuse-soa.html?ca=drs-tp3705). This quote really caught my eye: 

> Services are to be independent, in that clients need not understand the inner workings of a service component; essentially the service operates as a "black box." "White box" reuse, or cut and paste, where source code is modified in order to use in another context, while useful, is not typically as beneficial as "black box reuse."

I've been a long time cut-n-paste guy, but lately I've been seeing the advantages of doing more "black box" code. This quote hit me like a ton of bricks, it succinctly describes the way that code should be reused. Of course this (code reuse) is something that has been touted for years (its one of the first things any OO book says about the benefits of OO programming). I have always nodded my head and agreed with this statement, but was never able to really implement it (beyond doing class inheritance). For some reason lately (my growth as a programmer I suppose) I've been thinking of reuse more in a "architectural" way (i.e. creating and using interfaces) rather than in an "implementation" way (i.e. cut-n-paste working code into new code). For me, this article does a good job of explaining why the SOA oriented design and reuse are good things. 
