# Generated by Django 3.2 on 2025-03-07 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20250306_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_image',
            field=models.ImageField(blank=True, upload_to='students/'),
        ),
    ]
