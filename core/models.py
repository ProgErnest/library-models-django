from django.db import models

# Create your models here.
class Book(models.Model):

    title = models.CharField(max_length=50)
    isbn = models.CharField(unique=True, max_length=50)
    publication_date = models.DateField()
    available = models.BooleanField(default=True)
    author = models.ForeignKey("author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["-publication_date"]

    def __str__(self):       
        return self.title


class Author(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name


class Loan(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.CharField(max_length=50)
    loan_date = models.DateField(auto_now=False, auto_now_add=True)
    return_date = models.DateField(auto_now=False, auto_now_add=False)
    effective_return_date = models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False)
    

    class Meta:
        verbose_name = "loan"
        verbose_name_plural = "loans"

    def __str__(self):
        return f"{self.book.title} borrowed by {self.borrower}"



