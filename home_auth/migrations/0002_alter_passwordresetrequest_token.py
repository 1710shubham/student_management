# Generated by Django 3.2 on 2025-03-07 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='zORu1zsNBYtp7HFCuhECd4nzeJMVbxsH', editable=False, max_length=100, unique=True),
        ),
    ]
