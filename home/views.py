from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

from django.contrib import messages

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
    # if post method
    if request.method == "POST":
        # get parameters
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        if name and email and phone and desc:
            # If all form fields are not empty
            contact = Contact(
                name=name, email=email, phone=phone, desc=desc, date=datetime.today()
            )
            contact.save()
            messages.success(request, "Form successfully submitted!")
        else:
            # If any of the form fields are empty
            messages.error(request, "Please fill in all the form fields.")

    return render(request, "contact.html")
