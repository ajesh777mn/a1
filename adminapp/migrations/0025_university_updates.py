# Generated by Django 4.0.1 on 2022-05-16 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0024_media_updates'),
    ]

    operations = [
        migrations.CreateModel(
            name='university_updates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('pdf', models.FileField(upload_to='')),
            ],
        ),
    ]
