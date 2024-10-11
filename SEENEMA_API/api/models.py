from django.db import models
from django.contrib.auth.models import User  # Import the default User model

class Watchlist(models.Model):
    # Associate each movie in the watchlist with a specific user
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # If user is deleted, delete their watchlist items as well

    # Movie information
    movie_id = models.IntegerField()  # TMDb or other third-party movie ID
    title = models.CharField(max_length=200)  # Movie title
    description = models.TextField(null=True, blank=True)  # Optional description of the movie
    release_date = models.DateField(null=True, blank=True)  # Optional release date of the movie
    added_on = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the movie is added to the watchlist

    def __str__(self):
        return f"{self.title} - {self.user.username}"  # Display the movie title and the associated user

    class Meta:
        ordering = ['-added_on']  # Order watchlist items by when they were added, newest first
