from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.models import User
from blogs.models import Blog, Entry
from blogs.views import index, lastest_entries

# Test cases for web views.

class IndexViewTest(TestCase):

    def test_index_page_return_correct_html(self):
        url = self.client.get('/')

        self.assertTemplateUsed(url, 'blogs/index.html')
        self.assertTemplateUsed(url, 'base.html')
        self.assertEqual(url.status_code, 200)

class LastestEntriesViewTest(TestCase):

    def setUp(self):
        entries = [Entry()] * 4
        self.url = self.client.get('/lastest_entries/', {'entries': entries})

    def test_lastest_page_return_correct_html(self):
        self.assertTemplateUsed(self.url, 'blogs/lastest_entries.html')
        self.assertTemplateUsed(self.url, 'base.html')

    def test_lastes_page_status(self):
        self.assertEqual(self.url.status_code, 200)


class BlogsViewTest(TestCase):

    def setUp(self):
        blogs = [Blog()] * 4
        self.url = self.client.get('/blogs/', {'blogs': blogs})

    def test_blogs_page_return_correct_html(self):
        self.assertTemplateUsed(self.url, 'blogs/blogs.html')
        self.assertTemplateUsed(self.url, 'base.html')

    def test_blogs_page_status(self):
        self.assertEqual(self.url.status_code, 200)


class BlogViewTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='test_user01', password='123456')
        blog = Blog.objects.create(name='Test-view', description='some text', owner=user)

        self.url = self.client.get(f'/blog/{blog.id}/')

    def test_blog_page_return_correct_html(self):
        self.assertTemplateUsed(self.url, 'blogs/blog.html')
        self.assertTemplateUsed(self.url, 'base.html')
    
    def test_display_blog(self):
        self.assertContains(self.url ,'some text')

    def test_blog_page_status(self):
        self.assertEqual(self.url.status_code, 200)


class EntryViewTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='test_user01', password='123456')
        blog = Blog.objects.create(name='Test-view', description='some text', owner=user)
        entry = Entry.objects.create(title='testing app', text='entry test', blog=blog)

        self.url = self.client.get(f'/entry/{entry.id}/')

    def test_blog_page_return_correct_html(self):
        self.assertTemplateUsed(self.url, 'blogs/entry.html')
        self.assertTemplateUsed(self.url, 'base.html')
    
    def test_display_blog(self):
        self.assertIn('entry test', self.url.content.decode())

    def test_blog_page_status(self):
        self.assertEqual(self.url.status_code, 200)
