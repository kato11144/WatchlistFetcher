# WatchlistFetcher

Fetch the Watchlist using the [TMDB](https://www.themoviedb.org/) API

## Setup Environment Variables

**Copy `.env.example` to `.env`**
```sh
cp .env.example .env
```
**Edit the `.env` file**
```sh
vim .env
```

---

### Build and Start Container
```sh
docker compose up -d --build
```

### Access the Container
```sh
docker compose exec app /bin/bash
```

### Stop and Remove Container
```sh
docker compose down
```
