from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import CreateUser,CreateCard
from .models import Card, User_likes
from django.views.generic import UpdateView

# Create your views here.

@login_required(login_url="/login")
def home(request):
    cards = Card.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("card_id")
        card = Card.objects.filter(id=post_id).first()
        
        if card and card.author == request.user:
            card.delete()
        
            

    return render(request,"main/index.html",{"cards":cards})


def like(request,card_id):
    info = User_likes(user_id=request.user.id,card_id=card_id)
    info.save()
    return redirect("/#add")

def likes(request):
    user_likes = User_likes.objects.filter(user_id=request.user.id)
    cards = Card.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("card_id")
        print(post_id)
        post = User_likes.objects.filter(card_id=post_id,user_id=request.user.id).first()
        if post:
            post.delete()


    return render(request,"main/likes.html",{"user_likes":user_likes,"cards":cards})

class Update(UpdateView):
    model = Card
    template_name = "main/update.html"

    fields = ["title","price",'img_url',"description"]


def logoutt(request):
    logout(request)
    
    return redirect('/login')
    
@login_required(login_url="/login")
def add_card(request):

    if request.method == "POST":
        form = CreateCard(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = CreateCard()

    return render(request,"main/add_card.html",{"form":form})

def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/home')
    
    return render(request, "main/login.html")

def sign_up(request):
    
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("/")
    else:
        form = CreateUser()
    
    return render(request,"main/sign_up.html",{"form":form})