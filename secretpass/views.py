from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Account
from .serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
