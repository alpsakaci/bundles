from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Account
from .serializers import UserSerializer, AccountSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # override post
        serializer.save(owner=self.request.user)
