# Generated by Django 4.0.6 on 2022-07-27 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outputs', '0002_output_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='output',
            name='created_at',
        ),
    ]
