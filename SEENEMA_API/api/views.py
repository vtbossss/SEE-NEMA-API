from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from .models import Watchlist
from .serializers import WatchlistSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .services import fetch_movie_data
from django.shortcuts import render

# User Registration View


def landingview(request):
    return render(request,'landingpage.html')


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save the user
            # Generate JWT token for the user
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "User created successfully",
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Add a movie to the watchlist
class AddToWatchlistView(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication
    serializer_class = WatchlistSerializer

    def post(self, request, *args, **kwargs):
        movie_title = request.data.get('title')
        if not movie_title:
            return Response({"error": "Movie title is required"}, status=400)

        # Fetch movie details from TMDb (or your data source)
        movies = fetch_movie_data(movie_title)
        if not movies:
            return Response({"error": "Movie not found"}, status=404)

        # Add the first result to the watchlist for the authenticated user
        movie_data = movies[0]
        watchlist_item, created = Watchlist.objects.get_or_create(
            user=request.user,  # Associate with the logged-in user
            movie_id=movie_data['id'],
            defaults={
                'title': movie_data['title'],
                'description': movie_data['overview'],
                'release_date': movie_data['release_date']
            }
        )
        if created:
            return Response({"message": "Movie added to watchlist"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Movie is already in your watchlist"}, status=status.HTTP_200_OK)


# List all movies in the user's watchlist
class WatchlistView(generics.ListAPIView):
    serializer_class = WatchlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "message": "Movies in your watchlist retrieved successfully",
            "count": queryset.count(),
            "data": serializer.data
        })


# Update a movie in the watchlist
class WatchlistUpdateView(generics.UpdateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            "message": "Movie in your watchlist updated successfully",
            "data": response.data
        })


# Delete a movie from the watchlist
class WatchlistDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WatchlistSerializer

    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the movie to delete
        self.perform_destroy(instance)
        return Response({
            "message": "Movie removed from your watchlist successfully",
            "movie_title": instance.title
        }, status=200)
