# Generated by Django 4.0.4 on 2022-06-20 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=10000)),
                ('customerEmail', models.EmailField(max_length=254)),
                ('custOccupation', models.CharField(max_length=10000)),
                ('roomNumber', models.CharField(max_length=10000)),
                ('numberOfNight', models.IntegerField()),
                ('checkIn', models.DateField()),
                ('checkOut', models.DateField()),
                ('bill', models.CharField(max_length=10000)),
            ],
        ),
    ]
