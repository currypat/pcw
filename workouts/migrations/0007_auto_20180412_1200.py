# Generated by Django 2.0.4 on 2018-04-12 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0006_auto_20180412_1150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='created',
            new_name='pub_date',
        ),
    ]