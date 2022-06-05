from django.contrib.auth.models import User


class UserServices:
    @classmethod
    def create_user(cls, username: str, email: str, password: str):
        new_user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        new_user.save()

        return {
            "username": username,
            "email": email
        }
