import random

from django.db import models


def generate_id():
    return "tt" + str(random.randint(9000000, 9999999))


class Movie(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=generate_id)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    type = models.CharField(max_length=20)
    poster = models.URLField()

    def __str__(self):
        return f"{self.title}"
