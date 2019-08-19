---
layout:     post
title:      "TDD and honesty in code"
date:       2010-09-10 09:02:48
categories: astronomy
---
I'm working on a little project to help keep track of satellites. Specifically, I'm taking an existing code base (the [AIAA SGP4 code](http://pdf.aiaa.org/preview/CDReadyMAST06_1308/PV2006_6753.pdf) which is written in C/C++), wrapping it with [python](http://python.org), and then eventually putting a web front end on it. The end goal is that astronomers will be able to use this code/website to check their observations to see if there was a satellite in their field of view when they took their measurements. Since I'm using a known library in to create something new, this seemed like a really great opportunity to use some Test Driven Development (TDD) to ensure that as I build up the parts of the system, the numbers stay true and that the code stays honest. This is working out really well. Combining python's unit test module with [nosetests](http://somethingaboutorange.com/mrl/projects/nose) allows me to quickly bang out a test to make sure that the positional numbers that the SGP4 code generates is what the documentation says it should be. By using TDD I can map out where the code needs to go a little better: As I find something that is missing I can write out a quick test that will fail. When I run nosetests, I have that failure glaring at me telling me where more code is needed. For example, I have one set of test data that gives the observer's location in standard latitude and longitude coordinates. My code isn't quite expecting this, the [MPC format ](http://www.minorplanetcenter.org/iau/mpc.html)is a little bit different. This is a problem that is easy to fix, but I have a plethora of problems at the moment and I need to make sure this one gets taken care of properly. So I opened up the python file that tests the Observatory class and added in a failing test that called _testLatLongToXYZ()._ When I run the tests I now see that this is a failing method which gives me the mental kick in the pants to go and implement that method, even if it is just a stub. Why do I say just a stub? Because putting in the stub lets  me do two things: 1) I've now got something there, and 2) I can now update the test to call that stub. The secret is that the test should now call the stub and expect it to pass, but the stub should always return something (None, False, -1, etc.) to indicate that it failed. This acts as a pointer to an area that needs improvement in the code. This is what TDD is all about. You keep repeating this process until you converge on a "correct" answer which is a method that does just what it needs to do. In theory, and so far my practice confirms this, the resulting code should be smaller and more accurate. For me this is a great thing because it encourages code that is more honest. What is honest code? To me, it is code that does what it says and nothing else. The shorter the code is, the more focused it is. The python language is very expressive and allows you to do a lot without saying a lot. This power can lead you to try and do too much in one function. Once you have a function that not only converts Lat and Long, but also converts polar coordinates and writes satellite data to the database, can you really honestly call that function _convertLatLongToXYZ()_? This is especially valuable in the scientific context of this astronomy related code. The code is open source, and in the event there is a problem with it, as people dig into the code they need to have confidence that the code is relatively well written. At a high level the tests give them the numerical sense of ease that it is working when the tests run and show the proper numbers being returned. At a low level, seeing that the code is broken up into small logical sections gives the confidence that once  problem is found it can be corrected, tested, and shown that there are minimal side effects in other parts of the program. As the lone developer on this project, this type of check-and-balance gives me a lot of hope that I'll be able to produce something that is accurate and useful to the community at large. Openness and honesty help build confidence and trust. If you are interested in the project, be sure to check it out: [ObsSatId: A python astronomy project to wrap the SGP4 code to check for satellites](https://bitbucket.org/nloadholtes/obssatid)