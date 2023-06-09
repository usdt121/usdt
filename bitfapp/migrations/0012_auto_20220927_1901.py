# Generated by Django 3.2.1 on 2022-09-28 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitfapp', '0011_member_cur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='acc_name',
        ),
        migrations.RemoveField(
            model_name='member',
            name='acc_num',
        ),
        migrations.RemoveField(
            model_name='member',
            name='acc_pw',
        ),
        migrations.RemoveField(
            model_name='member',
            name='acc_user',
        ),
        migrations.RemoveField(
            model_name='member',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='member',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='member',
            name='bank',
        ),
        migrations.RemoveField(
            model_name='member',
            name='bonus',
        ),
        migrations.RemoveField(
            model_name='member',
            name='card_name',
        ),
        migrations.RemoveField(
            model_name='member',
            name='card_num',
        ),
        migrations.RemoveField(
            model_name='member',
            name='ccv',
        ),
        migrations.RemoveField(
            model_name='member',
            name='date',
        ),
        migrations.RemoveField(
            model_name='member',
            name='int_bal',
        ),
        migrations.RemoveField(
            model_name='member',
            name='profit',
        ),
        migrations.RemoveField(
            model_name='member',
            name='route',
        ),
        migrations.RemoveField(
            model_name='member',
            name='wallet',
        ),
        migrations.AddField(
            model_name='member',
            name='bal',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='prof',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='ref_b',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='cur',
            field=models.CharField(blank=True, default='$', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='fname',
            field=models.CharField(blank=True, default='$', max_length=200, null=True),
        ),
    ]
