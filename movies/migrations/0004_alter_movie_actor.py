# Generated by Django 4.0.5 on 2022-06-08 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_remove_actor_movie_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(through='movies.ActorMovie', to='movies.actor'),
        ),
    ]
