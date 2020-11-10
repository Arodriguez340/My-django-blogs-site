from django.urls import path, re_path
from . import views

app_name = 'blogs'
urlpatterns = [
   # Home page
   path('', views.index, name='index'),
   # Page that show the lastest entries added to the site.
   path('lastest_entries/', views.lastest_entries, name='lastest_entries'),
   # Page that show all the register blogs.
   path('blogs/', views.blogs, name='blogs'),
   # Page that show a specific blog by its id(primary key).
   path('blog/<int:blog_id>/', views.blog, name='blog'),
   # Page that allow users add a new entry to they blogs.
   path('new_entry/<int:blog_id>/', views.new_entry,name='new_entry'),
   # Page to register a new blog.
   path('new_blog/', views.new_blog, name='new_blog'),
   # pag that show a specific view by it id(primary key).
   path('entry/<int:entry_id>/', views.entry, name='entry'),
   # Page that allows an user edit a blog entry.
   path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]