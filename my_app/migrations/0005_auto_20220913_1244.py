# Generated by Django 2.2.2 on 2022-09-13 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20220913_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 9, 13, 12, 44, 1, 173304)),
        ),
    ]
