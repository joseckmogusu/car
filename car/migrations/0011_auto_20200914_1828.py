# Generated by Django 3.0.5 on 2020-09-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0010_auto_20200914_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('processed', 'processed')], default='pending', max_length=50, verbose_name='Status'),
        ),
    ]
