from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Book(models.Model):

    title = models.CharField(_("title"), max_length = 50)
    subtitle = models.CharField(_("subtitle"), max_length = 50)
    isbn = models.CharField(_("isbn"), unique = True, max_length = 50)
    language = models.CharField(_("language"),max_length = 50)
    genre = models.CharField(_("genre"), max_length = 50)
    num_pages = models.PositiveIntegerField(_("number of pages"))
    publication_date = models.DateField(_("publication date"))
    available = models.BooleanField(default = True)
    author = models.ForeignKey("author", on_delete = models.SET_NULL, null = True,verbose_name = _("author"))

    summary = models.TextField(_("summary"), null = True, blank = True)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):       
        return self.title


class Author(models.Model):

    name = models.CharField(_("name"), max_length=50)
    surname = models.CharField(_("surname"), max_length=50)
    birthday = models.DateField(_("birthday"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

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



