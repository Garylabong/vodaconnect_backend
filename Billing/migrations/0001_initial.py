# Generated by Django 3.0 on 2021-05-21 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SubscribersInventory', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('type_charge', models.CharField(blank=True, max_length=250, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True, verbose_name='Amount')),
                ('pay_ref', models.CharField(blank=True, max_length=250, null=True, verbose_name='Payment Reference')),
                ('status', models.CharField(blank=True, choices=[('Paid', 'Paid'), ('UnPaid', 'UnPaid')], max_length=150, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vodaconnect_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubscribersInventory.VodaConnectNumber')),
            ],
            options={
                'verbose_name': 'Other Charges',
                'verbose_name_plural': 'Other Charges',
                'ordering': ['type_charge'],
            },
        ),
        migrations.CreateModel(
            name='MonthlyCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_full_name', models.CharField(blank=True, max_length=500, null=True)),
                ('client_code', models.CharField(blank=True, max_length=100, null=True)),
                ('plan_type', models.CharField(blank=True, choices=[('BASIC PACKAGES/STANDARD/$4.99/MONTHLY', 'BASIC PACKAGES/STANDARD/$4.99/MONTHLY'), ('BASIC PACKAGES/PROFESSIONAL/$19.95/MONTHLY', 'BASIC PACKAGES/PROFESSIONAL/$19.95/MONTHLY'), ('BASIC PACKAGES/ENTERPRISE/$24.95/MONTHLY', 'BASIC PACKAGES/ENTERPRISE/$24.95/MONTHLY'), ('12-24 MOS. LOCK IN PLANS/STANDARD/$4.99/MONTHLY', '12-24 MOS. LOCK IN PLANS/STANDARD/$4.99/MONTHLY'), ('12-24 MOS. LOCK IN PLANS/PROFESSIONAL/$14.99/MONTHLY', '12-24 MOS. LOCK IN PLANS/PROFESSIONAL/$14.99/MONTHLY'), ('12-24 MOS. LOCK IN PLANS/ENTERPRISE/$19.99/MONTHLY', '12-24 MOS. LOCK IN PLANS/ENTERPRISE/$19.99/MONTHLY'), ('TEXT AND CALL  FEATURES/STANDARD/$8.99/MONTHLY', 'TEXT AND CALL  FEATURES/STANDARD/$8.99/MONTHLY'), ('TEXT AND CALL  FEATURES/PROFESSIONAL/$21.99/MONTHLY', 'TEXT AND CALL  FEATURES/PROFESSIONAL/$21.99/MONTHLY'), ('TEXT AND CALL  FEATURES/ENTERPRISE/$29.99/MONTHLY', 'TEXT AND CALL  FEATURES/ENTERPRISE/$29.99/MONTHLY'), ('TEXT MESSAGING/Standard/$8.95/MONTHLY', 'TEXT MESSAGING/Standard/$8.95/MONTHLY'), ('TEXT MESSAGING/\tProfessional/$11.95/MONTHLY', 'TEXT MESSAGING/\tProfessional/$11.95/MONTHLY'), ('TEXT MESSAGING/\tEnterprise/$14.95/MONTHLY', 'TEXT MESSAGING/\tEnterprise/$14.95/MONTHLY'), ('TEXT MESSAGING/\tEnterprise Plus (Volume Pricing)/$4.95 Access Fee', 'TEXT MESSAGING/\tEnterprise Plus (Volume Pricing)/$4.95 Access Fee'), ('TOLL-FREE/OPTION 1/1800-$29.95/MONTHLY', 'TOLL-FREE/OPTION 1/1800-$29.95/MONTHLY'), ('TOLL-FREE/OPTION 1/1888-$29.95/MONTHLY', 'TOLL-FREE/OPTION 1/1888-$29.95/MONTHLY'), ('TOLL-FREE/OPTION 1/1877-$29.95/MONTHLY', 'TOLL-FREE/OPTION 1/1877-$29.95/MONTHLY'), ('TOLL-FREE/OPTION 1/1866-$29.95/MONTHLY', 'TOLL-FREE/OPTION 1/1866-$29.95/MONTHLY'), ('TOLL-FREE/OPTION 2/1800-$9.99/MONTHLY', 'TOLL-FREE/OPTION 2/1800-$9.99/MONTHLY'), ('TOLL-FREE/OPTION 2/1888-$9.99/MONTHLY', 'TOLL-FREE/OPTION 2/1888-$9.99/MONTHLY'), ('TOLL-FREE/OPTION 2/1877-$12.99/MONTHLY', 'TOLL-FREE/OPTION 2/1877-$12.99/MONTHLY'), ('TOLL-FREE/OPTION 2/1866-$12.99/MONTHLY', 'TOLL-FREE/OPTION 2/1866-$12.99/MONTHLY'), ('FAX NUMBER/FAX NUMBER/$7.99/MONTHLY', 'FAX NUMBER/FAX NUMBER/$7.99/MONTHLY'), ('FAX NUMBER/Porting/CAT A-$5.00,CAT C-$100.00', 'FAX NUMBER/Porting/CAT A-$5.00,CAT C-$100.00'), ('CORPORATE PACKAGES/STANDARD/$699/MONTHLY', 'CORPORATE PACKAGES/STANDARD/$699/MONTHLY'), ('CORPORATE PACKAGES/PROFESSIONAL/$1299/MONTHLY', 'CORPORATE PACKAGES/PROFESSIONAL/$1299/MONTHLY'), ('CORPORATE PACKAGES/ENTERPRISE/$2899/MONTHLY', 'CORPORATE PACKAGES/ENTERPRISE/$2899/MONTHLY'), ('VIDEO CONFERENCING/Hassle-Free Video Conferencing with WebRTC/$49 USD/MONTHLY', 'VIDEO CONFERENCING/Hassle-Free Video Conferencing with WebRTC/$49 USD/MONTHLY'), ('IP-TV - INDIVIDUAL PACKAGES/SEE TV NETWORK/$4.99/ MONTHLY', 'IP-TV - INDIVIDUAL PACKAGES/SEE TV NETWORK/$4.99/ MONTHLY')], max_length=150, null=True, verbose_name='Type of Plan')),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True, verbose_name='Total Cost')),
                ('month_covered', models.DateField(blank=True, null=True)),
                ('date_payment', models.DateField(blank=True, null=True)),
                ('reference', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.CharField(blank=True, choices=[('Paid', 'Paid'), ('UnPaid', 'UnPaid')], max_length=150, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vodaconnect_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubscribersInventory.VodaConnectNumber')),
            ],
            options={
                'verbose_name': 'Monthly Charges',
                'verbose_name_plural': 'Monthly Charges',
                'ordering': ['reference'],
            },
        ),
    ]
