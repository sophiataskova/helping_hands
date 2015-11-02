from django.core.management import setup_environ
from helping_hands_site import settings

setup_environ(settings)

import fts.tests

fts.tests.main()