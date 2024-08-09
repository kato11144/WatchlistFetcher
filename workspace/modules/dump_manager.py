import json
import os

class DumpManager:
    def __init__(self, file_name):
        self.dir_name = 'data'
        os.makedirs(self.dir_name, exist_ok=True)
        self.file_path = os.path.join(self.dir_name, file_name)

    def save_watchlists(self, movie_watchlist, tv_watchlist):
        data = {
            'movies': movie_watchlist,
            'tv_shows': tv_watchlist
        }

        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f'Watchlists saved to {self.file_path}')

    @staticmethod
    def get_example_format():
        """
        Returns an example of the data format used for dumping watchlists.
        The example format uses generic types instead of specific values.
        """
        return {
            'movies': [
                {
                    'id': 123,  # int
                    'title': 'string',  # str
                    'original_title': 'string',  # str
                    'release_date': 'YYYY-MM-DD',  # str (ISO 8601 format)
                    'poster_path': '/path/to/poster.jpg',  # str
                    'vote_average': 0.0,  # float
                    'local_poster_path': 'path/to/local_poster.jpg'  # str
                },
                {
                    'id': 456,  # int
                    'title': 'string',  # str
                    'original_title': 'string',  # str
                    'release_date': 'YYYY-MM-DD',  # str (ISO 8601 format)
                    'poster_path': '/path/to/poster.jpg',  # str
                    'vote_average': 0.0,  # float
                    'local_poster_path': 'path/to/local_poster.jpg'  # str
                }
            ],
            'tv_shows': [
                {
                    'id': 789,  # int
                    'name': 'string',  # str
                    'original_name': 'string',  # str
                    'first_air_date': 'YYYY-MM-DD',  # str (ISO 8601 format)
                    'poster_path': '/path/to/poster.jpg',  # str
                    'vote_average': 0.0,  # float
                    'local_poster_path': 'path/to/local_poster.jpg'  # str
                }
            ]
        }

if __name__ == "__main__":
    dump_manager = DumpManager('watchlists.json')

    example_format = dump_manager.get_example_format()
    print("Example format for dumped data:")
    print(json.dumps(example_format, indent=4, ensure_ascii=False))

    movie_watchlist = example_format['movies']
    tv_watchlist = example_format['tv_shows']

    dump_manager.save_watchlists(movie_watchlist, tv_watchlist)
