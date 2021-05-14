# Generated by Django 3.0 on 2021-05-14 11:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('SubscribersInventory', '0004_auto_20210511_1557'),
        ('AccountFiles', '0018_auto_20210514_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountfile',
            name='client_full_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubscribersInventory.VoIpInformation'),
        ),
        migrations.AlterField(
            model_name='accountfile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]