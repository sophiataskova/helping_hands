from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import Http404

from helping_hands_app.models import Event

def index(request):
    latest_event_list = Event.objects.all().order_by('-pub_date')[:5]
    context = {'latest_event_list': latest_event_list}
    return render(request, 'helping_hands_app/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'helping_hands_app/detail.html', {'event': event})

def results(request, event_id):
    return HttpResponse("You're looking at the votes of event %s." % event_id)

def vote(request, event_id):
    return HttpResponse("You're voting on event %s." % event_id)
