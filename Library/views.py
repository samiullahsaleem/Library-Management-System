from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import AuthorForm, BookForm
from .models import Author, Book
# Create your views here.

@login_required(login_url=reverse_lazy('loginform'),redirect_field_name='next')
def addNewBook(request):
    if request.method == 'POST':
        authorform = AuthorForm(request.POST)
        bookform = BookForm(request.POST)
        if authorform.is_valid() and bookform.is_valid():
            author = Author(Author=request.POST['Author'])
            author.save()
            book = Book(Author=author, title=request.POST['title'], genre=request.POST['genre'], price=request.POST['price'], isbn=request.POST['isbn'])
            book.save()
            return render(request, "Library/home.html")
    else:
        authorform = AuthorForm()
        bookform = BookForm()
        return render(request, 'Library/addnewbook.html', {'authorform': authorform, 'bookform': bookform})
@login_required(login_url=reverse_lazy('loginform'),redirect_field_name='next')
def editBook(request, pk):
    try: 
        book = Book.objects.get(BookId=pk)
    except:
        return render(request, 'Library/home.html')
    if request.method == 'POST':
        Author = request.POST.get('Author')
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        price = request.POST.get('price')
        isbn = request.POST.get('isbn')

        # Update book object with new values

        book.title = title
        book.genre = genre
        book.price = price
        book.isbn = isbn
        book.save()
        return render(request, 'Library/home.html')
    else:
        authorform = AuthorForm(initial={'Author': book.Author})
        bookform = BookForm(initial={'title': book.title, 'genre': book.genre, 'price': book.price, 'isbn': book.isbn})
        return render(request, 'Library/editbook.html', {'authorform': authorform, 'bookform': bookform, 'book': book})
@login_required(login_url=reverse_lazy('loginform'),redirect_field_name='next')
def deleteBook(request, pk):
    try: 
        book = Book.objects.get(BookId=pk)
    except:
        return render(request, 'Library/home.html')
    if request.method == 'POST':
        book.delete()
        return render(request, 'Library/home.html')
    else:
        return render(request, 'Library/deletebook.html', {'book': book})


def searchBook(request):
    if request.method == 'POST':
        title = request.POST['title']
        books = Book.objects.filter(title__icontains=title)
        return render(request, 'Library/home.html', {'books': books})
    else:
        return render(request, 'Library/home.html')

