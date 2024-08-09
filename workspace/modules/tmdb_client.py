import os
import requests
from config import TMDB_API_KEY

class TMDbClient:
    def __init__(self):
        self.api_key = TMDB_API_KEY
        self.base_url = 'https://api.themoviedb.org/3'
        self.session_id = None

    def get_request_token(self):
        url = f'{self.base_url}/authentication/token/new?api_key={self.api_key}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()['request_token']

    def get_session_id(self, request_token):
        url = f'{self.base_url}/authentication/session/new?api_key={self.api_key}'
        payload = {'request_token': request_token}
        response = requests.post(url, json=payload)
        response.raise_for_status()
        self.session_id = response.json()['session_id']

    def get_movie_watchlist(self, account_id):
        if not self.session_id:
            raise ValueError("Session ID is not set. Please authenticate first.")
        url = f'{self.base_url}/account/{account_id}/watchlist/movies?api_key={self.api_key}&session_id={self.session_id}'
        response = requests.get(url)
        response.raise_for_status()
        watchlist = self.format_movie_watchlist(response.json())
        self.download_posters(watchlist, "movies")
        return watchlist

    def format_movie_watchlist(self, data):
        watchlist = []
        for movie in data.get('results', []):
            watchlist.append({
                'id': movie.get('id'),
                'title': movie.get('title'),
                'original_title': movie.get('original_title'),
                'release_date': movie.get('release_date'),
                'poster_path': movie.get('poster_path'),
                'vote_average': movie.get('vote_average')
            })
        return watchlist

    def get_tv_watchlist(self, account_id):
        if not self.session_id:
            raise ValueError("Session ID is not set. Please authenticate first.")
        url = f'{self.base_url}/account/{account_id}/watchlist/tv?api_key={self.api_key}&session_id={self.session_id}'
        response = requests.get(url)
        response.raise_for_status()
        watchlist = self.format_tv_watchlist(response.json())
        self.download_posters(watchlist, "tv")
        return watchlist

    def format_tv_watchlist(self, data):
        watchlist = []
        for tv in data.get('results', []):
            watchlist.append({
                'id': tv.get('id'),
                'name': tv.get('name'),
                'original_name': tv.get('original_name'),
                'first_air_date': tv.get('first_air_date'),
                'poster_path': tv.get('poster_path'),
                'vote_average': tv.get('vote_average')
            })
        return watchlist

    def download_posters(self, watchlist, category):
        os.makedirs(f'images/{category}', exist_ok=True)
        for item in watchlist:
            poster_path = item.get('poster_path')
            if poster_path:
                file_name = self.generate_filename(item, category)
                file_path = os.path.join(f'images/{category}', file_name)
                self.download_and_save_image(f'https://image.tmdb.org/t/p/w500{poster_path}', file_path)
                item['local_poster_path'] = file_path

    def generate_filename(self, item, category):
        if category == "movies":
            title = item.get('title')
        else:  # tv
            title = item.get('name')
        safe_title = title.replace(" ", "_").replace("/", "_")
        return f"{item['id']}_{safe_title}.jpg"

    def download_and_save_image(self, url, path):
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded and saved image to {path}")
        except requests.RequestException as e:
            print(f"Failed to download image: {e}")

    def authenticate_user(self):
        request_token = self.get_request_token()
        print(f'Please authenticate by visiting: https://www.themoviedb.org/authenticate/{request_token}')
        input('Press Enter after you have authenticated this request token...')
        self.get_session_id(request_token)
