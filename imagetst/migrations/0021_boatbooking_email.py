# Generated by Django 5.0 on 2023-12-27 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagetst', '0020_remove_boatbooking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='boatbooking',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
