from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def sign_up(request):
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('home')
    return render(request, 'registration/sign_up.html', context={'forms': form})
