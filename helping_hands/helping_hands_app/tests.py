# from django.core.management import setup_environ
# from ..helping_hands_site import settings

# setup_environ(settings)


import datetime

from django.utils import timezone
from django.test import TestCase

from helping_hands_app import models 
from models import Event


# class EventMethodTests(TestCase):

#     def test_was_published_recently_with_future_event(self):
#         """
#         was_published_recently() should return False for events whose
#         pub_date is in the future.
#         """
#         time = timezone.now() + datetime.timedelta(days=30)
#         future_event = Event(pub_date=time)

# self.assertEqual(future_event.was_published_recently(), False)


from selenium import webdriver
from views import register
import unittest



class RegistrationTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_open_registration_page(self):  
        found = resolve('/register')
        self.assertEqual(found.func, register)
        # self.browser.get('http://localhost:8000/register')
      
        # self.assertIn('User Registration', self.browser.title)  
        # self.fail('Finish the test!')  
    
    def test_registration_page_returns_correct_html(self):
     	request = HttpRequest() 
        response = home_page(request) 
        self.assertTrue(response.content.startswith(b'<html>')) 
        self.assertIn(b'<title>User Registration</title>', response.content) 
        self.assertTrue(response.content.endswith(b'</html>'))

if __name__ == '__main__':  
	unittest.main()  
#    unittest.main(warnings='ignore')  
