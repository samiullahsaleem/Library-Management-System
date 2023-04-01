from django import forms


class UserRegisterForm(forms.Form):
    email = forms.EmailField()
    fullname = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(max_length=20)

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

