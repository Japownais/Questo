# Generated by Django 5.0.3 on 2024-03-22 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_tests_cdn_vestibular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tests',
            name='cdn_vestibular',
            field=models.TextField(),
        ),
    ]
