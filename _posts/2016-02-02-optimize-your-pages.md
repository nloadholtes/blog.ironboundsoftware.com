---
layout:     post
title:      "Optimize your pages!"
date:       2016-02-02 09:32:25
author:     admin
categories: programming
tags:  
permalink: /2016/02/02/optimize-your-pages/
---
If you are going to make web pages, you might as well make them fast. No one like sitting around waiting for something to load up. NO ONE. Don't be that website. Be fast! Optimize for an awesome visitor experience! Lets talk about some tools to help speed up your pages. If your site isn't on the public internet for whatever reason (and yes, there are a lot of pages that can't run on the public internet for  **very** good reasons) you can still profile and optimize your pages using the Chrome Developer tools. 

Firefox and other browsers also have developer tools. I personally favor Chrome, so I'm going to focus on that one for this article. Your browser of choice probably has tools that are very similar, I encourage you to learn them!

## Unleash the Chrome Developer Tools

Click on "View->Developer->Developer Tools" to get started. From here you can see a tool bar now splits your browser window: [![browser with tools opened](/blog/wp-content/uploads/2016/01/Screen-Shot-2016-01-24-at-11.13.07-AM-1024x411.png)](/blog/wp-content/uploads/2016/01/Screen-Shot-2016-01-24-at-11.13.07-AM.png) The tab you are interested in is "Audits". Click on the "Run" button and it will reload your page while profiling it to see where the code is spending all of its time. When it is done running you'll get a nice little report that is color coded to let you know where the trouble spots are. [![the results and things to optimize](/blog/wp-content/uploads/2016/01/Screen-Shot-2016-01-24-at-11.15.28-AM.png)](/blog/wp-content/uploads/2016/01/Screen-Shot-2016-01-24-at-11.15.28-AM.png) This information is really great. In this case it is pointing out that reorganizing some script tags and a CSS call will allow the browser to optimize the downloading of the files. That should allow the browser to render the page faster (which means the user will see the content quicker, and thus be happier). This report will also tell you not-so-useful things however. For example, the line about "base.css: 65% is not used by current page" is not really helpful. For this project base.css is where all of the css for the site has been condensed into. For this page, only 35% of the styles in that page are being used. This is ok, other pages will use other styles. It would be nice to know if there are styles that are not used anywhere in the site, but that's a tall order to fill and these tools don't offer that insight. 

## Check out GTMetrix to optimize for the network

If your site is on the internet, [GTMetrix is a great tool](https://gtmetrix.com/). It is similar to the Chrome Developer tools, but it runs from a computer somewhere on the internet. This allows it to see a more realistic view of your page's performance because it involves actual network data transfers. (The chrome tools run locally so they don't always reflect the true performance that an end user will experience.) To use this tool you tell it the URL of your site, and then it send a browser to look at it. That browser is configured to run some performance tools that will analyze its performance. This allows you to see some different opinions about your site and how you could optimize it. These tests will tend to find things like places where assets could/should be compressed, and also where you could be using a Content Distribution Network (CDN) to speed up your page rendering and delivery. This is a great tool to double check your work. Its free, so I highly recommend running your site on it at least once to see how your site looks to the outside world. [Thanks to the 100 MBA for recommending this great resource!](http://100mba.net/mba508/)

## Wrapping up

Hopefully this post has given you some ideas on how and why you should optimize your website. Please go and try them out! If you can make your website 20% your customers will love it! Be sure and drop a note to let us know how these tools work out for you!
