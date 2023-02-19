from django import forms

class AuthUser(forms.Form):
    username = forms.CharField(max_length=30, help_text="username")
    password = forms.CharField(max_length=30, help_text="password")