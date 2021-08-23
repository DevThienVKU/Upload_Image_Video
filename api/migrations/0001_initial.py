# Generated by Django 3.2.6 on 2021-08-22 13:04

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('cover', models.ImageField(blank=True, null=True, upload_to=api.models.upload_path)),
            ],
        ),
    ]