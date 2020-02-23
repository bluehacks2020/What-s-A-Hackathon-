# Generated by Django 3.0.3 on 2020-02-22 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IndigenousPeople', '0003_cultureinfo_webpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Product3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='Product1',
        ),
    ]