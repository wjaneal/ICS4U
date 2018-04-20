from django.db import models

# Create your models here.
# coding:utf-8
from django.db import models
 
 
class Article(models.Model):
    title = models.CharField(u'title', max_length=256)
    content = models.TextField(u'content')
 
    pub_date = models.DateTimeField(u'time to publish', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'time to update',auto_now=True, null=True)
    def __str__(self):# 在Python3中用 __str__ 代替 __unicode__
        return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "Full name of the person"

    full_name = property(my_property)

