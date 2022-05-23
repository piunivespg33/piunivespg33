from django.contrib.auth.models import User


class UserServices:
    @classmethod
    def create_user(cls, username: str, first_name: str, last_name: str, password: str):
        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        new_user.save()

        return {
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
        }
