from django.shortcuts import render


def homepage(request):
    """View function for the homepage"""
    return render(request, "homepage.html")
