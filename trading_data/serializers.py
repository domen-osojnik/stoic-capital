from rest_framework import serializers
from .models import TradeInstrument

class TradeInstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeInstrument
        fields = '__all__'
