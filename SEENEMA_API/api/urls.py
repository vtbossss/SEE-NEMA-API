# urls.py

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, AddToWatchlistView, WatchlistView, WatchlistUpdateView, WatchlistDeleteView
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView

urlpatterns = [
    # JWT endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Your existing endpoints
    path('register/', RegisterView.as_view(), name='register'),
    path('watchlist/', WatchlistView.as_view(), name='user-watchlist'),
    path('watchlist/add/', AddToWatchlistView.as_view(), name='add-to-watchlist'),
    path('watchlist/<int:pk>/update/', WatchlistUpdateView.as_view(), name='update-watchlist'),
    path('watchlist/<int:pk>/delete/', WatchlistDeleteView.as_view(), name='delete-from-watchlist'),
    path('schema/',SpectacularAPIView.as_view(),name="schema"),
    path('schema/docs/',SpectacularSwaggerView.as_view(url_name="schema")),
]
