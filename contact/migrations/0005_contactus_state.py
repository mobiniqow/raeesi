# Generated by Django 4.1.7 on 2023-03-02 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_remove_contactus_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='state',
            field=models.IntegerField(choices=[(0, 'Unread'), (1, 'Read')], default=0),
        ),
    ]
