---
layout:     post
title:      "Running a daily mailing list with Python and MailChimp"
date:       2018-02-25 16:02:03
categories: python
tags:  
permalink: /2018/02/25/daily-email-list-python-mailchimp/
---
So I'm a really big fan of Stoic philosophy. I really like the way it prepares us for troubles in life, and I thought it would be really cool to have a daily email to go out and give you a shot of Stoic inspiration for the day. And since I liked it, why not start a mailing list and share this others? The first step was to go to [MailChimp](https://mailchimp.com) and setup a mailing list. Getting people on to your mailing list is a huge topic and I won't really go into detail here but if you're interested to learn more tweet me at [@nloadholtes](https://twitter.com/nloadholtes) and let me know and I'll whip up a post for you.  _([Here's the list if you want to join it](https://heroicinspiration.com/daily-stoic-inspiration))_ The next thing that was needed was to organize these quotes into a way that was usable. I'm using an a Google spreadsheet because it's just really easy to put stuff there. Simpler to maintain than a database, this choice turned out to be a pretty good move! There are python libraries that can easily manipulate these spreadsheets. 

## My (basic) Workflow

Every Sunday evening I would go and go through my list of quotes in the spreadsheet. I usually just did a sort on the "date_used" column and then I choose a quote that I have not used in a long time and set that into an email template that would go out on a given day. Doing this is an extremely manual process. In the beginning I could be done fairly quickly, taking about 20 minutes. But after a while that got very old and there were a few days where I actually missed setting up the emails because I just didn’t have the time or energy on Sunday night. Another problem that I ran into was a human error. When you are copying and pasting from a spreadsheet into a separate window of a web browser, it's very easy to lose track of which quote you're working on and what day is supposed to go out. Additionally there was a weird mental stress that popped up, but more on that later. Putting this process into a script seem like a very obvious way to make my life easier. 

## Python + MailChimp API = <3

The script I wound up writing randomly chooses 5 older quotes that have not been in the past 90 days. It takes those quotes and generates an API call to MailChimp for each one to create a email campaign, one for each weekday. As it chooses a quote, it updates the “date_used” cell with the date we are going to publish the quote on. Here are the things you need to make this happen: 

  * A MailChimp account (free is fine) 
    * Create a mail list
    * [Create an API key](https://kb.mailchimp.com/integrations/api-integrations/about-api-keys#Find-or-Generate-Your-API-Key)
  * A google spreadsheet with quotes ([See this example sheet](https://docs.google.com/spreadsheets/d/126_iTXN0eQQSW9w8tUCcVBgQU9-7XPiRybOKpS5ZUKc/edit?usp=sharing), and make a copy!) 
    * An API key for access to that spreadsheet.  _(You will need read and write access, see[this documentation for details](https://github.com/burnash/gspread))_
    * The “key” id for the spreadsheet  _(this is the long string in the URL of the spreadsheet,_
  * `pip install mailchimp3 gspread` to get the [Mailchimp library](https://pypi.python.org/pypi/mailchimp3) and the GSpread library

With those pieces, you are ready to rock! Here’s what my code looks like:  This code is little hacky because I threw it together slowly over several months. At first, I was just getting the quotes and printing them to the screen. Then eventually I modified it to start posting them to MailChimp. The most recent change makes a dump of the quote data into a JSON file that I then feed into another script that handles posting to Facebook. (Let me know if you want a post about that) 

## How it works

The MailChimp and Google credentials are read from environment variables, but the spreadsheet key and a few other things are hardcoded. This is just how I did it, ideally those hardcoded things should also be parameters or env variables. (Translation: Don’t do what I did there!) The main method gets a “start” date parameter from the command line. (This script is assuming it will generate 5 days worth of quotes at a time, which is my normal cadence.) That date is then passed into the `get_quotes()` function which eventually returns a list of dicts containing the quotes for the week. That list is then serialized for another script to use, or if I need to do a re-run of this with the same data. The list is then iterated through, and each “day” in the list is fed into the `create_campaign()` function which generates the email. The final step is having the email scheduled for delivery on the appropriate day. After this runs you can log into your MailChimp account and see the emails all scheduled for delivery: [![](https://ironboundsoftware.com/blog/wp-content/uploads/2018/02/Screen-Shot-2018-02-25-at-3.06.01-PM-420x365.png)](https://ironboundsoftware.com/blog/wp-content/uploads/2018/02/Screen-Shot-2018-02-25-at-3.06.01-PM.png)And at this point, everything is set! I have found MailChimp to be very reliable and the scheduled emails have gone out without a hitch for over a year. 

## Some numbers

As of this writing I have 109 people on the mailing list. MailChimp has some very generous quotas for the free level, I have yet to bump into them with this list. Another thing I like about MailChimp: The reporting page is pretty nice and straightforward for these types of campaigns. Your numbers may vary, but this is what I see when I look at these reports: [![](https://ironboundsoftware.com/blog/wp-content/uploads/2018/02/Screen-Shot-2018-02-25-at-3.10.07-PM.png)](https://ironboundsoftware.com/blog/wp-content/uploads/2018/02/Screen-Shot-2018-02-25-at-3.10.07-PM.png) Considering this is a small list on a very niche topic, and is running on a free plan, this is pretty nice! Earlier I mentioned the time savings. Before my script, the MailChimp portion of this was taking about 20 minutes to do manually. Now that it is automated, all I have to do is type in the correct date and run the script. That normally takes about 30 seconds to complete. :) At this point I should probably create a cronjob and just use that to kick off the process automatically every Sunday. Another interesting thought: before I used to stress a little about picking the “right” quote for the day. By handing this responsibility to Python’s `random.sample()` function, I no longer worry about this. Instead I too get the pleasant surprise of seeing a random quote every weekday. Quick Note: I haven’t done the cronjob YET because I still haven’t fully automated the Facebook script that cross posts these quotes. Once I get that “fixed” the whole process will become hands off.  
