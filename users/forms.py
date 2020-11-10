from django import forms
from users.models import UserProfile

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = [
            'name',
            'last_name',
            'description',
            'profile_img',
            'email',
            'twitter'
        ]