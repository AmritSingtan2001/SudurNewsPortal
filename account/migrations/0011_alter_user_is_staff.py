# Generated by Django 4.2.4 on 2023-08-04 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_rename_name_user_fullname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]