# Generated by Django 4.0.5 on 2022-06-07 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='owner',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]