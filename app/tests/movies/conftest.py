import pytest

from movies.models import Movie


@pytest.fixture(scope="function")
def add_movie():
    def _add_movie(title, year, type, poster):
        movie = Movie.objects.create(title=title, year=year, type=type, poster=poster)
        return movie

    return _add_movie
