
This is the new site! Here's what's new with my current project [https://remotematcher.com](Remote Matcher){:target="_blank"}:
<iframe title="Makerlog Embed" height="300" style="width:100%" scrolling="no" frameborder="0" allowtransparency="true" src="https://api.getmakerlog.com/users/3793/embed"></iframe>

---
Here are the latest posts

{% for post in site.posts limit:10 %}
<div>
<h3>{{ post.title }}</h3>
Published on {{ post.date | date: "%a, %d %b %Y %H:%M:%S %z" }}<br>
<a href="{{post.url | prepend:site.baseurl | prepend:site.url}}">Read more...</a>
</div>
<hr>
{% endfor %}

Thanks for visiting!
