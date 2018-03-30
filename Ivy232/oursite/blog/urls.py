from django.conf.urls import url

from django.urls import path
from . import views
'''
#app_name = 'blog'
urlpatterns = [

    path('',views.main_page, name='main_page'),
    path('post_list', views.post_list, name='post_list')
    #path('detail_page/', views.detail_page, name='detail_page'),

    #path('<int:post_id>/detail_page/', views.detail_page, name='detail_page'),
]

# This pattern will tell Django that views.post_list is the right place to go if someone enters your website at the 'http://127.0.0.1:8000/' address.
'''
urlpatterns = [
    # ex: /
    path('', views.main_page, name='main_page'),
    # ex: /post_list/
    path('post_list/', views.post_list, name='post_list'),
    path('post_list2/', views.post_list2, name='post_list2'),
    path('post_list3/', views.post_list3, name='post_list3'),

    # ex: /post_list/5/
    path('post_list/<int:post_id>/', views.detail_page, name='detail_page'),
    
]
 
