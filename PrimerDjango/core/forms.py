from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. 3-50 characters.', label='first_name', widget=forms.TextInput(attrs={'id': 'first_name', 'name': 'first_name'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. 3-50 characters.', label='last_name', widget=forms.TextInput(attrs={'id': 'last_name', 'name': 'last_name'}))
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.', label='email', widget=forms.EmailInput(attrs={'id': 'email', 'name': 'email'}))
    address = forms.CharField(max_length=200, required=False, help_text='Optional. Enter your address.', label='address', widget=forms.TextInput(attrs={'id': 'address', 'name': 'address'}))
    birthdate = forms.DateField(required=True, help_text='Required. Format: YYYY-MM-DD', label='birthdate', widget=forms.DateInput(attrs={'type': 'date', 'id': 'birthdate', 'name': 'birthdate'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'birthdate', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'id': 'first_name', 'name': 'first_name'})
        self.fields['last_name'].widget.attrs.update({'id': 'last_name', 'name': 'last_name'})
        self.fields['username'].widget.attrs.update({'id': 'username', 'name': 'username'})
        self.fields['email'].widget.attrs.update({'id': 'email', 'name': 'email'})
        self.fields['password1'].widget.attrs.update({'id': 'password1', 'name': 'password1'})
        self.fields['password2'].widget.attrs.update({'id': 'password2', 'name': 'password2'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            """ Assuming you have a profile model to save additional fields
            user.Cliente.direccion = self.cleaned_data['address']
            user.Cliente.nacimiento = self.cleaned_data['birthdate']
            user.Cliente.save()
            """
        return user
