# Generated by Django 4.0.4 on 2022-06-21 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_booking_roomnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='roomNumber',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
