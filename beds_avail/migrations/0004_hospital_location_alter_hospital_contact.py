# Generated by Django 5.1.1 on 2024-09-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beds_avail', '0003_alter_hospital_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='location',
            field=models.CharField(default='New Delhi', max_length=255),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='contact',
            field=models.CharField(default='Not Updated', max_length=13),
        ),
    ]
