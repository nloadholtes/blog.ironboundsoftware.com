---
layout:     post
title:      "thumbnailer.py"
date:       2004-12-07 08:33:56
author:     Nick
categories: programming,python
tags:  
permalink: /2004/12/07/thumbnailerpy/
---

Ever have a ton of digital photos that you wanted to make a thumbnail gallery out of? Ever wanted a quick-and-dirty way to create it? I did. There's packages out there to do this, but a)I didn't want to pay for them, and b)I didn't want to install a ton of stuff. So I busted out trusty old python and whipped up this script. 

    
Its pretty simple, i.e. its pretty simply written, but it gets the job done. Just run it at the top of a directory structure and it will walk it (using a [recipe](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52664) from the cookbook). 

As it runs into jpg's it uses PIL (built into Python 2.3) to create a thumbnail jpg and a 800x600 pixel version of the picture. It also logs the images as it goes, and when it is done it writes out an plain-jane index.html file of all of the thumbnails (one per line) with a link to the 800x600 res version. 

The original image files are left intact. Enjoy! 

[thumbnailer.py](http://www.geocities.com/nloadholtes/code/thumbnailer.py.html)
    
```python
    #!/usr/bin/env python
    #
    # thumbnailer.py
    # 
    # A quick and dirty script to walk a directory tree, find jpg's,
    # make a thumbnail, and make a 800x600 version. Also makes an
    # HTML file to show all of the thumbnails (with links to the
    # 800x600 version). Designed to take the high quality pics 
    # from digital camera and produce a web friendly version gallery.
    #
    # by Nick Loadholtes
    # Nov 2004
    #
    import Image
    import os
    
    imagelist = []
    
    #
    # This function by  Robin Parmar's receipe on the python cookbook:
    # http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52664
    def Walk( root, recurse=0, pattern='*', return_folders=0 ):
    
            import fnmatch, os, string
    
            # initialize
            result = []
    
            # must have at least root folder
            try:
                    names = os.listdir(root)
    
            except os.error:
                    return result
    
            # expand pattern
            pattern = pattern or '*'
    
            pat_list = string.splitfields( pattern , ';' )
    
            # check each file
            for name in names:
                    fullname = os.path.normpath(os.path.join(root, name))
    
                    # grab if it matches our pattern and entry type
                    for pat in pat_list:
                            if fnmatch.fnmatch(name, pat):
    
                                    if os.path.isfile(fullname) or (return_folders and os.path.isdir(fullname)):
    
                                            result.append(fullname)
                                    continue
    
                    # recursively scan other folders, appending results
                    if recurse:
    
                            if os.path.isdir(fullname) and not os.path.islink(fullname):
    
                                    result = result + Walk( fullname, recurse, pattern, return_folders )
    
            return result
    
    #
    # This function takes a jpg in and creates a thumbnail version and a 800x600 version
    # while leaving the original file intact.
    def thumbnail(filename):
    
            global imagelist
            print "Crunching: ", filename
            outfile = os.path.splitext(filename)[0] + ".thumb.jpg"
    
            outfile2 = os.path.splitext(filename)[0] + ".med_res.jpg"
    
            print "\tOutfiles: ", outfile, " ", outfile2
            img = Image.open(filename)
    
            thumbsize = 64,64
            img.thumbnail(thumbsize)
    
            img.save(outfile, "JPEG")
            img2 = Image.open(filename)
    
            imgsize = img2.size
            if(imgsize[0] > imgsize[1]):
    
                    size = 800,600
            else:
                    size = 600,800
    
            medimg = img2.resize(size)
            medimg.save(outfile2, "JPEG")
    
            imagelist.append('<a href=\''+ outfile2+ '\'><img src=\''+outfile+'\'/><br/>'+os.path.splitext(filename)[0]+'</a><br/><br/>\n')
    
    
    
    if __name__ == '__main__':
            files = Walk('.', 1, '*.jpg', 0)
    
            print 'There are %s files below current location:' % len(files)
            for file in files:
    
                    thumbnail(file)
            htmlbuff = '<html><body>\n'
            for line in imagelist:
    
                    htmlbuff += line
            htmlbuff += '</body></html>'
    
            print htmlbuff
            f = open('index.html', 'w')
    
            f.write(htmlbuff)

```

