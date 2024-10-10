from django.db import models

class Watchlist(models.Model):
    movie_id = models.IntegerField()  # TMDb movie ID
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # Remove user reference
