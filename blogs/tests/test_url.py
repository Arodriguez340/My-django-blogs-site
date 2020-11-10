from django.test import TestCase
from django.urls import resolve, reverse
from blogs.models import Blog, Entry
from blogs.views import index, lastest_entries, blog

# Test cases for urls.

class IndexUrlTest(TestCase):

    def setUp(self):
        # Setup data that'll be use in each test.
        self.url = ('/')


    def test_index_url_can_resolve_to_index_view(self):
        self.assertEqual(resolve(self.url).func, index)

class LastestUrlTest(TestCase):

    def setUp(self):
        # Setup data that'll be use in each test.
        self.url = self.client.get('/lastest_entries/')

    def test_lastest_url_can_resolve_to_lastest_view(self):
        self.assertEqual(resolve(self.url).func, lastest_entries)

class BlogUrlTest(TestCase):
    def setUp(self):
        self.url = ('blog/1/')

    def test_blog_url_can_resolve_to_view(self):
        self.assertEqual(resolve(self.url).func, blog)

