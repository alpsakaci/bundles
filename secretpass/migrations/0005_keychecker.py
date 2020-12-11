# Generated by Django 3.1.3 on 2020-12-11 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('secretpass', '0004_auto_20201118_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyChecker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salt', models.CharField(max_length=24)),
                ('keyhash', models.CharField(max_length=128)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keychecker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
