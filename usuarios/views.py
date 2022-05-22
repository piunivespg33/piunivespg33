from django.db import IntegrityError
from django.shortcuts import render, redirect
from rest_framework import status
from usuarios.serializer import UserRegisterSerializer
from usuarios.services import UserServices
from .forms import RegistrationForm
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


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

class UserApi(APIView):

    def post(self, request, format=None):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            
            if serializer.data["password"] == serializer.data["cpassword"]:
                try:

                    new_user = UserServices.create_user(
                        username=serializer.data["username"],
                        first_name=serializer.data["first_name"],
                        last_name=serializer.data["last_name"],
                        password=serializer.data["password"]
                    )
                    return Response(new_user, status=status.HTTP_201_CREATED)

                except IntegrityError as e: 
                    error =  {"username": [f"O usuário '{serializer.data['username']}' já existe."]}
                    return Response(error, status=status.HTTP_400_BAD_REQUEST)

                except Exception as e:
                    print(e)
                    return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                error =  {"password": ["O campo password e confirmar password são diferentes."]}
                return Response(error, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
