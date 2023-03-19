# Generated by Django 3.2.1 on 2021-07-11 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitfapp', '0005_member_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='status',
            field=models.CharField(blank=True, default='Pending', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='manage',
            name='site',
            field=models.CharField(default='site', max_length=200, primary_key=True, serialize=False),
        ),
    ]