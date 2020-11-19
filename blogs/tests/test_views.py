from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from blogs.models import Blog, Entry
from blogs.views import index, lastest_entries

'''Test suit for the blogs app.
before testing adjucts souce code in views like, login requirement decorators, and chech of blogs' owners.'''

class IndexViewTest(TestCase):

    def test_index_page_return_correct_html(self):
        url = self.client.get('/')

        self.assertTemplateUsed(url, 'blogs/index.html')
        self.assertTemplateUsed(url, 'base.html')
        self.assertEqual(url.status_code, 200)


class LastestEntriesViewTest(TestCase):

    def setUp(self):
        entries = [Entry()] * 4 # create four intance of Enty and stores them in a list.
        self.url = self.client.get('/lastest_entries/', {'entries': entries})

    def test_lastest_page_return_correct_html(self):
        self.assertTemplateUsed(self.url, 'blogs/lastest_entries.html')
        self.assertTemplateUsed(self.url, 'base.html')

    def test_lastes_page_status(self):
        self.assertEqual(self.url.status_code, 200)


class BlogsViewTest(TestCase):

    def setUp(self):
        blogs = [Blog()] * 4 # create four intances of Blog pointing to the same object.
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


class NewBlogViewTest(TestCase):
    '''Before runnig the adjucts view code like user login check, that redirect user to a register page if it doesn't have a account.'''
    
    def setUp(self):
        self.url = self.client.get('/new_blog/')

    def test_new_blog_view_return_correct_html(self):
        self.assertTemplateUsed(self.url, 'blogs/new_blog.html')
        self.assertTemplateUsed(self.url, 'base.html')

    def test_display_form(self):
        self.assertContains(self.url, 'Add a new blog')
    
    def test_new_blog_page_status(self):
        self.assertEqual(self.url.status_code, 200)

    def test_can_save_a_POST_request(self):

        response = self.client.post('/new_blog/', {'name': 'the cool blog', 'description': 'cool description'}) # sent data to the view.

        self.assertEqual(Blog.objects.count(), 1)
        new_blog = Blog.objects.first()
        self.assertEqual(new_blog.name, 'the cool blog')

        self.assertEqual(response.status_code, 302)       # check redirec status after saving the data.
        self.assertEqual(response['location'], '/blogs/') # check new location after redirect.


class NewEntryViewTest(TestCase):
    
    def setUp(self):
        user = User.objects.create(username='cooluser', password='12345')
        self.blog = Blog.objects.create(name='cool blog', description='cool description', owner=user)
        self.url = self.client.get(f'/new_entry/{self.blog.id}/')

    def test_new_entry_view_return_correct_html(self):
        self.assertTemplateUsed(self.url, 'blogs/new_entry.html')
        self.assertTemplateUsed(self.url, 'base.html')

    def test_display_form(self):
        self.assertContains(self.url, 'Add a new entry')
    
    def test_new_entry_page_status(self):
        self.assertEqual(self.url.status_code, 200)

    def test_can_save_a_POST_request(self):

        response = self.client.post(f'/new_entry/{self.blog.id}/', {'title': 'the cool title', 'text': 'cool text'})
        # make small changes in view before testing like remove user login check.
        self.assertEqual(Entry.objects.count(), 1)
        new_entry = Entry.objects.first()
        self.assertEqual(new_entry.title, 'the cool title')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], f'/blog/{self.blog.id}/')


class EditNewEntryViewTest(TestCase):
    
    def setUp(self):
        user = User.objects.create(username='cooluser', password='12345')
        blog = Blog.objects.create(name='cool blog', description='cool description', owner=user)
        self.entry = Entry.objects.create(title='the cool title', text='cool text', blog=blog)
        self.url = self.client.get(f'/edit_entry/{self.entry.id}/')

    def test_new_entry_view_return_correct_html(self):
        self.assertTemplateUsed(self.url, 'blogs/edit_entry.html')
        self.assertTemplateUsed(self.url, 'base.html')

    def test_display_form(self):
        self.assertContains(self.url, 'Edit entry')
        self.assertContains(self.url, 'the cool title')
        self.assertContains(self.url, 'cool text')
    
    def test_new_entry_page_status(self):
        self.assertEqual(self.url.status_code, 200)

    def test_can_save_a_POST_request(self):

        response = self.client.post(f'/edit_entry/{self.entry.id}/', {'title': 'the cool title2', 'text': 'cool text2'})
        # make small changes in view before testing like remove user login check.
        edited_entry = Entry.objects.first()
        self.assertEqual(edited_entry.title, 'the cool title2')
        self.assertEqual(edited_entry.text, 'cool text2')

        self.assertEqual(response.status_code, 302)
        blog = self.entry.blog
        self.assertEqual(response['location'], f'/blog/{blog.id}/')