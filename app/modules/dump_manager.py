import json
import os

class DumpManager:
    def __init__(self):
        self.dir_name = 'data'
        self.file_name = 'watchlists.json'
        self.file_path = os.path.join(self.dir_name, self.file_name)
        os.makedirs(self.dir_name, exist_ok=True)

    def save_watchlists(self, movie_watchlist, tv_watchlist):
        data = {
            'movie': movie_watchlist,
            'tv': tv_watchlist
        }

        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f'Watchlists saved to {self.file_path}')

    def get_example_format(self):
        """
        Returns an example of the data format used for dumping watchlists.
        The example format uses generic types instead of specific values.
        """
        return {
            'movie': [
                {
                    'id': 123,
                    'title': 'string',
                    'original_title': 'string',
                    'release_date': 'YYYY-MM-DD',
                    'poster_path': '/path/to/poster.jpg',
                    'vote_average': 0.0,
                    'local_poster_path': 'path/to/local_poster.jpg'
                },
                {
                    'id': 456,
                    'title': 'string',
                    'original_title': 'string',
                    'release_date': 'YYYY-MM-DD',
                    'poster_path': '/path/to/poster.jpg',
                    'vote_average': 0.0,
                    'local_poster_path': 'path/to/local_poster.jpg'
                }
            ],
            'tv': [
                {
                    'id': 789,
                    'name': 'string',
                    'original_name': 'string',
                    'first_air_date': 'YYYY-MM-DD',
                    'poster_path': '/path/to/poster.jpg',
                    'vote_average': 0.0,
                    'local_poster_path': 'path/to/local_poster.jpg'
                }
            ]
        }

if __name__ == "__main__":
    dump_manager = DumpManager()

    example_format = dump_manager.get_example_format()
    print("Example format for dumped data:")
    print(json.dumps(example_format, indent=4, ensure_ascii=False))

    movie_watchlist = example_format['movie']
    tv_watchlist = example_format['tv']

    dump_manager.save_watchlists(movie_watchlist, tv_watchlist)
