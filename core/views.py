from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect

from .forms import SignUpForm

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})


def logout(request):
    auth_logout(request)
    # Optionally, add any custom behavior here before redirecting
    return redirect('frontpage')  # Redirect to the frontpage or any other desired page
