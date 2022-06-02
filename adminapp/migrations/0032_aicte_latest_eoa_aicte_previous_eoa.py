# Generated by Django 4.0.1 on 2022-06-01 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0031_informn_corner'),
    ]

    operations = [
        migrations.CreateModel(
            name='AICTE_latest_EOA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('pdf', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='AICTE_previous_EOA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('pdf', models.FileField(upload_to='')),
            ],
        ),
    ]