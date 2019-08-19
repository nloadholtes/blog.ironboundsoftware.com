---
layout:     post
title:      "Data clumps"
date:       2005-11-15 08:30:53
categories: java
---
In the book "Refactoring: Improving the design of existing code" Martin Fowler makes a lot of interesting points about the "smells" that you can detect in (potentially) bad code. Today I ran across a problem in some that resulted in several different smells. Basically I had too many parameters that were duplicated across several methods. When I made a change to one of the parameters I had to make changes in a bunch of different places to reflect this change. In the book this basically resulted in the smells "Long Parameter List", "Shotgun Surgery", and "Data Clumps". The last one is the one that caught my eye, if I had detected that smell earlier then the other two smells would have never surfaced. Fowler points this out on page 81: 

> A good test is to consider deleting one of the data values: if you did this, would the others make any sense?

That section of the book is now making me think about data that I'm passing around: There's probably a lot of parameters that can and need to be consolidated into objects. That way the consolidation objects can be modified and the classes that pass it around won't have to be. Plus as a side benefit there will be a better definition of your business objects and what you are trying to accomplish with them.
