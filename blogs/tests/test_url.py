from django.test import TestCase
from django.urls import resolve, reverse
from blogs.models import Blog, Entry
from blogs.views import index, lastest_entries, blogs, blog, entry, new_blog, new_entry, edit_entry

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
        self.url = ('/lastest_entries/')

    def test_lastest_url_can_resolve_to_lastest_view(self):
        self.assertEqual(resolve(self.url).func, lastest_entries)

class BlogsUrlTest(TestCase):
    def setUp(self):
        self.url = ('/blogs/')

    def test_blogs_url_can_resolve_to_view(self):
        self.assertEqual(resolve(self.url).func, blogs)

class BlogUrlTest(TestCase):
    def setUp(self):
        self.url = ('/blog/1/')

    def test_blog_url_can_resolve_to_view(self):
        self.assertEqual(resolve(self.url).func, blog)

class EntryUrlTest(TestCase):
    def setUp(self):
        self.url = ('/entry/1/')

    def test_entry_url_can_resolve_to_view(self):
        self.assertEqual(resolve(self.url).func, entry)

class NewBlogUrlTest(TestCase):
    def setUp(self):
        self.url = ('/new_blog/')

    def test_entry_url_can_resolve_to_view(self):
        self.assertEqual(resolve(self.url).func, new_blog)

class NewEntryUrlTest(TestCase):
    def setUp(self):
        self.url = ('/new_entry/1/')

    def test_entry_url_can_resolve_to_view(self):
        self.assertEqual(resolve(self.url).func, new_entry)

class EditEntryUrlTest(TestCase):
    def setUp(self):
        self.url = ('/edit_entry/1/')

    def test_entry_url_can_resolve_to_view(self):
        self.assertEqual(resolve(self.url).func, edit_entry)