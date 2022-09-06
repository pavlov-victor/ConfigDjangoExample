import pytest

from users.models import User
from users.services import create_user_service


@pytest.mark.django_db
class TestUserServices:
    def test_create_user_service(self):
        username = "test_create_user_service"
        create_user_service(username=username, password="123")
        assert (user := User.objects.filter(username=username).first())
        assert user.check_password("123")
