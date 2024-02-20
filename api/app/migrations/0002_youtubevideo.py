# Generated by Django 4.2 on 2024-02-15 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=255, unique=True)),
                ('thumbnail_url', models.URLField(max_length=500)),
                ('fetched_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]