# Generated by Django 3.2.1 on 2022-04-19 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitfapp', '0010_manage_coupon_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='cur',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
