from django import forms

class AuthorForm(forms.Form):
    Author = forms.CharField(max_length=100)

class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
    genre = forms.CharField(max_length=100)
    price = forms.FloatField()
    isbn = forms.CharField(max_length=100)

