# Generated by Django 4.2.3 on 2023-09-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_alter_scrap_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qna',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='생성 일시'),
        ),
    ]
