# Generated by Django 4.1.2 on 2023-04-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0005_remove_reviewrating_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitLater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=250)),
            ],
        ),
    ]
