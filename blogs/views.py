from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Entry, Blog
from .forms import BlogForm, EntryForm


def index(request):
    """Home page"""
    return render(request, 'blogs/index.html')
    

def blogs(request):
    """Show the last 10 blogs available on the site."""
    try:
        blogs = Blog.objects.order_by('-date_added') [:10]
    except Blog.DoesNotExist:
        raise Http404('No blog has been found!')
    else:
        context = {'blogs': blogs}

    return render(request, 'blogs/blogs.html', context)


def lastest_entries(request):
    """ Show the lastest entries of the site."""
    try:
        entries = Entry.objects.order_by('-date_added') [:10] # the queryset only retrieve the last 10
    except Entry.DoesNotExist:
        raise Http404('No entry has been found!')  
    else:
        context = {'entries': entries}
    return render(request, 'blogs/lastest_entries.html', context)


def new_blog(request):
    # before testing comment out user authenticate 
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/users/register/', request.path))
    else:
        if request.method != 'POST':
            form = BlogForm()
        else:
            form = BlogForm(request.POST)
            if form.is_valid():
                new_blog = form.save(commit=False)
                new_blog.owner =  request.user # for testing use User.objects.create(username='user', password='pass')
                new_blog.save()
                return redirect('blogs:blogs')

    context = {'form':form}
    return render(request, 'blogs/new_blog.html', context)


def blog(request, pk):
    """Show a single blog and its entries.
    take an blog_id or primaty key as positinal argument."""
    blog = get_object_or_404(Blog, pk=pk)
    
    name = blog.name
    description = blog.description
    entries = blog.entry_set.order_by("-date_added")

    context = {
        'blog':blog,
        'name': name,
        'description': description,
        'entries': entries,
    }

    return render(request, 'blogs/blog.html', context)

@login_required
def delete_blog(request, pk):
    # try to retreive blog or return 404 error
    obj = get_object_or_404(Blog, pk=pk)

    _check_blog_owner(obj, request)

    if request.method == 'POST':
        # delete object
        obj.delete()
        # after deleting redirect to blogs section
        return redirect('blogs:blogs')

    return render(request, 'blogs/delete_obj.html', {'object': obj})


@login_required
def new_entry(request, pk):
    '''View that takes an blog_id as parameter and return a form that allows user to create a new entry for a given blog.'''
    blog = get_object_or_404(Blog, pk=pk)

    _check_blog_owner(blog, request) # comment out before testing.

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.blog = blog
            new_entry.save()
            form.save_m2m()
            return redirect('blogs:blog', pk=pk)

    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_entry.html', context)


def entry(request, pk):
    """Shows a single entry of an specific blog."""
    entry = get_object_or_404(Entry, pk=pk)

    title = entry.title
    text = entry.text
    blog = entry.blog
    img = entry.img
    tags = entry.tags.all()


    context = {
        'entry': entry,
        'title': title,
        'text': text,
        'blog': blog,
        'tags': tags,
        'img': img,
    }

    return render(request, 'blogs/entry.html', context)


@login_required
def edit_entry(request, pk):
    """Edit an existing entry. take a entry id as parameter and return a form with the data of an exiting entry."""
    entry = get_object_or_404(Entry, pk=pk)

    blog = entry.blog

    _check_blog_owner(blog, request) # comment out before testing

    if request.method != "POST":
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            form.save_m2m()
            return redirect('blogs:blog', pk=pk)

    context = {"entry": entry, "blog": blog, "form": form}
    return render(request, "blogs/edit_entry.html", context)


@login_required
def delete_entry(request, pk):
    # try to retreive blog or return 404 error
    obj = get_object_or_404(Entry, pk=pk)

    _check_blog_owner(obj, request)
    
    if request.method == 'POST':
        # delete object
        obj.delete()
        # after deleting redirect to blogs section
        return redirect('blogs:blog', pk=obj.blog.id)

    return render(request, 'blogs/delete_obj.html', {'object': obj})


def _check_blog_owner(blog, request):
    if blog.owner != request.user:
        raise Http404
