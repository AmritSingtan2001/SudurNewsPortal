# Generated by Django 4.2.4 on 2023-08-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_discriptions_ourteam_about_our_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='title',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ourteam',
            name='title',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='privacypolicy',
            name='title',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
