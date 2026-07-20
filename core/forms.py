from django import forms
from .models import Book,Author,Loan
class CreateBookForm(forms.ModelForm):
    # publication_date = forms.DateField(
    #     widget=forms.DateInput(attrs = {'type': 'date'})
    # )
    # summary = forms.Textarea()
    class Meta:
        model = Book
        fields = ['title','isbn','author','available','publication_date','summary']
        widgets= {
            'title': forms.TextInput(attrs={
                'class': 'w-full pl-9 pr-4 py-2.5 text-sm text-slate-800 bg-slate-50 border border-slate-200 rounded-lg shadow-xs placeholder:text-slate-400 placeholder:italic outline-none transition focus:border-indigo-400 focus:bg-white focus:ring-3 focus:ring-indigo-100',
                'placeholder': 'Ex : Le Petit Prince'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'w-full pl-9 pr-4 py-2.5 text-sm text-slate-800 bg-slate-50 border border-slate-200 rounded-lg shadow-xs placeholder:text-slate-400 placeholder:italic outline-none transition focus:border-indigo-400 focus:bg-white focus:ring-3 focus:ring-indigo-100',
                'placeholder': 'Ex : 978-3-16-148410-0'
            }),
            'author': forms.Select(attrs={
                'class': 'w-full pl-9 pr-4 py-2.5 text-sm text-slate-800 bg-slate-50 border border-slate-200 rounded-lg shadow-xs placeholder:text-slate-400 placeholder:italic outline-none transition focus:border-indigo-400 focus:bg-white focus:ring-3 focus:ring-indigo-100',
            }),
            'available': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 accent-indigo-500 rounded cursor-pointer shrink-0',
                'checked': False
            }),
            'publication_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full pl-9 pr-4 py-2.5 text-sm text-slate-700 bg-slate-50 border border-slate-200 rounded-lg shadow-xs outline-none transition focus:border-indigo-400 focus:bg-white focus:ring-3 focus:ring-indigo-100'
            }),
            'summary': forms.Textarea(attrs={
                'class': 'w-full pl-9 pr-4 py-2.5 text-sm text-slate-800 bg-slate-50 border border-slate-200 rounded-lg shadow-xs placeholder:text-slate-400 placeholder:italic outline-none transition focus:border-indigo-400 focus:bg-white focus:ring-3 focus:ring-indigo-100',
                'placeholder': 'Ex : 978-3-16-148410-0'
            }),
        }

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
