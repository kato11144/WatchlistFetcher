from modules.tmdb_client import TMDbClient
from modules.dump_manager import DumpManager
from modules.logger_manager import LoggerManager
from config import TMDB_ACCOUNT_ID

def main():
    logger = LoggerManager.setup_logger()

    logger.info('Starting main function')

    tmdb_client = TMDbClient()

    try:
        tmdb_client.authenticate_user()

        logger.info('User authenticated successfully')

        movie_watchlist = tmdb_client.get_movie_watchlist(TMDB_ACCOUNT_ID)
        tv_watchlist = tmdb_client.get_tv_watchlist(TMDB_ACCOUNT_ID)

        dump_manager = DumpManager('watchlists.json')
        dump_manager.save_watchlists(movie_watchlist, tv_watchlist)

        logger.info('Watchlists have been saved successfully')

    except Exception as e:
        logger.error(f'An error occurred: {e}', exc_info=True)

if __name__ == '__main__':
    main()
