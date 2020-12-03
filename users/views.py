from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.forms import UserProfileForm
from users.models import UserProfile

# Create your views here.
def dashboard(request):
    return render(request, 'users/dashboard.html')


def register(request):
    '''Register a new user'''
    if request.method != 'POST':
        #display blank registration form.
        form = UserCreationForm()
    else:
        # process completed.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Login and then redirect  to the home page.
            login(request, new_user)
            return redirect('users:dashboard')

    # display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

@login_required
def profile(request, pk):
    #user_profile = get_object_or_404(UserProfile, pk=pk)
    try:
        user_profile = UserProfile.objects.get(pk=pk)
    except:
        return redirect('users:new_profile', pk=pk)


    full_name = f'{user_profile.name} {user_profile.last_name}'
    user_name = request.user.username
    description = user_profile.description
    email = user_profile.email
    twitter = user_profile.twitter
    profile_img = user_profile.profile_img

    context = {
        'full_name': full_name,
        'user_name': user_name,
        'description': description,
        'email': email,
        'twitter': twitter,
        'profile_img': profile_img,
    }

    return render(request, 'users/profile.html', context)


@login_required
def new_profile(request, pk):
    '''Create a new user profile.'''
    user = User.objects.get(pk=pk)

    form = UserProfileForm(request.POST, request.FILES)

    if form.is_valid():
        new_profile = form.save(commit=False)
        new_profile.user = user
        new_profile.save()
        return redirect('users:profile', pk=pk)

    context = {'form': form}
    return render(request, 'users/new_profile.html', context)
    
@login_required
def edit_profile(request, pk):
    """Edit an existing profile."""
    profile = get_object_or_404(UserProfile, pk=pk)

    user = profile.user

    if request.method != "POST":
        # Initial request; pre-fill form with the current entry.
        form = UserProfileForm(instance=profile)
    else:
        # POST data submitted; process data.
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile', pk=pk)

    context = {"profile": profile, "user": user, "form": form}
    return render(request, "users/edit_profile.html", context)