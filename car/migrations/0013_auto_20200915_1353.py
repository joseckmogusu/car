# Generated by Django 3.0.5 on 2020-09-15 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0012_auto_20200915_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('processed', 'processed'), ('done', 'done')], default='pending', max_length=100),
        ),
    ]