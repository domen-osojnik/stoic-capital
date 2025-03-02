# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class TradingAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trading_accounts')
    account_name = models.CharField(max_length=100)
    account_size = models.DecimalField(max_digits=12, decimal_places=2)
    max_total_drawdown = models.DecimalField(max_digits=6, decimal_places=2)
    max_daily_drawdown = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_default = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.account_name} ({self.user.username})"
