# Generated by Django 3.0.3 on 2020-02-22 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IndigenousPeople', '0004_auto_20200222_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultureinfo',
            name='pic1',
            field=models.CharField(default='https://upload.wikimedia.org/wikipedia/commons/f/f8/Women_in_traditional_Manobo_dress_%28Kaamulan_Festival_2017%2C_Bukidnon%2C_Philippines%29.jpg', max_length=2083),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cultureinfo',
            name='pic2',
            field=models.CharField(default='https://upload.wikimedia.org/wikipedia/commons/f/f8/Women_in_traditional_Manobo_dress_%28Kaamulan_Festival_2017%2C_Bukidnon%2C_Philippines%29.jpg', max_length=2083),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cultureinfo',
            name='pic3',
            field=models.CharField(default='https://upload.wikimedia.org/wikipedia/commons/f/f8/Women_in_traditional_Manobo_dress_%28Kaamulan_Festival_2017%2C_Bukidnon%2C_Philippines%29.jpg', max_length=2083),
            preserve_default=False,
        ),
    ]
