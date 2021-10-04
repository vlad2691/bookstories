from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView, LoginRequiredMixin):
    model = Book
    context_object_name = 'books'
    template_name = 'book/book_list.html'
    login_url = 'account_login'


class BookDetailView(DetailView, LoginRequiredMixin):
    model = Book
    template_name = 'book/book_detail.html'
    login_url = 'account_login'