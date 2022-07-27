# Generated by Django 4.0.6 on 2022-07-26 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('registration_number', models.CharField(max_length=20)),
                ('manufacturer', models.CharField(max_length=255)),
                ('type', models.BooleanField(max_length=120)),
                ('description', models.BooleanField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
