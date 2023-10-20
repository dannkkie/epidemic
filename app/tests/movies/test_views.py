import pytest
from django.contrib.auth.models import User

from movies.models import Movie


@pytest.mark.django_db
def test_add_movie(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        "/api/v1/movies/",
        {
            "title": "The Big Lebowski",
            "year": "2023",
            "type": "movie",
            "poster": "https://example.com/poster.jpg",
        },
        content_type="application/json",
    )
    assert resp.status_code == 201
    assert resp.data["title"] == "The Big Lebowski"

    movies = Movie.objects.all()
    assert len(movies) == 1


@pytest.mark.django_db
def test_add_movie_invalid_json(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post("/api/v1/movies/", {}, content_type="application/json")
    assert resp.status_code == 400

    movies = Movie.objects.all()
    assert len(movies) == 0


@pytest.mark.django_db
def test_add_movie_invalid_json_keys(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        "/api/v1/movies/",
        {
            "title": "The Big Lebowski",
            "type": "movie",
            "poster": "https://example.com/poster.jpg",
        },
        content_type="application/json",
    )
    assert resp.status_code == 400

    movies = Movie.objects.all()
    assert len(movies) == 0


@pytest.mark.django_db
def test_get_single_movie(client):
    movie = Movie.objects.create(
        title="The Big Lebowski",
        year="2023",
        type="movie",
        poster="https://example.com/poster.jpg",
    )
    resp = client.get(f"/api/v1/movies/{movie.id}/")
    assert resp.status_code == 200
    assert resp.data["title"] == "The Big Lebowski"


@pytest.mark.django_db
def test_get_single_movie_incorrect_id(client):
    resp = client.get(f"/api/v1/movies/foo/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_single_movie_by_title(client):
    movie = Movie.objects.create(
        title="The Big Lebowski",
        year="2023",
        type="movie",
        poster="https://example.com/poster.jpg",
    )
    resp = client.get(f"/api/v1/movies/title/{movie.title}/")
    assert resp.status_code == 200
    assert resp.data["title"] == "The Big Lebowski"


@pytest.mark.django_db
def test_get_single_movie_incorrect_title(client):
    resp = client.get(f"/api/v1/movies/title/non-existent-title/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_movies(client, add_movie):
    movie_one = add_movie(
        title="The Big Lebowski",
        year="2023",
        type="movie",
        poster="https://example.com/poster1.jpg",
    )
    resp = client.get(f"/api/v1/movies/")
    assert resp.status_code == 200
    assert resp.data[0]["title"] == movie_one.title


@pytest.mark.django_db
def test_remove_movie(client, add_movie):
    # Log in as a user first
    client.login(username="username", password="password")

    movie = add_movie(
        title="The Big Lebowski",
        year="2023",
        type="movie",
        poster="https://example.com/poster1.jpg",
    )

    resp = client.get(f"/api/v1/movies/{movie.id}/")
    assert resp.status_code == 200
    assert resp.data["title"] == "The Big Lebowski"

    resp_two = client.delete(f"/api/v1/movies/{movie.id}/")
    assert resp_two.status_code == 204

    resp_three = client.get("/api/v1/movies/")
    assert resp_three.status_code == 200
    assert len(resp_three.data) == 0


@pytest.mark.django_db
def test_remove_movie_incorrect_id(client):
     # Create a user
    user = User.objects.create_user(username='testuser', password='12345')

     # Log the user in
    client.login(username='testuser', password='12345')

    resp = client.delete(f"/api/v1/movies/99/")
    assert resp.status_code == 404
