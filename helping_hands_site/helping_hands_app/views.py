from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, Event


class IndexView(generic.ListView):
    template_name = 'helping_hands_app/index.html'
    context_object_name = 'latest_event_list'

    def get_queryset(self):
        """Return the last five published events."""
        return Event.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Event
    template_name = 'helping_hands_app/detail.html'


class ResultsView(generic.DetailView):
    model = Event
    template_name = 'helping_hands_app/results.html'


def vote(request, event_id):
    e = get_object_or_404(Event, pk=event_id)
    try:
        selected_choice = e.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the event voting form.
        return render(request, 'helping_hands_app/detail.html', {
            'event': e,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('helping_hands_app:results', args=(e.id,)))
