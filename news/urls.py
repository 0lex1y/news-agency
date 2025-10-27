from django.urls import path
from .views import *

app_name = 'news'
urlpatterns = [

    # News
    path('', NewsListView.as_view(), name='index'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/<int:pk>/detail/', NewsDetailView.as_view(), name='news_detail'),

    # Topics
    path('topics/', TopicsListView.as_view(), name='topics_list'),
    path('topics/create/', TopicsCreateView.as_view(), name='topics_create'),
    path('topics/<int:pk>/update/', TopicsUpdateView.as_view(), name='topics_update'),
    path('topics/<int:pk>/delete/', TopicsDeleteView.as_view(), name='topics_delete'),
    path('topics/<int:pk>/detail/', TopicsDetailView.as_view(), name='topics_detail'),

    # Redactors
    path('redactors/', RedactorsListView.as_view(), name='redactors_list'),
    path('redactors/create/', RedactorsCreateView.as_view(), name='redactors_create'),
    path('redactors/<int:pk>/update/', RedactorsUpdateView.as_view(), name='redactors_update'),
    path('redactors/<int:pk>/delete/', RedactorsDeleteView.as_view(), name='redactors_delete'),
    path('redactors/<int:pk>/detail/', RedactorsDetailView.as_view(), name='redactors_detail'),

]
