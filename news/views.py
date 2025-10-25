from django.views import generic
from django.views.generic import ListView
from .models import *


class NewsIndex(generic.ListView):
    model = Newspaper
    template_name = 'news/index.html'
    context_object_name = 'newspapers'
    paginate_by = 5

