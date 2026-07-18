from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseNotAllowed
from . import models
from .forms import CreateBookForm
# Create your views here.

def book_list(request):
    books = models.Book.objects.all()
    return render(request, "core/book_list.html", {'books':books})   
def book_detail(request, pk):
    book = get_object_or_404(models.Book, id=pk)
    return render(request,"core/book_detail.html", {'book':book})

def book_create(request):
    if (request.method == "POST"):
        form = CreateBookForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("get_all_books")

    elif (request.method == "GET"):
        form = CreateBookForm()
        return render(request,"core/create_form.html",{"form": form})
    else:
        return HttpResponseNotAllowed()

# @csrf_exempt
def book_delete(request,pk):
    if request.method == 'POST':
        book = get_object_or_404(models.Book,id=pk)
        book.delete()
        return redirect("get_all_books")
    else:
        return HttpResponseNotAllowed(['POST'])
            