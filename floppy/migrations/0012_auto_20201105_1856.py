# Generated by Django 3.1.2 on 2020-11-05 15:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floppy', '0011_auto_20201105_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notelog',
            name='change_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
