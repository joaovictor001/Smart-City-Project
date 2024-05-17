from django .contrib.auth.models import User
from rest_framework import generics, permissions
from app_smart.api import serializers


class CreateUserApiViewSet(generics.CreateAPIView):
  

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    #permissions_classes = [permission.IsAdminUser]


    def post(self,request,*args, **kwargs):
        return self.create(request,*args,**kwargs)