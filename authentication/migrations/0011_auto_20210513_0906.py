# Generated by Django 3.0 on 2021-05-13 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_auto_20210513_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='profile_picture',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
    ]