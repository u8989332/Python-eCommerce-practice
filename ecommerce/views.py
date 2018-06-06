from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ContactForm, LoginForm


def home_page(request):
    context = {
        "title" : "home la",
        "content" : "hhooommme"
    }
    return render(request, "home_page.html", context)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title" : "contact la",
        "content" : "contactcccccccccc",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('name'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    print(request.user.is_authenticated)
    
    if form.is_valid():
        print(request.user.is_authenticated)
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            return redirect("/login")
        else:
            print("Error")
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('name'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    context = {
        "form" : form
    }
    return render(request, "auth/login.html", context)


def home_page_old(request):
    return HttpResponse("Heeeeloo  world")