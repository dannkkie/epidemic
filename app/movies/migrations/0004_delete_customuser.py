# Generated by Django 4.2.6 on 2023-10-20 22:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0003_alter_movie_id"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]