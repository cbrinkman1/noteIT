from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from django.shortcuts import get_object_or_404
from django.utils import timezone



def index(request):
    username = None
    lastest_notes_list = None
    if request.user.is_authenticated:
        username = request.user.username
        lastest_notes_list = Note.objects.filter(creator=request.user).order_by("category", "-pubDate")
    template = loader.get_template("users/index.html")
    
    context = {"latest_notes_list": lastest_notes_list, "username":username}
    return render(request, "users/index.html", context)
    
def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    access = False
    if request.user.is_authenticated:
        if request.user == note.creator:
            access = True
    context = {"note":note, "access":access}
    return render(request, "users/detail.html", context)
    
def create(request):
    if request.method == 'POST':
        noteTitle = request.POST["title"]
        noteText = request.POST["note"]
        color = request.POST["color"]
        colorR = 0
        colorG = 0
        colorB = 0
        if color == "red":
            colorR = 255
        elif color == "yellow":
            colorR = 255
            colorG = 255
        elif color == "green":
            colorR = 50
            colorG = 205
            colorB = 50
        elif color == "blue":
            colorR = 137
            colorG = 207
            colorB = 240
        elif color == "pink":
            colorR = 238
            colorG = 142
            colorR = 223
        category = request.POST["category"]
        if request.user.is_authenticated:
            username = request.user.username
            newNote = Note(noteTitle=noteTitle, noteText=noteText, pubDate=timezone.now(), category=category, creator=request.user, colorR=colorR, colorG=colorG, colorB=colorB)
            newNote.save()
            return redirect('/users/')
            
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    context = {"username":username}
    return render(request, "users/create.html", context)
    
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/users/')
    context = {'loginform':form}
    return render(request, "users/login.html", context)
    
def logout(request):
    auth.logout(request)
    return redirect("/users/")
    
def new(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print("here")
            form.save()
            return redirect("/users/")
        else:
            print("Errors: ", form.errors)
    context = {"registerform": form}
    return render(request, "users/new.html", context)
