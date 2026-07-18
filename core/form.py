from django import forms
from models import Author
class CreateBookForm(forms.Form):
    title = forms.CharField(50)
    isbn = forms.CharField(50)
    autor = forms.ChoiceField(choices=Author.objects.all())
    available = forms.BooleanField()
    summary = forms.Textarea()
