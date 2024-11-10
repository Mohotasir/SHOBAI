from django.shortcuts import render

# Create your views here.


def storeUser(request):
    return render(request, "store_user.html")
