from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseNotAllowed
from . import models
# Create your views here.

def book_list(request):
    books = models.Book.objects.all()
    return render(request, "core/book_list.html", {'books':books})   
def book_detail(request, pk):
    book = get_object_or_404(models.Book, id=pk)
    return render(request,"core/book_detail.html", {'book':book})

def book_create(request):
    if (request.method == "POST"):
        title = request.POST.get('title')
        isbn = request.POST.get('isbn')
        author_id = request.POST.get('author')
        
        summary = request.POST.get('sumary')
        available = request.POST.get('available')
        publish_date = request.POST.get('publication_date')
        final_author = get_object_or_404(models.Author,id=author_id)
        models.Book.objects.create(
            title=title,
            isbn=isbn,
            author=final_author,
            summary=summary,
            publication_date=publish_date,
            available=available
        )
        return redirect("get_all_books")
    elif (request.method == "GET"):
        authors = models.Author.objects.all()
        return render(request,"core/create_form.html",{"authors": authors})
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
            