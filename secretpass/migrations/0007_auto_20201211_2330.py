# Generated by Django 3.1.3 on 2020-12-11 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretpass', '0006_auto_20201211_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keychecker',
            name='keyhash',
            field=models.CharField(max_length=128),
        ),
    ]
