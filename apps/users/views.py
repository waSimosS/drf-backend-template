
from rest_framework import generics

from .models import User
from .serializers import UserSerializer, UserListSerializer

from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin




class CreateUserView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdmin, )
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdmin, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get_serializer_class(self):
        print (self.request.user.is_admin)
        if self.request.user.is_admin : 
            return UserSerializer
        return super().get_serializer_class()