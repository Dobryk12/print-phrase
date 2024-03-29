from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from press.forms import (
    NewspaperSearchForm,
    NewspaperForm,
    RedactorSearchForm,
    RedactorFormForLogin,
    RedactorFormForUpdate,
    TopicSearchForm,
    TopicForm
)
from press.models import (
    Newspaper,
    Topic,
    Redactor
)


@login_required
def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""
    newspapers = Newspaper.objects.all()
    topics = Topic.objects.all()
    redactors_top = (get_user_model().
                     objects.annotate(num_publications=Count('newspapers')).
                     order_by('-num_publications'))

    context = {
        "topics": topics,
        "newspapers": newspapers,
        "redactors_top": redactors_top,
    }

    return render(request, "press/index.html", context)


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    context_object_name = "newspaper_list"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        context["search_form"] = NewspaperSearchForm()
        return context

    def get_queryset(self):
        queryset = Newspaper.objects.all()
        name = self.request.GET.get("name")
        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("press:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("press:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("press:newspaper-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    context_object_name = "redactor_list"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)
        context["search_form"] = RedactorSearchForm()
        return context

    def get_queryset(self):
        queryset = get_user_model().objects.all()
        username = self.request.GET.get("username")
        if username:
            return queryset.filter(username__icontains=username)
        return queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorFormForLogin
    success_url = reverse_lazy("login")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("press:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorFormForUpdate
    success_url = reverse_lazy("press:redactor-list")


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        context["search_form"] = TopicSearchForm()
        return context

    def get_queryset(self):
        queryset = Topic.objects.all()
        name = self.request.GET.get("username")
        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy("press:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("press:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy("press:topic-list")
