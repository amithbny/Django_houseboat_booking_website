# Generated by Django 5.0 on 2023-12-24 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagetst', '0015_book_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='hotel',
            new_name='houseboat',
        ),
        migrations.AddField(
            model_name='book',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='imagetst.packages'),
        ),
        migrations.AlterField(
            model_name='book',
            name='rooms',
            field=models.PositiveSmallIntegerField(default=1, null=True),
        ),
    ]
