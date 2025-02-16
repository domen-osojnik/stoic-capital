from django.contrib import admin

# Register your models here.
from .models import Tag, Instrument, Strategy, Trade, TradingAccount

# Register your models here.
admin.site.register(Tag)
admin.site.register(Instrument)
admin.site.register(Strategy)
admin.site.register(Trade)
admin.site.register(TradingAccount)