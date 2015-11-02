from django.contrib.auth.models import User
from django.core.management import setup_environ
from hepling_hands_site import settings

setup_environ(settings)

user = User.objects.create_user('paul', 'mccartney@thebeatles.com', 'paulpassword')

user.last_name = 'Mccartney'

user.save()

print user.last_name
