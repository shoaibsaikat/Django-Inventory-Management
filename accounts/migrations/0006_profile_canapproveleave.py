# Generated by Django 3.2.6 on 2021-09-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210915_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='canApproveLeave',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
