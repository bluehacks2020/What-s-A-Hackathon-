# Generated by Django 3.0.3 on 2020-02-22 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IndigenousPeople', '0002_auto_20200222_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultureinfo',
            name='webpage',
            field=models.CharField(default='ips', max_length=30),
            preserve_default=False,
        ),
    ]
