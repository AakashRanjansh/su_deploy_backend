# Generated by Django 4.2 on 2023-10-27 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subhakaarya_app', '0009_vendorlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendorlist',
            old_name='vedor_name',
            new_name='title',
        ),
    ]
