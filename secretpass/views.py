from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from django.shortcuts import get_object_or_404
from .models import Account
from .crypto import encrypt_password, decrypt_password
from .serializers import UserSerializer, AccountSerializer
import string
import random


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, *args, **kwargs):
        super().update(request)
        user = User.objects.get(id=pk)
        user.set_password(request.data["password"])
        user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = Account.objects.filter(owner=request.user)
        serializer = AccountSerializer(
            queryset, many=True, context={"request": request}
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Account.objects.filter(owner=request.user)
        account = get_object_or_404(queryset, pk=pk)
        serializer = AccountSerializer(account, context={"request": request})

        return Response(serializer.data)

    def perform_create(self, serializer):
        password = serializer.validated_data["password"]
        serializer.validated_data["password"] = encrypt_password(password)
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["POST"])
    def decrypt_password(self, request, pk=None):
        user = request.user
        account = self.get_object()
        if account.owner == user:
            load = {"plain_password": decrypt_password(account.password)}
        else:
            raise PermissionDenied

        return Response(load)


@api_view(["POST"])
def generate_password(request):
    characters = string.ascii_letters + string.digits
    password = ""
    for i in range(20):
        if (i + 1) % 7 == 0:
            password = password + "".join("-")
        else:
            password = password + "".join(random.choice(characters))
    return Response({"password": password})
