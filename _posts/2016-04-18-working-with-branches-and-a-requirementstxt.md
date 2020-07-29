---
layout:     post
title:      "Working with branches and a requirements.txt"
date:       2016-04-18 09:26:00
author:     nickadmin
categories: python,software development,uncategorized
tags:  
permalink: /2016/04/18/working-with-pip-branch/
---
Recently I had an interesting situation: We had some new code, lets call it project A, that had not been merged into master, but it needed to used by another project (project B) to see if a certain bug had been fixed. These projects are both python based, so they are using the normal tools. (pip and setup.py, etc.) Project B pip installs Project A, and in the requirements.txt it is listed like a normal git repository dependency. But, we want test a different branch of Project A. Simply promoting the branch to master is not ideal; if there is a problem with the branch potentially all projects that depend on Project A could be affected. And lets be honest, what are the odds they will be "positively" affected? In my experience, its zero. 

## Can we install a pip branch?

So ideally we need to get Project B to load in that specific branch. The first thought we had was to modify the version of Project B that had been installed in the virtualenv for Project A. This could get... messy. Instead of manually changing files (or trying to cherry pick file from a git repo) we can just use pip to get that branch. But how do you get a pip branch? The first step is to uninstall Project A so that we don't risk any bizarre cross-talk. This is done by invoking: 

pip uninstall project_a

Then the next step is to modify the requirements.txt file to point to the new branch. This is a temporary change that is being tested locally, so there is no need to check this file into your repo. The original line looked like this: 

-e git+ssh:git@github.com/path/to/project_a.git#egg=project_a

Thanks to this [link on stack overflow](https://stackoverflow.com/questions/20101834/pip-install-from-github-repo-branch), we now see that we should change this line to look like: 

-e git+ssh:git@github.com/path/to/project_a.git **@new_branch** #egg=project_a

Notice the part in bold. That is what tells the repo that we are looking for the branch named... new_branch. After this change, re-running pip install -r requirements.txt will download and install the specified branch of that repository. At this point Project B is ready to run with the new version of Project A. After you are done with your testing, all you'll need to do is uninstall Project A (like we did before), do a git checkout requirements.txt, and re-run the pip install. The beauty of this approach is the following: 

  1. You don't have to modify any of the locally installed files for Project A.
  2. The "integrity" of Project B is maintained: all of the work you did to install Project A is normal in terms of the development process. No special work is needed (other than the temporary change to the requirements.txt) to make this work.
  3. Related to #2, this process is repeatable. If you need to test multiple branches of Project A, these same steps can be repeated without significant changes to Project B.

And that's it! Its super easy to do, and it is a good exercise in making sure your project is setup correctly. Specifying a pip branch is a very easy way to get the code you want to test the things you need to see.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTQ0MTk2Njk0XX0=
-->