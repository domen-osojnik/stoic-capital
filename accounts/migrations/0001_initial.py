# Generated by Django 4.2.19 on 2025-03-02 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TradingAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("account_name", models.CharField(max_length=100)),
                ("account_size", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "max_total_drawdown",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
                (
                    "max_daily_drawdown",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
                ("pnl", models.DecimalField(decimal_places=2, max_digits=6)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trading_accounts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
