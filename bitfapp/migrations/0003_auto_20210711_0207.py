# Generated by Django 3.2.1 on 2021-07-11 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitfapp', '0002_member_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='balance',
            field=models.CharField(blank=True, default=0.0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='bonus',
            field=models.CharField(blank=True, default=0.0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='profit',
            field=models.CharField(blank=True, default=0.0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='ref',
            field=models.CharField(blank=True, default=0.0, max_length=200, null=True),
        ),
    ]
