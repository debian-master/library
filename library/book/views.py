from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Book
from .forms import BookCreateForm

class BookCreateView(CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'book/book-create.html'
    success_url = reverse_lazy('book_listing')



class BookListing(ListView):
    model = Book
    template_name = 'book/book-listing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context