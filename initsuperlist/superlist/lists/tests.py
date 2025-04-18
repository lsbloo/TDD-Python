from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):

    ## check if new url /home/ is resolved from framework and home_page function views is attached
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/home/')
        self.assertEqual(found.func, home_page)

    ## should return html content page correct from home_page function view attached
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
        

 

    
