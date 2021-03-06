# Generated by Django 4.0.5 on 2022-06-08 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_actormovie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='movie_title',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='actor_first_name',
        ),
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(related_name='movies', through='movies.ActorMovie', to='movies.actor'),
        ),
    ]
