# Generated by Django 2.0.4 on 2018-04-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0008_auto_20180417_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exercise_slug',
            field=models.SlugField(unique=True),
        ),
    ]