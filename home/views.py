from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    # context = {"variable": "AbhishekBhujel", "variable2": "Lucky"}
    return render(request, "index.html")
    # return HttpResponse("Welcome to Bhujel App Developers")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    return render(request, "contact.html")


