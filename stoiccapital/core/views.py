from django.shortcuts import render
from .serializers import TradingAccountSerializer
from .models import TradingAccount
from rest_framework import permissions, generics

# Create your views here.
class TradingAccountListCreateView(generics.ListCreateAPIView):
    serializer_class = TradingAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return accounts that belong to the authenticated user
        return TradingAccount.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Ensure the account is linked to the logged-in user
        serializer.save(user=self.request.user)