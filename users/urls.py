from django.urls import path
from django.conf.urls import include
from users.views import dashboard, register


app_name = 'users'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register, name='register'),
]