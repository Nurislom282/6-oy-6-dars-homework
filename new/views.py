from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import Category,Book

categoryes = Category.objects.all()
books = Book.objects.all()

context = {
    "categoryes":categoryes,
    "books":books
}
def main(request :WSGIRequest):
    return render(request,'index.html',context)

def books_by_category(request :WSGIRequest,category_id):
    categoryes_2 = Category.objects.all()
    books_2 = Book.objects.filter(category_id=category_id)
    context_for_books_in_category ={
        "categoryes":categoryes_2,
        'books':books_2
    }
    return render(request,'index.html',context_for_books_in_category)


def book_detail(request :WSGIRequest,pk):
    book_3 = Book.objects.get(pk=pk)
    context = {
        "book":book_3
    }
    return render(request,'Detail.html',context)

def about_us(request :WSGIRequest):
    return render(request,'about_us.html',context)

def contact(request: WSGIRequest):
    return render(request,'contacts.html',context)

