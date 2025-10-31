from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import RedactorsCreateForm
from .models import (Newspaper,
                     Topics,
                     Redactor)


class NewsListView(generic.ListView):
    model = Newspaper
    template_name = "news/index.html"
    context_object_name = "newspapers"
    paginate_by = 5

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q:
            return Newspaper.objects.filter(title__icontains=q)
        return Newspaper.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "")
        return context


class NewsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    fields = "__all__"
    template_name = "news/newspaper_form.html"
    success_url = reverse_lazy("news:index")


class NewsUpdateView(generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    template_name = "news/newspaper_form.html"
    success_url = reverse_lazy("news:index")


class NewsDeleteView(generic.DeleteView):
    model = Newspaper
    template_name = "news/newspaper_delete_confirm_form.html"
    success_url = reverse_lazy("news:index")


class NewsDetailView(generic.DetailView):
    model = Newspaper
    template_name = "news/newspaper_detail.html"


class TopicsListView(generic.ListView):
    model = Topics


class TopicsCreateView(generic.CreateView):
    model = Topics
    fields = "__all__"
    success_url = reverse_lazy("news:topics_list")


class TopicsUpdateView(generic.UpdateView):
    model = Topics
    fields = "__all__"
    success_url = reverse_lazy("news:topics_list")


class TopicsDeleteView(generic.DeleteView):
    model = Topics
    template_name = "news/topics_delete_confirm.html"
    success_url = reverse_lazy("news:topics_list")


class TopicsDetailView(generic.DetailView):
    model = Topics
    context_object_name = "topics"


class RedactorsListView(generic.ListView):
    model = Redactor
    template_name = "news/redactors_list.html"


class RedactorsCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorsCreateForm
    template_name = "news/redactor_form.html"
    success_url = reverse_lazy("news:redactors_list")


class RedactorsUpdateView(generic.UpdateView):
    model = Redactor
    form_class = RedactorsCreateForm
    template_name = "news/redactor_form.html"
    success_url = reverse_lazy("news:redactors_list")


class RedactorsDeleteView(generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("news:redactors_list")


class RedactorsDetailView(generic.DetailView):
    model = Redactor
    context_object_name = "redactor"
