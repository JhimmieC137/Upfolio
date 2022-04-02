# Generated by Django 4.0.2 on 2022-02-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_rename_name_info_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='web_images')),
                ('description', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]