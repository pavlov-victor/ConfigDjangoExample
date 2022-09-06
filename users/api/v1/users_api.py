from rest_framework.response import Response
from rest_framework.views import APIView


class SelfUserAPIView(APIView):
    """Работа над своим аккаунтом."""

    def get(self, request, *args, **kwargs):
        return Response({"user": str(self.request.user)})
