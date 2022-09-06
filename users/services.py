from users.models import User


def create_user_service(username, password):
    user = User.objects.create(username=username)
    user.set_password(password)
    user.save()
