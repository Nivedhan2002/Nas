from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from app1.models import uploadMForm, uploadForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "Mform.html", {'myform':uploadMForm(), "names":uploadForm.objects.all()})

def formpage(request):
    return render(request, "Mform.html", {'myform':uploadMForm(), "names":uploadForm.objects.all()})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"login.html", {"message":"Invalid credentials"})
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message":"logged out"})

def aftersubmit(request):
    if request.method == 'POST':
        my_form = uploadMForm(request.POST, request.FILES)
        if my_form.is_valid():
            my_form.save()
    return HttpResponseRedirect("/app1/formpage/")