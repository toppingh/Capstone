# Generated by Django 4.2.3 on 2023-09-15 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_result'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Result',
        ),
    ]