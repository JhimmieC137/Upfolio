# Generated by Django 4.0.2 on 2022-02-11 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_info_name_alter_info_heading_alter_info_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='name',
            new_name='about',
        ),
    ]