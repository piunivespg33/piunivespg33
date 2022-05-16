from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import logout

def home(request):
    return render(request, 'index.html')

def users(request):
    return render(request, 'users.html')

def cadastrarUsuario(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html")
        else:
            form = RegistrationForm()
            context = {
                'form': form,
            }
            return render(request, "cadastrarUsuario.html", context)
    else:
        form = RegistrationForm()
        context = {
            'form': form,
        }
        return render(request, "cadastrarUsuario.html", context)

def user_logout(request):
    logout(request)
    return redirect('/piunivespg33/')