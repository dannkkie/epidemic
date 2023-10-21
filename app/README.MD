
# Epidemic Test

A Movie collection Database

## Requirements

### 1. Fetch test data via https from OMDB API

- You should fetch 100 movies from OMDB API. It's up to you what kind of movies you will get.
- Movies should be saved in the database.
- This method should be ran only once if database is empty.

### 2. Implement an api

- The api should have a method that returns a list of movies from the database
- There should be option to set how many records are returned in single API response (by default 10)
- There should be pagination implemented in the backend
- Data should be ordered by Title
- The api should have a method that returns a single movie from the database
- There should be option to get the movie by title
- The api should have a method to add a movie to the database
- Title should be provided in request
- All movie details should be fetched from OMDB API and saved in the database
- The api should have a method to remove a movie from the database
- There should be option to remove movie with it's id
- This method should be protected so only authorized user can perform this action (There is test user in the database)

### 3. Unit tests for all cases


## Solution

### Run locally

clone the Project
```
git clone git@github.com:dannkkie/epidemic.git

```

cd into project root dir
```
cd epidemic

```

Build Image
```
docker-compose build

```

Run containers
```
docker-compose up -d

```

Create migrations
```
docker-compose exec movies python manage.py makemigrations

```

Appy migrations
```
docker-compose exec movies python manage.py migrate

```

Seed database
```
docker-compose exec movies python manage.py seed_db

```

Create a test user
```
docker-compose exec movies python manage.py createsuperuser

```

Run tests
```
docker-compose exec movies pytest -p no:warnings

```

Lint
```
docker-compose exec movies flake8 .

```

Run black and isort with check options
```
docker-compose exec movies black --exclude=migrations --check .
docker-compose exec movies isort . --check-only

```

Make code changes with Black and isort
```
docker-compose exec movies black --exclude=migrations .
docker-compose exec movies isort .

```

## Usage

Run below command to create a super user


- GET all movies (http://127.0.0.1:8009/api/v1/movies/)
- GET all movies with optional arguments page and limit (http://localhost:8009/api/v1/movies?limit=10&page=3)
- GET single movie with id (http://127.0.0.1:8009/api/v1/movies/{id})
- GET single movie with title (http://127.0.0.1:8009/api/v1/movies/title/{title})
- POST add a movie to the database body of the request should be json (http://127.0.0.1:8009/api/v1/movies/)
    ```
    {
        "title": "some_title",
        "year": "some year",
        "type": "movie",
        "poster" "https://some_url.com"
    }

    ```
- DELETE a movie with id ((http://127.0.0.1:8009/api/v1/movies/{id})). You need authorization to delete a movie, use the user ealier created to login using 
((http://127.0.0.1:8009/admin))
