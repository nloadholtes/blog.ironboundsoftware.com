---
layout:     post
title:      "How to serve static files with flask"
date:       2016-08-22 10:16:32
categories: flask
---
With every web app there comes a time when you will need to serve up some static files. Maybe it is the JS or image files, or maybe you are just trying something out. Let's talk about how to handle this in [Flask](http://flask.pocoo.org/).  [caption id="attachment_811" align="alignright" width="357"][![Serving static files with flask is cool](https://ironboundsoftware.com/blog/wp-content/uploads/2016/08/freezeing_flask.gif)](https://ironboundsoftware.com/blog/wp-content/uploads/2016/08/freezeing_flask.gif) Just a cool picture.[/caption] 

## Letting something else serve the files

First things first, if you can let something else serve the static files, that should be your preference. Flask is a really great web framework, but it is not the best choice for serving up static content. Regular web servers like Apache or Nginx are much better choices. Web servers are optimized for this type of activity so it really is best to just let them do it. Most of the time this is a simple configuration change. This is a pretty common task, so thankfully there are lots of great sites that show how to do this. If you are using a service like  Amazon's Elastic Beanstalk service, you will find that there's an option for setting the static file path. 

## Getting flask to serve static files

Occasionally you will find that it is easier to just serve a static file from flask. Situations where this occur include: 

  * Its a very low-traffic file (like you legal terms and conditions for example)
  * You are doing active development and just need to test something out (e.g. you don't want to set up nginx on your dev machine)
  * You are running on something like Heroku and its just easier to serve this one file from flask

In any of those cases it is pretty easy to serve static files with flask by using methods like  **flask.send_file()** or  **flask.send_from_directory()**. [Here is a great StackOverflow discussion about how to use those methods](https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask#20648053). Here are two important things to remember when serving static files with flask: 

### Beware of using user input as part of the path

Since you can specify things like "../../" in the parameters you pass to send_file(), you need to be  _ **VERY**_ careful about anything you pass to it. For example, if you are just taking parameters that the user is sending in and using them... there's a great chance your user will send in "bad" data. For example, an attacker could start sending in things like "../../../../passwords.txt" or other things looking for files from you file system. If you have some kind of test data (for example, "sample_user_data.json") in your deployed code, someone is going to find it. If that file contains real data... well, it won't be pretty for anyone. 

### Flask likes to look for a folder called "static"

By default flask thinks that there could or should be a directory called "static" just under the root level of the project. This is a fine assumption, but depending on how your project is structured, it might not be correct. For example, in one of my current projects I've got a "server" directory which contains all of my flask and python code. I also have a "ui" directory which contains all of my Handlebars.js and Javascript code. I'm using gulp to process all of the javascript and output the HTML to "ui/output". If I want to serve up those files as I do my development, I have to pass in "../../ui/output/index.html" to  **flask.send_file()** instead of just plain "index.html". For development this isn't too terribly bad. It did take a couple of minutes to get the right number of "../" into the string, but once I did that then everything was fine. Once this goes to production I'm going to have nginx serve up the static files. 

## Other best practices

My number one bit of advice is to have all of your static files in one spot. When everything is nested under one directory it makes your configurations so much simpler to maintain. Instead of having one static directory for images, and another for images, etc, have those directories nested under one common directory. Many people will probably say I should combine the "ui" and "server" directories and have the HTML output written to "static". That is a great argument that will simplify some of the code, but I prefer to keep my language seperated in projects. too often I've seen SQL being put into template code, and HTML being coded into Java/Python methods. Having languages commingle like that just leads to a blurring of responsibilities. For me, the maintenance headaches down the road just aren't worth it. Your mileage may vary. 

## Wrapping up

You can serve static files with flask. If its going to be anything that is frequently trafficked, you are better off letting a web server handle the load. What's your favorite server? Let me know if the comments!
