# Possibility and Probability

This is the new site! Here's what's new:

{% for post in site.posts limit:10 %}
<div>
<h3>{{ post.title }}</h3>
Published on {{ post.date | date: "%a, %d %b %Y %H:%M:%S %z" }}<br>
[Read more]({{post.url | prepend:site.baseurl | prepend:site.url}})
</div>
{% endfor %}

<hr>
Thanks for visiting!
