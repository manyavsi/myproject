# Generated by Django 4.2.3 on 2023-08-14 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0002_alter_advertisement_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
