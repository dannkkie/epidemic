import pytest

from movies.models import Movie


@pytest.mark.django_db
def test_movie_model():
    movie = Movie(
        id="tt3896198",
        title="Raising Arizona",
        year="1987",
        type="movie",
        poster="https://example.com/poster.jpg",
    )
    movie.save()
    assert movie.id == "tt3896198"
    assert movie.title == "Raising Arizona"
    assert movie.year == "1987"
    assert movie.type == "movie"
    assert movie.poster == "https://example.com/poster.jpg"
    assert str(movie) == movie.title
