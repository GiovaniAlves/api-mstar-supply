# Generated by Django 4.0.6 on 2022-07-27 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
