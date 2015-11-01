"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        
        # Tests that 1 + 1 always equals 2.
        
        self.assertEqual(1 + 1, 2)

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

browser.quit()
"""

from selenium import webdriver
from helping_hands_app.views import register
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


