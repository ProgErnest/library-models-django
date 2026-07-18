from django.urls import path
from . import views
urlpatterns = [
    path('books/all/', views.book_list,name="get_all_books"),
    path('books/detail/<int:pk>/', views.book_detail,name="book_detail"),
    path('books/create/', views.book_create, name="create_book"),
    path('books/update/<int:pk>', views.book_update, name="update_book"),
    path('books/delete/<int:pk>/', views.book_delete, name="delete_book"),

    path('author/all/', views.list_authors, name="authors_list")
    
]
