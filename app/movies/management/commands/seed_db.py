import requests
from django.core.management.base import BaseCommand

from movies.models import Movie


class Command(BaseCommand):
    help = "Populates the database with movie data from the OMDB API"

    def handle(self, *args, **options):
        if not Movie.objects.exists():
            # api_key = os.getenv('API_KEY')
            api_key = "2a8012e1"
            if api_key is None:
                print("Set the API_KEY environment variable")
                return

            movies = []
            for i in range(1, 11):
                url = f"http://www.omdbapi.com/?s=movie&page={i}&apikey={api_key}"
                response = requests.get(url)
                data = response.json()

                if "Search" in data:
                    for item in data["Search"]:
                        movie = Movie(
                            id=item["imdbID"],
                            title=item["Title"],
                            year=item["Year"],
                            type=item["Type"],
                            poster=item["Poster"],
                        )
                        movies.append(movie)

            if movies:
                Movie.objects.bulk_create(movies)
