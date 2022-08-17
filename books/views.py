from django.shortcuts import render


from django.http import HttpResponse


def books(request):
    return HttpResponse("Here will be my library")


