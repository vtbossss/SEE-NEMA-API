from django.urls import path
from .views import AddToWatchlistView, WatchlistView, WatchlistUpdateView, WatchlistDeleteView

urlpatterns = [
    path('watchlist/', WatchlistView.as_view(), name='user-watchlist'),
    path('watchlist/add/', AddToWatchlistView.as_view(), name='add-to-watchlist'),
    path('watchlist/<int:pk>/update/', WatchlistUpdateView.as_view(), name='update-watchlist'),
    path('watchlist/<int:pk>/delete/', WatchlistDeleteView.as_view(), name='delete-from-watchlist'),
]
