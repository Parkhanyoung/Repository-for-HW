# Generated by Django 3.2.2 on 2021-05-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_auto_20210509_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
