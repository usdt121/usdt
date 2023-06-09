# Generated by Django 3.2.1 on 2022-09-28 04:15

import cloudinary.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitfapp', '0013_auto_20220927_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='slip',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='slip'),
        ),
        migrations.AlterField(
            model_name='dhistory',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 27, 21, 15, 21, 977114), null=True),
        ),
        migrations.AlterField(
            model_name='whistory',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 27, 21, 15, 21, 977114), null=True),
        ),
    ]
