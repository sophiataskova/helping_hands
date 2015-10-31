import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Event


class EventMethodTests(TestCase):

    def test_was_published_recently_with_future_event(self):
        """
        was_published_recently() should return False for events whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_event = Event(pub_date=time)

self.assertEqual(future_event.was_published_recently(), False)
