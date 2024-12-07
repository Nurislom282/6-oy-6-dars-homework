from django.urls import path
from .views import main,about_us,contact,books_by_category,book_detail

urlpatterns = [
    path('',main,name='main'),
    path('category/<int:category_id>/',books_by_category,name='books_by_category'),
    path('books/<int:pk>/',book_detail,name='detail'),
    path('about_us/',about_us,name='about_us'),
    path('contacts/',contact,name='contact')
]