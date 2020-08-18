
Welcome!

I like computers and space. At least that's how my wife recently described me on a form for our kids' school.

I rather like that, so I've decided to embrace it! This blog is now going to be more about space exploration in addition to computers and programming.

From time to time I'll probably post something about small businesses (its a topic I do care a lot about), but for the most part I'm going to document the research I've been doing. Here's what I'm interested in lately:

* Exploration of the extended solar system, specifically the moons of outer planets.
* Robots doing that exploration
* Computing efficently or with reduced resources
* How AI can be used to make our future better

Thanks for checking it out! Be sure to sign up for the monthly newsletter. Not only is it a roundup of these posts, but I also include links to interesting articles.

<!--
I have put my current project [Remote Matcher](https://remotematcher.com){:target="blank"} on hold for a little while. Just too many things going on at the moment. It is still "open for business" so if you are interested in remote work, go check it out!
-->

<!-- <iframe title="Makerlog Embed" height="300" style="width:100%" scrolling="no" frameborder="0" allowtransparency="true" src="https://api.getmakerlog.com/users/3793/embed"></iframe>
-->

---
Here are the latest posts

{% for post in site.posts limit:10 %}
<div>
<h3>{{ post.title }}</h3>

{{ post.summary }}
  
<i>Published on {{ post.date | date: "%a, %b %d %Y" }}</i><br>
<a href="{{post.url | prepend:site.baseurl | prepend:site.url}}">Read more...</a>
</div>
<hr>
{% endfor %}

Thanks for visiting!
