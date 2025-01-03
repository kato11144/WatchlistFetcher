from modules.logger_manager import LoggerManager
from modules.tmdb_client import TMDbClient
from modules.dump_manager import DumpManager

logger_manager = LoggerManager()
tmdb_client = TMDbClient()
dump_manager = DumpManager()

def main():
    try:
        logger = logger_manager.setup_logger()
        logger.info('Starting main function')

        tmdb_client.authenticate_user()
        logger.info('User authenticated successfully')

        movie_watchlist = tmdb_client.get_movie_watchlist()
        tv_watchlist = tmdb_client.get_tv_watchlist()
        dump_manager.save_watchlists(movie_watchlist, tv_watchlist)
        logger.info('Watchlists have been saved successfully')

    except Exception as e:
        logger.error(f'An error occurred: {e}', exc_info=True)

if __name__ == '__main__':
    main()
