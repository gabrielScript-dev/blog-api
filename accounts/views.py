from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
