from django.test import TestCase
from blogs.models import Blog, Entry
from django.contrib.auth.models import User

class BlogModelTest(TestCase):

    def test_saving_and_retrieving_blogs(self):
        user = User.objects.create(username='user1', password='12345')
        blog1 = Blog.objects.create(name='blog1', description='text', owner=user)
        blog2 = Blog.objects.create(name='blog2', description='text', owner=user)

        blogs = Blog.objects.all()
        
        self.assertEqual(blogs.count(), 2)

        first_blog = blogs[0]
        second_blog = blogs[1]
        self.assertEqual(first_blog.name, 'blog1')
        self.assertEqual(second_blog.name, 'blog2')


class EntryModelTest(TestCase):

    def test_saving_and_retrieving_entries(self):
        user = User.objects.create(username='user1', password='12345')
        blog1 = Blog.objects.create(name='blog1', description='text', owner=user)
        entry1 = Entry.objects.create(title='entry1', text='text', blog=blog1)
        entry2 = Entry.objects.create(title='entry2', text='text1', blog=blog1)

        entries = Entry.objects.all()
        
        self.assertEqual(entries.count(), 2)

        first_entry =  entries[0]
        second_entry = entries[1]
        self.assertEqual(first_entry.title, 'entry1')
        self.assertEqual(second_entry.title, 'entry2')