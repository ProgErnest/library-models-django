from django import forms
from .models import Book,Author,Loan
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

class LoanForm(forms.ModelForm):
    # loan_date = forms.DateField(
    #     widget= forms.DateInput(attrs = {'type': 'date'})
    # )
    return_date = forms.DateField(
        widget= forms.DateInput(attrs = {'type': 'date'})
    )
    # effective_return_date = forms.DateField(
    #     widget= forms.DateInput(attrs = {'type': 'date'})
    # )
    class Meta:
        model = Loan
        fields = ['book','borrower','return_date','effective_return_date']