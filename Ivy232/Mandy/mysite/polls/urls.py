"""
Created on Mon Mar  5 13:31:03 2018

@author: xuwentong
"""


from django.urls import path
from . import views
#1
'''
app_name = 'polls' # identity different apps'urls
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    # the 'name' value as called by the {% url %} template tag (in html)
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # added the word 'specifics'
    path('specifics/<int:question_id>/', views.detail, name='detail'),
]
'''
# New: Amend URLconf
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
