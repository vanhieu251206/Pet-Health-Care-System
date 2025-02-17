from django import forms
from .models import CustomUser

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'dob', 'phone', 'email', 'address', 'avatar']
