# Generated by Django 3.0.5 on 2020-07-17 13:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0040_auto_20200717_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 13, 8, 23, 139562, tzinfo=utc)),
        ),
    ]