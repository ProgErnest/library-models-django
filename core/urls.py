from django.urls import path
from . import views
urlpatterns = [
    path('books/all/', views.book_list,name="get_all_books"),
    path('books/detail/<int:pk>/', views.book_detail,name="book_detail"),
    path('books/create/', views.book_create, name="create_book"),
    path('books/update/<int:pk>', views.book_update, name="update_book"),
    path('books/delete/<int:pk>/', views.book_delete, name="delete_book"),

    path('author/all/', views.list_authors, name="authors_list"),
    path('author/detail/<int:pk>/', views.detail_author, name="detail_author"),
    path('author/create/', views.create_author, name="create_author"),
    path('author/update/<int:pk>/', views.update_author, name="update_author"),
    path('author/delete/<int:pk>/', views.delete_author, name="delete_author"),
    
    path('loans/all/', views.list_loans, name="loan_list"),
    path('loans/detail/<int:pk>/', views.detail_loan, name="detail_loan"),
    path('loans/create/', views.initiate_loan, name="initiate_loan"),
    path('loans/update/<int:pk>/', views.update_loan, name="update_loan"),
    path('loans/delete/<int:pk>/', views.delete_loan, name="delete_loan"),
    
]
