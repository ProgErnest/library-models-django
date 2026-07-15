from django.db import models

# Create your models here.
class Book(models.Model):

    book_title = models.CharField(max_length=50)
    isbn = models.CharField(unique=True, max_length=50)
    publication_date = models.DateField()
    available = models.BooleanField(default=True)
    autor = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True )
    sumary = models.TextField(null=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["-publication_date"]

    def __str__(self):
        
        return self.title

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})
class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})


class Loan(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.CharField(max_length=50)
    loan_date = models.DateField(auto_now=False, auto_now_add=True)
    return_date = models.DateField(auto_now=False, auto_now_add=False)
    effective_return_date = models.DateField(null=True,auto_now=False, auto_now_add=False)
    

    class Meta:
        verbose_name = "loan"
        verbose_name_plural = "loans"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("loan_detail", kwargs={"pk": self.pk})

    def get_not_returned_books(self):
        return self.book.filter(effective_return_date = NULL)

