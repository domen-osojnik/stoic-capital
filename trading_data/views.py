from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import TradeInstrument
from .serializers import TradeInstrumentSerializer

class TradeInstrumentListCreateView(generics.ListCreateAPIView):
    queryset = TradeInstrument.objects.all()
    serializer_class = TradeInstrumentSerializer
    permission_classes = [permissions.IsAuthenticated]

class TradeInstrumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TradeInstrument.objects.all()
    serializer_class = TradeInstrumentSerializer
    permission_classes = [permissions.IsAuthenticated]
