# Generated by Django 3.0.1 on 2022-01-23 02:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0021_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=3, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'verbose_name_plural': 'Rating',
            },
        ),
        migrations.RemoveField(
            model_name='review',
            name='content',
        ),
        migrations.RemoveField(
            model_name='review',
            name='description',
        ),
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
        migrations.RemoveField(
            model_name='review',
            name='is_sold',
        ),
        migrations.RemoveField(
            model_name='review',
            name='name',
        ),
        migrations.RemoveField(
            model_name='review',
            name='price',
        ),
    ]
