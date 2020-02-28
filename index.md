
Welcome!

I have put my current project [Remote Matcher](https://remotematcher.com){:target="blank"} on hold for a little while. Just too many things going on at the moment. It is still "open for business" so if you are interested in remote work, go check it out!

<!-- <iframe title="Makerlog Embed" height="300" style="width:100%" scrolling="no" frameborder="0" allowtransparency="true" src="https://api.getmakerlog.com/users/3793/embed"></iframe>
-->

I'll have something interesting coming soon I'm sure, until then, please check out some of the things I've been thinking about:

---
Here are the latest posts

{% for post in site.posts limit:10 %}
<div>
<h3>{{ post.title }}</h3>
Published on {{ post.date | date: "%a, %b %d %Y" }}<br>
<a href="{{post.url | prepend:site.baseurl | prepend:site.url}}">Read more...</a>
</div>
<hr>
{% endfor %}

Thanks for visiting!
