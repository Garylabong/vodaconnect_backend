# Generated by Django 3.0 on 2021-05-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20210512_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
    ]
