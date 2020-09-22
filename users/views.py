from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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
    content = {'form': form}
    return render(request, 'registration/register.html', content)
