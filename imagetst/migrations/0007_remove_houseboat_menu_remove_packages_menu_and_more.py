# Generated by Django 5.0 on 2023-12-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagetst', '0006_menu_houseboat_menu_packages_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houseboat',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='packages',
            name='menu',
        ),
        migrations.AddField(
            model_name='houseboat',
            name='menu',
            field=models.ManyToManyField(null=True, to='imagetst.menu'),
        ),
        migrations.AddField(
            model_name='packages',
            name='menu',
            field=models.ManyToManyField(null=True, to='imagetst.menu'),
        ),
    ]
