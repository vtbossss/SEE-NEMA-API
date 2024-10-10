import requests
from django.conf import settings

def fetch_movie_data(title):
    api_url = f"https://api.themoviedb.org/3/search/movie?api_key={settings.TMDB_API_KEY}&query={title}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get('results', [])
    return None
