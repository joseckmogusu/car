# Generated by Django 3.0.5 on 2020-09-16 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0013_auto_20200915_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_db',
            name='condition_type',
            field=models.CharField(choices=[('Used', 'Used'), ('international Used', 'international Used'), ('New', 'New')], max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('processed', 'processed'), ('done', 'done')], default='pending', max_length=20),
        ),
    ]
