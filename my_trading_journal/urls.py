from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # Include the accounts endpoints here
    path('api/trading-data/', include('trading_data.urls')),  # ✅ Include new app

    # JWT authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login to get access & refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Get new access token using refresh token
]
