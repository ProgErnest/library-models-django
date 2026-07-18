from django import forms
from .models import Book,Author
class CreateBookForm(forms.ModelForm):
    publication_date = forms.DateField(
        widget=forms.DateInput(attrs = {'type': 'date'})
    )
    # summary = forms.Textarea()
    class Meta:
        model = Book
        fields = ['title','isbn','author','available','publication_date','summary']

class AuthorForm(forms.ModelForm):
    birthday = forms.DateField(
        widget= forms.DateInput(attrs = {'type': 'date'})
    )
    class Meta:
        model = Author
        fields = ['name','surname','birthday']