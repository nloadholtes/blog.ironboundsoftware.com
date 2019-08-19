---
layout:     post
title:      "My experiences with 5 different Continuous Integration servers"
date:       2016-11-14 09:21:50
categories: software-development
tags:  
permalink: /2016/11/14/experiences-5-different-continuous-integration-servers/
---
I've become the Johnny Appleseed of Continuous Integration servers. After I was bit by the testing bug, I quickly developed an interest in CI and began setting up servers at the places I worked. The benefits of letting a computer run the test automatically are so appealing. It cuts down the number of "dumb" bugs that are generated. It also helps ensure that the code is still working the way it used to. 

> What is a "dumb" bug? It is one of those bugs that is very simple (like a missing parens) and is found as soon as another person takes a look at your code. The discovery usually leads to a facepalm by the developer who did it.

Over the years as I've traveled to different companies I've been able to help introduce various Continuous Integration servers to other developers. If you would like to learn more about why CI is important, I will to point you to [THE resource that I learned from, Continuous Delivery by Jez Humble](http://amzn.to/2fP1XQW). Its a big read, but it really covers the topic well and offers a lot of useful strategies. Here's a run down of my experiences with 4 different Continuous Integration servers.

## Jenkins

[Jenkins](https://jenkins.io/index.html) is an opensource project that is very popular among people wanting to get Continuous Integrations into their organization. It is pretty easy to start with Jenkins and that makes it a great way to experiment in-house with a Continuous Integration server. Jenkins does not have the prettiest UI, but it does tell you what you need to know: Did my build pass. There is a plug-in system so if there is some special feature you need chances are that someone has written something to address it. The major benefit of using Jenkins is it is a safe way to show off CI/CD to your organization. It is usually pretty easy to get people to look at Jenkins. With everything being inside of your company firewall, and because it is "optional" to your development process, most developers tolerate it. Once the benefits of Continuous Integration are apparent, people will start get excited about Jenkins. My experience is once that point is reached, management begins to see Continuous Integration as a vital part of the development process. Most developers understand that much sooner. :) 

## Codeship

[Codeship](https://codeship.com/) is a "Continuous Integration Server as a service" offering. You basically setup your project, point some webhooks to the service and then let it rip. For the project where I used Codeship, everything was already setup for me. Io I have no experience in getting it up and running from scratch. The project was setup so that Codeship would build any branch committed to. If the commit was on the master or staging branch, it would deploy it to those environments. Overall I found it very easy to use: Builds usually kicked off quickly and usually worked. The only issues I had were occasional build failures due to Firefox or Chrome not starting correctly. (We had some JS UI tests that were spinning up browsers.) Additionally, Codeship can tend to send out a lot of status emails. During the time I was using them there were some issues with their Bitbucket integration which was leading to a ton of emails about the status of the system. I was using Github as my repo, so these emails were of little use. I would like to point out that this is a better situation than what we normally see. When there is a problem, most companies stop communicating, so props to Codeship for keeping everyone in the loop. 

## Bamboo

[Bamboo](https://www.atlassian.com/software/bamboo) is the Continuous Integration service from Confluence and it integrates in with their other suite of apps. I did not use this service for a very long period of time, but I was impressed by how seamlessly it integrated with Jira and Bitbucket. The only real negative I remember about this system was that the UI could get confusing when it was time to update or create a new CI job. Overall I was pretty happy with this system. Its integration with Bitbucket and Jira helped the team always know the status of the build. 

## Gitlab

In 2016 [Gitlab](https://about.gitlab.com/) began offering a built-in CI service for its code hosting. By adding a special YAML file to your project you can instruct Gitlab on how to build and test your code. This in and of itself is interesting. As a solo entrepreneur/developer the most interesting part was the price: FREE. That's right, if you have a private repo and you want to do CI, you now have an affordable option. One that doesn't involve setting up your own Jenkins instance. :) The Gitlab offering uses Docker containers (running on [Digital Ocean](https://m.do.co/c/76f9b19dc762)!) to run your code. If you are already using Docker in your development workflow, it should be very straightforward to get your tests working. As a bonus, there is even a way to use this feature to deploy your code. That's right, you can do Continuous Delivery! I have a blog post here that talks about [my experiences in doing deployments with a simple handlebars.js website](https://ironboundsoftware.com/blog/2016/09/19/deploying-with-gitlab-continuous-integration/). 

## Bitbucket

Bitbucket began offering a CI service very similar to Gitlab's in late 2016. Of the Continuous Integration servers in this list it is the one I have the least experience with. So far it seems very similar to Gitlab. It uses A YAML file to configure the Docker based process that does your bidding. My initial experiences with it are positive, the documentation is great and the UI is very pretty. If you are on Bitbucket it is worth your time to look into their [Pipelines](https://confluence.atlassian.com/bitbucket/bitbucket-pipelines-792496469.html). 

## Conclusion: Continuous Integration servers are important/awesome

In the bad old days of software development, testing was usually the 2nd thing to be cut when the schedule started to slip. With continuous integration servers you can prevent these problems by having automatic checks run for you. Modern software developers will benefit highly from adding a CI solution to their workflow. Even if you are the only one using it, eventually everyone will see the advantage of it.
