# Generated by Django 4.0.6 on 2022-07-27 10:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('outputs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='output',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
