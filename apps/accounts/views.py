from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages

def home(request):
    return redirect("dashboard") if request.user.is_authenticated else redirect("login")

def login_view(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Invalid username or password.")
    return render(request, "accounts/login.html")

@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")

def logout_view(request):
    logout(request)
    return redirect("login")
