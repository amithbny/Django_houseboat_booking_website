# Generated by Django 5.0 on 2023-12-21 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagetst', '0009_rename_menu_menu_menu_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='menu_content',
            new_name='menu',
        ),
        migrations.RemoveField(
            model_name='houseboat',
            name='menu_time',
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
