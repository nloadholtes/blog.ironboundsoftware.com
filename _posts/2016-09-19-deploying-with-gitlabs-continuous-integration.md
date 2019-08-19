---
layout:     post
title:      "Deploying with Gitlab's Continuous Integration"
date:       2016-09-19 11:31:52
categories: software-development
---
Have you seen the [Gitlab Continuous Integration feature](https://about.gitlab.com/handbook/sales/idea-to-production/)? It is pretty sweet. All you have to do is include a special yaml file and then when you check in new code it will build/test it for you. As awesome as that is, can it also deploy your code? The answer is YES! 

## Getting started

The first step is to create a .gitlab-ci.yml file in the root of your repo. This file is seen by gitlab and is used to configure a Continuous Integration (CI) server that will build and test your code.

> For the full details, you should [check out their documentation](https://about.gitlab.com/2016/08/26/ci-deployment-and-environments/). It is basically running your code in a docker container making the whole process pretty flexible.

I have a pretty simple homepage for myself over at [ironboundsoftware.com](https://ironboundsoftware.com). Its just a static site that is generated by gulp after it processes some handlebars templates. That's the kind of task that is great for a CI server, then the generated output can just be copied onto the server and boom, its being served. The only catch is that gitlab doesn't support pushing from its servers to your server. Via Deploy Keys it can pull your code, but that isn't terribly helpful in this situation. But, it turns out you can set up a private key that can be used to scp your code to its server. This is the help document that explains how to do this: [How to deploy code from gitlab](https://docs.gitlab.com/ce/ci/ssh_keys/README.html)

## It is so easy

The process is pretty straightforward: 

  * Create a new ssh key. _Don't re-use your current ssh key!_ Key reuse is a bad security practice.
  * Use ssh-copy-id to copy the public ssh key to your server
  * Go to your gitlab project page and select "Variables"
  * Make a new variable called SSH_PRIVATE_KEY and set its variable to  **the private key**. It is very important that you give it the private key, that's what makes it work (your server has the public key).
  * Update your .gitlab-ci.yml file so it looks something like the following example:

At this point when you commit and push your code to gitlab it will kick off the CI process. The sample code assumes this a JS project and it is using gulp to build the assets. At the end (line 37) it does a plain scp of the output directory (recursively) to the specified directory on the server. The end result is your newly created HTML, CSS, and images are pushed to your server and ready to be served up! That's right, a git push resulted in new code being deployed to production. THAT'S AWESOME!!!!!! 

## Gitlab continuous integration FTW

The great thing about all of this is that it is free. Gitlab does not charge for this awesome feature which is great because all developers need to be familiar with CI. This is the perfect opportunity to learn this important skill. Doing this requires only adding 1 file to your repository and the creation of 1 ssh key. These are simple to do, so you are cheating yourself if you don't at least try it out. As an added bonus, you can brag that you've got a CI/CD setup for one of your side projects. That's an awesome bragging point! Since the back end uses docker (you are using docker right?) it should be pretty easy to do[ Continuous Integration and deployment](http://amzn.to/2fpmoCO) with most any language or framework. My next task is to get this working with a [Python](https://python.org) Flask app I've been developing.