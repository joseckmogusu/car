# Generated by Django 3.0.5 on 2020-07-27 12:51

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
