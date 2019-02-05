from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def home(request):
    return render(request, 'home/index.html')

@login_required
def home_redirect(request):
    return redirect('/home')
