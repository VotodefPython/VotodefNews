# Generated by Django 4.0.5 on 2022-08-01 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='views',
        ),
    ]
