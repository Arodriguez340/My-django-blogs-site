from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required


from .models import Entry, Blog
from .forms import BlogForm, EntryForm

def index(request):
    """Home page"""
    return render(request, 'blogs/index.html')


def lastest_entries(request):
    """ Show the lastest entries of the site."""
    try:
        entries = Entry.objects.order_by('-date_added') [:10] # the queryset only retrieve the last 10
    except Entry.DoesNotExist:
        raise Http404('No entry has been found!')  
    else:
        context = {'entries': entries}
    return render(request, 'blogs/lastest_entries.html', context)


def entry(request, entry_id):
    """Shows a single entry of an specific blog."""
    entry = get_object_or_404(Entry, pk=entry_id)

    title = entry.title
    text = entry.text
    blog = entry.blog
    img = entry.img
    tags = entry.tags.all()


    context = {
        'title': title,
        'text': text,
        'blog': blog,
        'tags': tags,
        'img': img,
        'entry_id': entry_id,
    }

    return render(request, 'blogs/entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    #entry = Entry.objects.get(id=entry_id)
    entry = get_object_or_404(Entry, pk=entry_id)

    blog = entry.blog

    _check_blog_owner(blog, request)

    if request.method != "POST":
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            form.save_m2m()
            return redirect('blogs:blog', blog_id=blog.id)

    context = {"entry": entry, "blog": blog, "form": form}
    return render(request, "blogs/edit_entry.html", context)


@login_required
def new_entry(request, blog_id):
    
    #blog = Blog.objects.get(id=blog_id)
    blog = get_object_or_404(Blog, pk=blog_id)

    _check_blog_owner(blog, request)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.blog = blog
            new_entry.save()
            form.save_m2m()
            return redirect('blogs:blog', blog_id=blog.id)

    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_entry.html', context)



def blogs(request):
    """Show the last 10 blogs available on the site."""
    try:
        blogs = Blog.objects.order_by('-date_added') [:10]
    except Blog.DoesNotExist:
        raise Http404('No blog has been found!')
    else:
        context = {'blogs': blogs}

    return render(request, 'blogs/blogs.html', context)


def blog(request, blog_id):
    """Show a single blog and its entries."""
    #blog = get_object_or_404(Blog, pk=blog_id)
    blog = Blog.objects.get(pk=blog_id)
    
    name = blog.name
    description = blog.description
    entries = blog.entry_set.order_by("-date_added")

    context = {
        'name': name,
        'description': description,
        'entries': entries,
        'blog_id': blog.id
    }

    return render(request, 'blogs/blog.html', context)

@login_required
def new_blog(request):

    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:blogs')

    context = {'form':form}
    return render(request, 'blogs/new_blog.html', context)


def _check_blog_owner(blog, request):
    if blog.owner != request.user:
        raise Http404
