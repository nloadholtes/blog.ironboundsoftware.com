# Possibility and Probability

This is the new site! Here's what's new:

{% for post in site.posts limit:10 %}
<div>
<h3>{{ post.title }}</h3>
Published on {{ post.date | date: "%a, %d %b %Y %H:%M:%S %z" }}<br>
<a href="{{post.url | prepend:site.baseurl | prepend:site.url}}">Read more...</a>
</div>
<hr>
{% endfor %}

Thanks for visiting!
