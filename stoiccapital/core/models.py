from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Instrument(models.Model):
    # Type of instrument (e.g., Stock, Forex, Cryptocurrency)
    TYPE_CHOICES = [
        ('STOCK', 'Stock'),
        ('FOREX', 'Forex'),
        ('CRYPTO', 'Cryptocurrency'),
        ('COMMODITY', 'Commodity'),
        ('INDEX_CFD', 'Index CFD'),
        ('FUTURES', 'Futures'),
    ]
    
    name = models.CharField(max_length=100)  # Name of the instrument (e.g., Apple)
    symbol = models.CharField(max_length=20, unique=True)  # Symbol (e.g., AAPL for Apple stock)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)  # Type of instrument
    tick_value = models.DecimalField(max_digits=10, decimal_places=4)  # The value of a single "tick"

    def __str__(self):
        return f'{self.name} ({self.symbol}) - {self.type}'


class Strategy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Description of the strategy

    def __str__(self):
        return self.name

class TradingAccount(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to a specific user
    account_name = models.CharField(max_length=255)  # Name of the trading account
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)  # Current balance of the account
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the account was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp of the last update

    def __str__(self):
        return f"{self.account_name} - {self.balance} {self.currency}"

class Trade(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    entry_price = models.DecimalField(max_digits=10, decimal_places=2)  # Price when the trade was opened
    exit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Price when the trade was closed
    stop_loss = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Stop loss price
    buy_or_sell = models.CharField(max_length=4, choices=[('BUY', 'Buy'), ('SELL', 'Sell')])
    total_value = models.DecimalField(max_digits=12, decimal_places=2)
    trading_account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.instrument.symbol} {self.buy_or_sell} - {self.quantity} at {self.entry_price} for {self.trading_account.account_name}'

    def save(self, *args, **kwargs):
        self.total_value = self.quantity * self.entry_price
        super().save(*args, **kwargs)

    def calculate_pnl(self):
        if self.exit_price is not None:
            price_change = self.exit_price - self.entry_price
            tick_movement = price_change / self.instrument.tick_value
            pnl = tick_movement * self.quantity
            return pnl
        else:
            return 0

    def calculate_projected_loss(self):
        if self.stop_loss is not None:
            # Calculate the price change between the stop loss and entry price
            price_change = self.entry_price - self.stop_loss if self.buy_or_sell == 'BUY' else self.stop_loss - self.entry_price
            tick_movement = price_change / self.instrument.tick_value
            projected_loss_value = tick_movement * self.quantity

            # Calculate the percentage loss from the entry price
            projected_loss_percentage = (price_change / self.entry_price) * 100

            return projected_loss_value, projected_loss_percentage
        else:
            return 0, 0  # No stop loss set


