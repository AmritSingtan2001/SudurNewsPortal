# Generated by Django 4.2.4 on 2023-08-10 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_horizontalads_name_verticalads_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='horizontalads',
            name='show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='verticalads',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]