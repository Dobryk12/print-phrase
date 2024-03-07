from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from press.forms import NewspaperSearchForm
from press.models import Newspaper, Topic


# @login_required
def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""
    newspapers = Newspaper.objects.all()
    topics = Topic.objects.all()
    redactors_top = get_user_model().objects.annotate(num_publications=Count('newspapers')).order_by('-num_publications')
    # newspapers_of_topic = topics.newspaper_set.all

    context = {
        "topics": topics,
        "newspapers": newspapers,
        "redactors_top": redactors_top,
        # "newspapers_of_topic": newspapers_of_topic
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
