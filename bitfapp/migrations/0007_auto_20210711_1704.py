# Generated by Django 3.2.1 on 2021-07-12 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitfapp', '0006_auto_20210711_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='manage',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='manage',
            name='admin_pin',
            field=models.CharField(blank=True, default='1234', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='status',
            field=models.CharField(blank=True, default='Pending..', max_length=200, null=True),
        ),
    ]