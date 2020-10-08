from django.test import TestCase
from django.urls import resolve, reverse
from blogs.views import index

# Test cases for urls.

class IndexUrlTest(TestCase):

    def setUp(self):
        # Setup data that'll be use in each test.
        self.url = reverse('blogs:index')

    def test_root_url_can_be_accept_by_name(self):
        self.assertEqual(self.url, '/')

    def test_root_url_use_correct_view(self):
        print(resolve(self.url))
        self.assertEqual(resolve(self.url).func, index)