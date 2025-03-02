from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import TradingAccount
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, TradingAccountSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [(permissions.AllowAny)]

class TradingAccountListCreateView(generics.ListCreateAPIView):
    serializer_class = TradingAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TradingAccount.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        if serializer.validated_data.get("is_default", False):
            TradingAccount.objects.filter(user=user, is_default=True).update(is_default=False)
        serializer.save(user=user)

# ✅ Updated class to support PATCH
class TradingAccountDetailView(generics.RetrieveUpdateDestroyAPIView):  # ✅ Supports PATCH now
    serializer_class = TradingAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TradingAccount.objects.filter(user=self.request.user)

    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])