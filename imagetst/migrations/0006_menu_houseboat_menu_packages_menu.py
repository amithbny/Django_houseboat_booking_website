# Generated by Django 5.0 on 2023-12-20 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagetst', '0005_rename_houseboattype_houseboat_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_time', models.CharField(max_length=100)),
                ('menu', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='houseboat',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='imagetst.menu'),
        ),
        migrations.AddField(
            model_name='packages',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='imagetst.menu'),
        ),
    ]
