from django import forms
from pets.models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']  
        widgets = {
            'password': forms.PasswordInput(),
        }
