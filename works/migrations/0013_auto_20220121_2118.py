# Generated by Django 3.0.1 on 2022-01-21 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0012_available'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Available',
            new_name='Is_sold',
        ),
    ]