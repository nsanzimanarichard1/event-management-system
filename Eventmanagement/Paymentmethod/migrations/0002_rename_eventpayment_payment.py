# Generated by Django 4.2.2 on 2023-07-04 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0001_initial'),
        ('Participant', '0001_initial'),
        ('Paymentmethod', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventPayment',
            new_name='Payment',
        ),
    ]
