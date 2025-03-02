from django.urls import path
from .views import TradeInstrumentListCreateView, TradeInstrumentDetailView

urlpatterns = [
    path('trade-instruments/', TradeInstrumentListCreateView.as_view(), name='trade_instruments'),
    path('trade-instruments/<int:pk>/', TradeInstrumentDetailView.as_view(), name='trade_instrument_detail'),
]
