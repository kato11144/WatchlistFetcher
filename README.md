# WatchlistFetcher
Fetch the Watchlist using the [TMDB](https://www.themoviedb.org/) API with Docker

## Setup Environment Variables

**Copy `.env.example` to `.env`**
```sh
cp .env.example .env
```
**Edit the .env file**
```sh
nano .env
```

## Build and Start Container
```sh
docker compose up -d --build
```

## Access the Container
```sh
docker compose exec app /bin/bash
```
