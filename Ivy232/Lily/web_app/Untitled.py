{% load staticfiles %}

<html>
    <head>
        <title>Blog from Ivy Hall</title>
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    </head>
    <body>
        <div class="page-header">
            <h1><a href="/">Blog from Ivy Hall</a></h1>
        </div>
        {% for post in posts %}
            <div class="post">
                <p>published: {{ post.published_date }}</p>
                <h1><a href="">{{ post.title }}</a></h1>
                <p>{{ post.text|linebreaksbr }}</p>
            </div>
        {% endfor %}
    </body>
</html>
