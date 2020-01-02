# Generated by Django 3.0.1 on 2019-12-21 15:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20191220_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointments',
            old_name='date',
            new_name='app_date',
        ),
        migrations.RenameField(
            model_name='pills',
            old_name='days',
            new_name='pil_days',
        ),
        migrations.AddField(
            model_name='days',
            name='name',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='days',
            name='monday',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), size=4), size=4),
        ),
    ]
