from django.urls import path
from books.views import books

urlpatterns = [
    path('', books)
]
