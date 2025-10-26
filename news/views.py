from django.urls import reverse_lazy
from django.views import generic
from .models import *

class NewsListView(generic.ListView):
    model = Newspaper
    template_name = 'news/index.html'
    context_object_name = 'newspapers'
    paginate_by = 5


class NewsCreateView(generic.CreateView):
    model = Newspaper
    fields = '__all__'
    template_name = 'news/newspaper_form.html'
    success_url = reverse_lazy('news:index')


class NewsUpdateView(generic.UpdateView):
    model = Newspaper
    fields = '__all__'
    template_name = 'news/newspaper_form.html'
    success_url = reverse_lazy('news:index')

class NewsDeleteView(generic.DeleteView):
    model = Newspaper
    template_name = 'news/newspaper_delete_confirm_form.html'
    success_url = reverse_lazy('news:index')


class NewsDetailView(generic.DetailView):
    model = Newspaper

