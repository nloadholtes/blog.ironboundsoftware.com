---
layout:     post
title:      "Keep Flask from sending too many cookies"
date:       2015-08-18 12:28:28
author:     nickadmin
categories: flask,python,web,web services
tags:  
permalink: /2015/08/18/keep-flask-from-sending-too-many-cookies/
---
In the Python Flask web framework you can run into an issue where after logging in two cookies are sent back in the HTTP headers. One is the normal "session" cookie, and the other one is called "remember_token". This can cause a problem with some [Android libraries that only expect 1 cookie](http://stackoverflow.com/questions/18998361/android-volley-duplicate-set-cookie-is-overriden) to be sent back. The cause of this 2nd cookie is because of the [flask-login](https://flask-login.readthedocs.org/en/latest/#remember-me) library. It has a "helpful" feature that will send this second cookie. The tricky part is that you can't really stop it from doing this by manipulating the make_response response object. Instead, when you call login_user you have to pass a 2nd parameter to disable the remember cookie:    This will prevent that "remember_token" cookie from being tacked onto your request headers. The end result is one cookie and the Android Volley library is able to get the correct cookie.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY3NzA2MDAxNl19
-->