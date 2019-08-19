---
layout:     post
title:      "Tagging mp3 files with Python"
date:       2005-06-05 21:30:00
categories: os-x
---
Thanks to iTunes I discovered that about half of my mp3's did not have any ID3 tag information in them. (Apparently the settings for my ripper got messed up sometime in the distant past...) I quickly decided that manually editing over 400 files was out of the question. The files were organized by Artist then by Album and finally there was the song file itself. I looked for a python based ID3/MP3 reader and found pytagger. Written in Python with no dependencies, and having a good examples and documentation, this is exactly what I was looking for. I ran the file from my "music" directory and it walked the directory, found the mp3's, looked at them to see if they had the ID3 tags, and if not it looks at the directory path and then plugs in the Artist and Album info. This then makes the mp3 show up correctly in iTunes' playlist. The main work (outside of the tree walk) is in the function tag(file). Also, as a side note, yes there is a simpler way to do the directory walk, but on the version of python I'm running (2.3 on OS X 1.4) it doesn't have that cool os.walk() method. So I used a recipe from the cookbook so that all versions of python can use this method. Check it out [here](http://geocities.com/nloadholtes/code.html).
