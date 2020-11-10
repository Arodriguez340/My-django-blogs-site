from django.urls import path
from django.conf.urls import include
from . import views


app_name = 'users'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('new_profile/', views.new_profile, name='new_profile'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('edit_profile/<int:user_id>', views.edit_profile, name='edit_profile'),
]