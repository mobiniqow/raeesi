# Generated by Django 4.1.7 on 2023-03-02 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_part_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='part',
        ),
    ]
