# Generated by Django 3.0 on 2021-05-13 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SubscribersInventory', '0004_auto_20210511_1557'),
        ('Billing', '0007_auto_20210513_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlycharge',
            name='client_full_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubscribersInventory.VoIpInformation'),
        ),
    ]
