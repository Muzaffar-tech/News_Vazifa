from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from .models import News, Category
from .forms import RegisterForm, LoginForm
# Create your views here.



@login_required
def index(request):


    news_banner = News.objects.filter(is_active=True, is_banner=True)
    latest_news = News.objects.filter(is_active=True).order_by("-created")[:4]
    categories = Category.objects.all()

    context = {
        "latest_news":latest_news,
        "news_banner":news_banner,
        "categories":categories
    }
    return render(request, 'app/index.html', context)

def about(request):
    return render(request, 'app/about.html')

def blog_details(request):
    return render(request, 'app/blog_details.html')

def blog(request):
    return render(request, 'app/blog.html')

def category(request):
    return render(request, 'app/categori.html')

def contact(request):
    return render(request, 'app/contact.html')

def elements(request):
    return render(request, 'app/elements.html')

def latest_news(request):
    news = News.objects.filter(is_active=True).order_by("-created").first()

    context = {
        "news":news
    }
    return render(request, 'app/latest_news.html', context)

def detail(request):
    return render(request, 'app/detail.html')


def register(request: WSGIRequest):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Siz ro'yxatdan muvaffarqiyatli o'tdingiz!\n"
                                      f"Login parolni terib saytga kiring!")
            return redirect('login')
        else:
            print(form.error_messages, "**************")
    else:
        form = RegisterForm()
    context = {
        "form":form
    }

    return render(request, "register.html", context)


def user_login(request: WSGIRequest):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Saytga xush kelibsiz! {user.username}")
            return redirect("home")
    form = LoginForm()
    context={
        "form":form
    }
    return render(request, "login.html", context)

def user_logout(request):
    logout(request)
    messages.warning(request, f"Siz saytdan chiqdingiz!")
    return redirect("login")