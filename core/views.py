from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseNotAllowed
from . import models
from .forms import CreateBookForm,AuthorForm
# Create your views here.

def book_list(request):
    books = models.Book.objects.all()
    return render(request, "core/book_list.html", {'books':books})   

def book_detail(request, pk):
    book = get_object_or_404(models.Book, id = pk)
    return render(request,"core/book_detail.html", {'book' : book})

def book_create(request):
    if (request.method == "POST"):
        form = CreateBookForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("get_all_books")

    elif (request.method == "GET"):
        form = CreateBookForm()
        return render(request,"core/create_form.html",{"form" : form})
    else:
        return HttpResponseNotAllowed()

def book_update(request, pk):
    book = get_object_or_404(models.Book,id=pk)
    if (request.method == "POST"):
        form = CreateBookForm(request.POST, instance = book)
        if(form.is_valid()):
            form.save()
            return redirect("get_all_books")
    else:
        form = CreateBookForm(instance = book)
        return render(request,"core/create_form.html",{"form": form})



def book_delete(request,pk):
    if request.method == 'POST':
        book = get_object_or_404(models.Book,id=pk)
        book.delete()
        return redirect("get_all_books")
    else:
        return HttpResponseNotAllowed(['POST'])
            

# Sections for Autors

def list_authors(request):
    if request.GET.get('q') != None:
        search = request.GET.get('q')
        authors = models.Author.objects.filter(name__icontains = search)
    else:
        authors = models.Author.objects.all()
    return render(request, "core/authors.html", {"authors" : authors})

def detail_author(request,pk):
    author = get_object_or_404(models.Author, id = pk)
    books = author.book_set.all()
    return render(request,"core/detail_author.html",{"author": author, "books": books})

def create_author(request):
    if (request.method == "POST"):
        author_form = AuthorForm(request.POST)
        if(author_form.is_valid()):
            author_form.save()
            return redirect("authors_list")
    else:
        author_form = AuthorForm()
        return render(request,"core/author_form.html",{"author_form": author_form})
def update_author(request, pk):
    author = get_object_or_404(models.Author, id=pk)
    if (request.method == "POST"):
        author_form = AuthorForm(request.POST, instance=author)
        if(author_form.is_valid()):
            author_form.save()
            return redirect("authors_list")
    else:
        author_form = AuthorForm(instance=author)
        return render(request,"core/author_form.html",{"author_form": author_form})
    
def delete_author(request,pk):
    if(request.method == "POST"):
        author = get_object_or_404(models.Author, id=pk)
        author.delete(id=pk)
        return redirect("author_list")
    else:
        return HttpResponseNotAllowed(['POST'])
    

## Views from Loans

def list_loans(request):
    loans = models.Loan.objects.all()
    return render(request, "core/loans_list.html",{"loans": loans})

def detail_loan(request, pk):
    loan = get_object_or_404(models.Loan, id=pk)
    return render(request, "core/loan_detail.html", {"loan":loan})
