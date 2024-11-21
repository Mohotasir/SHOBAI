from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def homepage(request):
    """View function for the homepage"""
    return render(request, "homepage.html")


@login_required
def dashboard(request):
    """View function for the dashboard"""
    return render(request, "dashboard.html")
