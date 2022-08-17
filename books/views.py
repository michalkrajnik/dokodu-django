from django.shortcuts import render
from books.models import Book
# Create your views here.
from django.http import HttpResponse


def books(request):
    return HttpResponse("Here will be my library")
