from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from book.serializers import BookSerializer
from .models import Book
from .forms import BookCreateForm

# This is written in RESTAPIs

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny, )


class BookListing(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    queryset = None
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.get(id=self.kwargs['pk'])


## This commented code is written in Django generic Views

# class BookCreateView(CreateView):
#     model = Book
#     form_class = BookCreateForm
#     template_name = 'book/book-create.html'
#     success_url = reverse_lazy('book_listing')

# class BookListing(ListView):
#     model = Book
#     template_name = 'book/book-listing.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['books'] = Book.objects.all()
#         return context