from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts.models import User
from .serializers import UserSerializer, UserCreateSerializer, UserActivateSerializer

class UserViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


    @action(detail=True, methods=['post'], serializer_class=UserActivateSerializer)
    def activate(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"details", "activated your account successfully"},status=status.HTTP_200_OK)
        
