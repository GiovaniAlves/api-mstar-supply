# Generated by Django 4.0.6 on 2022-07-28 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0003_remove_input_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='type',
            field=models.CharField(default='input', max_length=120),
        ),
    ]
