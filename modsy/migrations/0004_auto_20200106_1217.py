# Generated by Django 3.0.1 on 2020-01-06 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modsy', '0003_auto_20200106_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='goal',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
