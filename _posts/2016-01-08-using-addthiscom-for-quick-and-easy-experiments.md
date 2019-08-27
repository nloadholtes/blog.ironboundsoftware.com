---
layout:     post
title:      "Using addthis.com for quick and easy experiments"
date:       2016-01-08 11:00:55
author:     admin
categories: statistics
tags:  
permalink: /2016/01/08/using-addthis-com-quick-easy-experiments/
---
# Experiments?

In my previous post I extolled the virtues of doing experiments with your customer facing apps. In this post I'm going to discuss how to use the sharing widget from addthis.com to do experiments in a way that is quick and easy to do. 

## What is addthis.com?

Most pages on the internet have little buttons and widgets to let you "share this page". [addthis.com](https://www.addthis.com) makes a very nice widget that not only shares your page, but it also tracks metrics and allows for some other interesting things that we will discuss shortly. This is done by setting up a free account on addthis.com ([go ahead and do that now, it is very quick and easy to do](https://www.addthis.com)). Once you've made an account then you will get a little snippet of javascript that you can put into your web app. The instructions for doing this are on the addthis.com website, I highly recommend following them as they will be more up-to-date than anything I write here. Once the javascript is installed you can then visit the addthis.com site and begin setting up things like how you want the sharing boxes to look on the screen. There are tons of choices that are free, I recommend using one of those and wait until you get comfortable with the platform before going for one of the "Pro" versions. Soon on your website you should start seeing the addthis.com widget being displayed on your pages. In a day or two you can then visit the addthis.com website (make sure you are logged in!) and see some stats. The widget acts as an analytics tracker similar to [Google Analytics](https://analytics.google.com/analytics/web/) or [Gaug.es](https://gaug.es), but in a much simpler manner. I have found the addthis.com analytics to be much more high-level and easier to read at a glance than any other solution out there. That being said, if you want more in-depth information you should be using a tool like Google Analytics. 

## So what is the advantage of addthis.com?

The javascript that was added to your site not only devliers the share buttons and the basic analytics for your site, it also allows them to inject other things such as pop overs, recommendations, and pop ups. I realize that some people are very opposed to anything "popping" up or over on their websites, but the facts are that those tools are effective and will get people's attention. We can leverage this with our experiments in order to find out how to tune our website. For example, lets say you want to collect email addresses from your visitors so you can build up a mailing list. By going to the addthis.com site and selecting "Tools" and then "Targeting" you can select a type of popup or pop-over that collects email addresses. (There are other choices too such as offering a link or displaying a sharing message/buttons.) 

## This is where the experiments start

For this example we are going to select the "Collect Emails" option. This will lead us to a design screen where we can put in different text, different images, and make all kinds of other decisions on the location, colors, and other things about the pop over. To have a successful experiment, you should only test one variable at a time. In this example let's focus in on the text of our "call to action" and leave everything else the same. Here are the steps: 

  1. Type in one of the call to actions you want to use. Let say it is "Enter your email"
  2. Click on "Save and Activate"
  3. If you now hover over the newly created entry, you should see something that says "Start an A/B test". Click on that.
  4. You should now see something very similar to step #1. Change the text so that it says "Let's be friends!"
  5. Click on "Save and Activate"

And now you have a running A/B experiment on your website! It is literally that easy. We skipped over a lot of the features that addthis.com offers, please feel free to revisit the Tools page and see what you can do with the visuals and positioning, etc. The default behavior for this experiment is that it will show the pop up when someone tries to leave the site. Half will see the "default" message, and half will see the nice friendly message. 

## So my experiment is running...

Now as people visit your site they will randomly see one of the two messages. Revisit the "Tools" page and it will show you the results: how many people have seen the experiment, and how many actually click on one of the options. The nice thing about addthis.com is that they are already aware of statistical significance and have built in a little meter to show you how your experiment is doing. If you have low numbers of traffic it could take a while to see the numbers bump up to a point where a winner can be declared. On the flip side, if you've got a lot of traffic you will get you answer sooner! Here's an example of an outcome I got on a site I was working with: [caption id="attachment_504" align="aligncenter" width="452"][![a_b_test_outcome from addthis](/blog/wp-content/uploads/2016/01/Screen-Shot-2016-01-08-at-10.39.02-AM.png)](/blog/wp-content/uploads/2016/01/Screen-Shot-2016-01-08-at-10.39.02-AM.png) An example of an A/B test that showed which text I should be using[/caption] As you can see I had about 11,000 people look at this particular experiment. Even though the conversion rate (in this case I was testing out some text to see if I could get people to click on a link to view a FAQ page) was a little bit low, having a large enough volume of visitors helped to determine which copy text was better. This kind of experiment is great at settling an argument about what is the best copy to use on a website. By letting the visitor to the website decide by clicking we get a clear idea of what they want. In fact, we could take the winning text and modify it slightly then test it again to see if we can further improve it. These experiments are not limited to just text though! You can also test out things such as pictures, colors, and positions. The combinations are almost endless and I encourage you to try things out!
