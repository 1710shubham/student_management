# Generated by Django 3.2 on 2025-03-06 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_parent_mother_occupation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='permanent_address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='parent',
            name='present_address',
            field=models.TextField(),
        ),
    ]
