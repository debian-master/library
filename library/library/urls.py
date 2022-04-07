"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from auth1.views import SignupView
from book.views import BookCreateView, BookListing, BookUpdateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignupView.as_view(), name='signup_view'),
    path('book/create/', BookCreateView.as_view(), name='book_create_view'),
    path('books/', BookListing.as_view(), name='book_listing'),
    path('book/<int:pk>/edit', BookUpdateView.as_view(), name='book_update'),

]
