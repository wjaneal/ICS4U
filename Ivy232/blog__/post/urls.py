'''
from django.conf.urls import url

from django.conf.urls import include

from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #function of show overall posts
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    #function of displaying one specific post
    url(r'^post/new/$', views.post_new, name='post_new'),
    #function of create a new post
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    #function of editing the posts
]

