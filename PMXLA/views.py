from django.shortcuts import render, redirect
from urllib.parse import urlencode
from django.contrib.auth import login, authenticate, logout, get_user, get_user_model
from django.contrib.auth import update_session_auth_hash #Cập nhật hash của session để tránh đăng xuất người dùng sau khi thay đổi mật khẩu.
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

from .models import *
# Create your views here.
def loginpage(request):
    return render(request, 'Front/login.html')

def signuppage(request):
    return render(request, 'Front/signup.html')

def homepage(request):
    return render(request, "Home/home.html")

def userpage(request):
    return render(request, "Back/userpage.html")

def mainpage(request):
    return render(request, "Front/mainpage.html")

def xylyanhpage(request):
    if request.method == "post":
        image = request.POST.get("image")
        if image:
            return render(request, 'Home/xylyanh.html')
        else:
            return redirect("homepage")
    else:
        return redirect("homepage")

def loginXLA(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is None:

            messages.error(request, "Invalied Username or Password, try again!")
            return redirect("loginpage")
        else:
            login(request, user)
            return redirect("homepage")

    else:
        return redirect("loginpage")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Validate inputs
        if not all([username, password, confirm_password]):
            messages.warning(request, "All fields are required.")
            return redirect("signuppage")

        # Check username availability
        if UserAlexa.objects.filter(username=username).exists():
            messages.warning(request, """Username has been used, 
                            please choose another username.""")
            return redirect("signuppage")

        # Verify passwords match
        if password != confirm_password:
            messages.warning(request, """Confirm Password does not match Password, 
                            please try again.""")
            return redirect("signuppage")

        try:
            # Create user with properly hashed password
            UserAlexa.objects.create(
                username=username,
                password=make_password(password)
            )
            return redirect("loginpage")
        except Exception as e:
            messages.warning(request, """An error occurred during signup. 
                            Please try again.""")
            return redirect("signuppage")
    
    return redirect("signuppage")
        

