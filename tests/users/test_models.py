import pytest

from users.models import User


@pytest.mark.django_db
class TestUserModel:
    def test_model_create(self):
        User.objects.create(username="test_user_model_create")
        assert User.objects.filter(username="test_user_model_create").exists()
