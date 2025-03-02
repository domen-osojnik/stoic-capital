from django.db import models

from django.db import models

class TradeInstrument(models.Model):
    FUTURES = 'futures'
    STOCK = 'stock'
    CFD = 'cfd'
    CURRENCY = 'currency'
    CRYPTO = 'crypto'

    INSTRUMENT_TYPES = [
        (FUTURES, 'Futures'),
        (STOCK, 'Stock'),
        (CFD, 'CFD'),
        (CURRENCY, 'Currency'),
        (CRYPTO, 'Crypto'),
    ]

    symbol = models.CharField(max_length=10, unique=True)  # Example: "ES"
    name = models.CharField(max_length=50)  # Example: "E-mini S&P 500"
    type = models.CharField(max_length=10, choices=INSTRUMENT_TYPES, default=FUTURES)  # ✅ New field
    tick_size = models.DecimalField(max_digits=10, decimal_places=6)  # Example: 0.25
    tick_value = models.DecimalField(max_digits=10, decimal_places=2)  # Example: 12.50
    contract_size = models.IntegerField()  # Example: 50 (per contract)
    currency = models.CharField(max_length=10, default="USD")  # Example: "USD"
    exchange = models.CharField(max_length=50, blank=True, null=True)  # CME, NYSE, etc.

    def __str__(self):
        return f"{self.symbol} ({self.name} - {self.get_type_display()})"
