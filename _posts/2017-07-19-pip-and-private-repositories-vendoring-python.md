---
layout:     post
title:      "pip and private repositories: vendoring python"
date:       2017-07-19 22:29:52
categories: python
tags:  
permalink: /2017/07/19/pip-and-private-repositories-vendoring-python/
---
At work I am working on a project to migrate a series of Python apps into the cloud. Docker is a perfect fit for some of the apps, but one problem we ran into is getting our apps to build when they have a dependency on a private repository. Using a technique called vendoring we are able to work around this problem and ensure that our dependencies are well known. Let's look at vendoring python code. 

## Vendoring Python: The basic problem

When docker builds an image we have it execute `pip install -r requirements.txt` to have install all of our Python dependencies. Inside of our requirements.txt file we have the normal dependencies like this: 

oauthlib==0.7.1 requests==2.4.3 requests-oauthlib==0.4.2

But we also have some dependencies that live in private repositories and those have entries that look like this: 

-e git+https://github.com/company-name/private-python-utils.git

This line tells pip to go to github and pull down that project. The catch is that for a private repo pip has to access to an ssh key that has access. If you run pip from the command line the operating system will supply that ssh key and pip is able to install the project. When docker runs pip, it does not have access to those ssh keys. As a result, the pip install fails because it can't see the repository. [caption id="" align="alignleft" width="1024"][![Python vendoring: put your dependency in a safe place!](https://farm4.staticflickr.com/3229/2647981973_a28e776b00_b_d.jpg)](https://farm4.staticflickr.com/3229/2647981973_a28e776b00_b_d.jpg) Source: https://flic.kr/p/52ZAMB[/caption] 

## Shopping local with people you trust

It might be possible to add a key to docker to allow it access, but then this becomes a management pain: every thing that tries to run `docker build` is going to have to be setup with that key. (Think about CI services, new developers, etc.) Instead, a better solution is to "vendor" the code. This means taking a specific snapshot of the project and putting it into your project. As in checking it into git. I first saw this technique being used by people in the [Go Lang community](https://golang.org/). They were doing it as a way to guarantee they were working with a "known" piece of code. ("known" meaning that they had done a security audit on it, etc.) Let's walk through the high level steps and then discuss the reasons and details. 

### Package up the dependency

In Python, there is a special file called `setup.py` that lives in the root directory of a project. For libraries this is a useful file to have, it describes the project and its dependencies. ( _Side note: if you are going to put a project into pypi.python.org having this file is a requirement)_ For details about `setup.py` I will refer you to this excellent article. This will get you up and running with a bare-bones file which is good enough for this exercise. With that file in place, the next step is to package up your code using the command: 

`python setup.py sdist`

That will create a directory called `dist` which holds a copy of your project in an install-able form. I work almost exclusively on Linux systems and by default there it seems to produce .tar.gz files. 

### Adding the dependency

The next step is to take that distributable file and put it into a directory in the base of your project. As a convention, most people will call this directory "vendor". This identifies it as things that are external-yet-essential to the project. Once the distributable file is there, the next step is to commit it to add it to version control. By doing this you guarantee that your code is now working against a known version of the dependency. This is a big deal in environments where immutability and repeatable builds are valuable. 

### Updating the requirements.txt

The final step is to update the requirements.txt file so that pip will be able to find and install the library. This is surprisingly easy to do. Simply change the line (see above) to: 

vendor/private-python-utils.tar

And now when pip runs, it will look in the vendor directory for that file and then install it from there. At this point you are vendoring python! The code should be ready to go. 

## Pro-tip

One thing I like to do when creating a setup.py file for a library is to include something to get the current git tag and commit information. This can be included into the name of the distributable file which helps identify which version of the library you are working with. Sometimes a gist is worth a thousand words, so here's an example of how to do this. (If you are not using git as your source control there is probably a similar way to do this.) 

## Wrapping up vendoring python

By this point you should have everything in place for an "external" system like docker or a CI server to be able to build your project. As long as it can run `pip` it should be able to find the dependency and install it. If you want to see another example of vendoring packages from github repositories, check out this link here for [a great overview of using some of pip's lesser known features](https://medium.com/underdog-io-engineering/vendoring-python-dependencies-with-pip-b9eb6078b9c0). With this in place you should be able to feel more secure about the code you are running because now the version really locked down.
