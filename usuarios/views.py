from django.db import IntegrityError
from rest_framework import status
from usuarios.serializer import UserRegisterSerializer
from usuarios.services import UserServices
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class UserApi(APIView):
    
    permission_classes = ()

    def post(self, request, format=None):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():

            if serializer.data["password"] == serializer.data["cpassword"]:
                try:

                    new_user = UserServices.create_user(
                        username=serializer.data["username"],
                        email=serializer.data["email"],
                        password=serializer.data["password"],
                    )
                    return Response(new_user, status=status.HTTP_201_CREATED)

                except IntegrityError as e:
                    print(e)
                    error = {
                        "username": [
                            f"O usuário '{serializer.data['username']}' já existe."
                        ]
                    }
                    return Response(error, status=status.HTTP_400_BAD_REQUEST)

                except Exception as e:
                    print(e)
                    return Response(
                        serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )
            else:
                error = {
                    "password": [
                        "O campo password e confirmar password são diferentes."
                    ]
                }
                return Response(error, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        if request.user.id is not None:
            return Response({"user": request.user.username}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        
        return Response(status=status.HTTP_205_RESET_CONTENT)