from django.urls import path, re_path
from . import views

app_name = 'blogs'
urlpatterns = [
   # Home page
   path('', views.index, name='index'),
     # Page that show all the register blogs.
   path('blogs/', views.blogs, name='blogs'),
   # Page that show the lastest entries added to the site.
   path('lastest_entries/', views.lastest_entries, name='lastest_entries'),
   # Page to register a new blog.
   path('new_blog/', views.new_blog, name='new_blog'),
   # Page that show a specific blog by its id(primary key).
   path('blog/<int:pk>/', views.blog, name='blog'),
   # Page that confir delete of a Blog
   path('delete_blog/<int:pk>/', views.delete_blog, name="delete_blog"),
   # Page that allow users add a new entry to they blogs.
   path('new_entry/<int:pk>/', views.new_entry,name='new_entry'),
   # pag that show a specific view by it id(primary key).
   path('entry/<int:pk>/', views.entry, name='entry'),
   # Page that allows an user edit a blog entry.
   path('edit_entry/<int:pk>/', views.edit_entry, name='edit_entry'),
   # Page that confirm delete of an extiting entry
   path('delete_entry/<int:pk>/', views.delete_entry, name='delete_entry')
]