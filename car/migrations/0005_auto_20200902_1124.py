# Generated by Django 3.0.5 on 2020-09-02 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_auto_20200902_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='customer',
        ),
    ]
