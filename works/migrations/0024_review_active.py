# Generated by Django 3.0.1 on 2022-02-24 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0023_auto_20220224_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
