# Generated by Django 3.0 on 2021-05-12 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_remove_client_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]