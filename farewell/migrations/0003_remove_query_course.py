# Generated by Django 2.0 on 2018-04-26 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farewell', '0002_auto_20180419_0834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='course',
        ),
    ]
