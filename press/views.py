from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from press.models import Newspaper, Topic


@login_required
def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""
    newspapers = Newspaper.objects.all()
    topics = Topic.objects.all()
    redactors_top = get_user_model().objects.annotate(num_publications=Count('newspapers')).order_by('-num_publications')
    newspapers_of_topic = topics.newspaper_set.all()

    context = {
        "topics": topics,
        "newspapers": newspapers,
        "redactors_top": redactors_top,
        "newspapers_of_topic": newspapers_of_topic
    }

    return render(request, "press/index.html", context)
