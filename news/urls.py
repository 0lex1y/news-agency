from django.urls import path
from .views import *


app_name = 'news'
urlpatterns = [
    path('', NewsIndex.as_view(), name='index'),
]