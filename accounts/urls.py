from django.urls import path
from .views import UserRegistrationView, TradingAccountListCreateView, TradingAccountDetailView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('trading-accounts/', TradingAccountListCreateView.as_view(), name='trading_accounts'),
    path('trading-accounts/<int:pk>/', TradingAccountDetailView.as_view(), name='trading_account_detail'),  # ✅ New endpoint for single account
]
