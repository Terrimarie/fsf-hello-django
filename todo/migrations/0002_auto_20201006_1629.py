# Generated by Django 3.1.1 on 2020-10-06 16:29
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='dome',
            new_name='done',
        ),
    ]
