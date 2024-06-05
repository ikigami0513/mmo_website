from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'rounded-lg m-2 p-2', 'placeholder': 'Nom d\'utilisateur'})
        self.fields['email'].widget.attrs.update({'class': 'rounded-lg m-2 p-2', 'placeholder': 'Adresse mail'})
        self.fields['password1'].widget.attrs.update({'class': 'rounded-lg m-2 p-2', 'placeholder': 'Mot de passe'})
        self.fields['password2'].widget.attrs.update({'class': 'rounded-lg m-2 p-2', 'placeholder': 'Confirmation'})
        
        self.fields['username'].label = ''
        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        
        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        
class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'rounded-lg m-2 p-2', 'placeholder': 'Nom d\'utilisateur'}),
        label=""
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'rounded-lg m-2 p-2', 'placeholder': 'Mot de passe'}),
        label=""
    )
    
    class Meta:
        model = User
        fields = ('username', 'password')
        
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'rounded-lg m-2 p-2', 'placeholder': 'Adresse mail'}),
        label=""
    )