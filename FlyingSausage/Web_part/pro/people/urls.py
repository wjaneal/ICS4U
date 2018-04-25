from django.conf.urls import patterns, url
from people import views
import question
urlpatterns = patterns('',
	url(r'^my/fav/$',question.views.fav_topic_list,name='fav_topic_list'),

	url(r'^follow/(?P<uid>\d+)/$',views.follow,name='follow'),
	url(r'^unfollow/(?P<uid>\d+)/$',views.un_follow,name='unfollow'),
	url(r'^my/following/$',views.following,name='following'),
	
	url(r'^register/$',views.register,name='register'),
	url(r'^login/$',views.login,name='login'),
	url(r'^logout/$',views.logout,name='logout'),
)
