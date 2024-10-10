from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Watchlist
from .serializers import WatchlistSerializer
from .services import fetch_movie_data

# Add a movie to the watchlist
class AddToWatchlistView(APIView):
    def post(self, request, *args, **kwargs):
        movie_title = request.data.get('title')
        if not movie_title:
            return Response({"error": "Movie title is required"}, status=400)

        # Fetch movie details from TMDb
        movies = fetch_movie_data(movie_title)
        if not movies:
            return Response({"error": "Movie not found"}, status=404)

        # Add first result to the watchlist
        movie_data = movies[0]
        watchlist_item, created = Watchlist.objects.get_or_create(
            movie_id=movie_data['id'],
            defaults={
                'title': movie_data['title'],
                'description': movie_data['overview'],
                'release_date': movie_data['release_date']
            }
        )
        if created:
            return Response({"message": "Movie added to watchlist"}, status=201)
        else:
            return Response({"message": "Movie is already in your watchlist"}, status=200)

# List all movies in the watchlist
class WatchlistView(generics.ListAPIView):
    serializer_class = WatchlistSerializer

    def get_queryset(self):
        return Watchlist.objects.all()  # No user filter since we're not using authentication

# Update a movie in the watchlist
class WatchlistUpdateView(generics.UpdateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer

# Delete a movie from the watchlist
class WatchlistDeleteView(generics.DestroyAPIView):
    queryset = Watchlist.objects.all()
