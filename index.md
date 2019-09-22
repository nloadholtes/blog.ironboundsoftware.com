# Possibility and Probability
This is the new front page

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-247234-4"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-247234-4');
</script>

This is the new site! Here's what's new:

{% for post in site.posts limit:10 %}
            {% if post.catagories contains "python"  %}
            <div>
                <h3>{{ post.title }}</h3>
                {{ post.content | slice: 0,100 | xml_escape }}<p>
                {{ post.date | date: "%a, %d %b %Y %H:%M:%S %z" }}
                (Read more)[{{post.url | prepend:site.baseurl | prepend:site.url}}]
            </div>
            {% endif %}
{% endfor %}
