# Generated by Django 3.2.2 on 2021-05-16 15:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_auto_20210516_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='written_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
