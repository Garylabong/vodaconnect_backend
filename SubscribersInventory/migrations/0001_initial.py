# Generated by Django 3.0 on 2021-05-21 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForwardingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forwarding_num', models.CharField(blank=True, max_length=100, null=True, verbose_name='Forwarding Number: (Customer Phone Line)')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Forwarding Information',
                'verbose_name_plural': 'Forwarding Information',
                'ordering': ['forwarding_num'],
            },
        ),
        migrations.CreateModel(
            name='VodaConnectNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vodaconnect_number', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ZiptrunkLoginDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ziptrunk_logins', models.CharField(blank=True, max_length=100, null=True)),
                ('ziptrunk_details', models.TextField(blank=True, max_length=100, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VoIpInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_full_name', models.CharField(blank=True, max_length=500, null=True)),
                ('company_name', models.CharField(blank=True, max_length=500, null=True)),
                ('client_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.ClientCode')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vodaconnect_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubscribersInventory.VodaConnectNumber')),
            ],
            options={
                'verbose_name': 'VoIpInformation',
                'verbose_name_plural': 'VoIpInformation',
                'ordering': ['client_full_name'],
            },
        ),
        migrations.CreateModel(
            name='TotalNumExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extension_logins', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('extension_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubscribersInventory.ForwardingInfo', verbose_name='Extension Number')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriberStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat_production', models.CharField(choices=[('New Prospect', 'New Prospect'), ('New Request', 'New Request'), ('Pending Request', 'Pending Request'), ('Call/Email Follow up', 'Call/Email Follow up'), ('Ready to Start', 'Ready to Start'), ('Sign up - Ready for Set up', 'PendSign up - Ready for Set uping'), ('Active - Live in Production', 'Active - Live in Production'), ('Request for Cancellation', 'Request for Cancellation'), ('Email sent for Cancellation', 'Email sent for Cancellation'), ('Account Cancelled by Vodaconnect', 'Account Cancelled by Vodaconnect'), ('Recurring Charge Cancelled', 'Recurring Charge Cancelled'), ('Account Cancelled', 'Account Cancelled')], max_length=100, verbose_name='Status In Production')),
                ('type_of_request', models.CharField(choices=[('New Number Request', 'New Number Request'), ('Porting Request', 'Porting Request'), ('Other Request', 'Other Request')], max_length=100, verbose_name='Type of Request ')),
                ('ready_for_testimony', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Not Applicable', 'Not Applicable')], max_length=100, verbose_name='Ready For Testimony?')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Subscriber Status',
                'verbose_name_plural': 'Subscriber Status',
                'ordering': ['stat_production'],
            },
        ),
        migrations.CreateModel(
            name='PlanDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_type', models.CharField(blank=True, choices=[('BASIC PACKAGES/STANDARD/$4.99/MONTHLY', 'BASIC PACKAGES/STANDARD/$4.99/MONTHLY'), ('BASIC PACKAGES/PROFESSIONAL/$19.95/MONTHLY', 'BASIC PACKAGES/PROFESSIONAL/$19.95/MONTHLY'), ('BASIC PACKAGES/ENTERPRISE/$24.95/MONTHLY', 'BASIC PACKAGES/ENTERPRISE/$24.95/MONTHLY'), ('12-24 MOS. LOCK IN PLANS/STANDARD/$4.99/MONTHLY', '12-24 MOS. LOCK IN PLANS/STANDARD/$4.99/MONTHLY'), ('12-24 MOS. LOCK IN PLANS/PROFESSIONAL/$14.99/MONTHLY', '12-24 MOS. LOCK IN PLANS/PROFESSIONAL/$14.99/MONTHLY'), ('12-24 MOS. LOCK IN PLANS/ENTERPRISE/$19.99/MONTHLY', '12-24 MOS. LOCK IN PLANS/ENTERPRISE/$19.99/MONTHLY'), ('TEXT AND CALL  FEATURES/STANDARD/$8.99/MONTHLY', 'TEXT AND CALL  FEATURES/STANDARD/$8.99/MONTHLY'), ('TEXT AND CALL  FEATURES/PROFESSIONAL/$21.99/MONTHLY', 'TEXT AND CALL  FEATURES/PROFESSIONAL/$21.99/MONTHLY'), ('TEXT AND CALL  FEATURES/ENTERPRISE/$29.99/MONTHLY', 'TEXT AND CALL  FEATURES/ENTERPRISE/$29.99/MONTHLY'), ('TEXT MESSAGING/Standard/$8.95/MONTHLY', 'TEXT MESSAGING/Standard/$8.95/MONTHLY'), ('TEXT MESSAGING/\tProfessional/$11.95/MONTHLY', 'TEXT MESSAGING/\tProfessional/$11.95/MONTHLY'), ('TEXT MESSAGING/\tEnterprise/$14.95/MONTHLY', 'TEXT MESSAGING/\tEnterprise/$14.95/MONTHLY'), ('TEXT MESSAGING/\tEnterprise Plus (Volume Pricing)/$4.95 Access Fee', 'TEXT MESSAGING/\tEnterprise Plus (Volume Pricing)/$4.95 Access Fee'), ('TOLL-FREE/OPTION 1/1800-$29.95/MONTHLY', 'TOLL-FREE/OPTION 1/1800-$29.95/MONTHLY'), ('TOLL-FREE/OPTION 1/1888-$29.95/MONTHLY', 'TOLL-FREE/OPTION 1/1888-$29.95/MONTHLY'), ('TOLL-FREE/OPTION 1/1877-$29.95/MONTHLY', 'TOLL-FREE/OPTION 1/1877-$29.95/MONTHLY'), ('TOLL-FREE/OPTION 1/1866-$29.95/MONTHLY', 'TOLL-FREE/OPTION 1/1866-$29.95/MONTHLY'), ('TOLL-FREE/OPTION 2/1800-$9.99/MONTHLY', 'TOLL-FREE/OPTION 2/1800-$9.99/MONTHLY'), ('TOLL-FREE/OPTION 2/1888-$9.99/MONTHLY', 'TOLL-FREE/OPTION 2/1888-$9.99/MONTHLY'), ('TOLL-FREE/OPTION 2/1877-$12.99/MONTHLY', 'TOLL-FREE/OPTION 2/1877-$12.99/MONTHLY'), ('TOLL-FREE/OPTION 2/1866-$12.99/MONTHLY', 'TOLL-FREE/OPTION 2/1866-$12.99/MONTHLY'), ('FAX NUMBER/FAX NUMBER/$7.99/MONTHLY', 'FAX NUMBER/FAX NUMBER/$7.99/MONTHLY'), ('FAX NUMBER/Porting/CAT A-$5.00,CAT C-$100.00', 'FAX NUMBER/Porting/CAT A-$5.00,CAT C-$100.00'), ('CORPORATE PACKAGES/STANDARD/$699/MONTHLY', 'CORPORATE PACKAGES/STANDARD/$699/MONTHLY'), ('CORPORATE PACKAGES/PROFESSIONAL/$1299/MONTHLY', 'CORPORATE PACKAGES/PROFESSIONAL/$1299/MONTHLY'), ('CORPORATE PACKAGES/ENTERPRISE/$2899/MONTHLY', 'CORPORATE PACKAGES/ENTERPRISE/$2899/MONTHLY'), ('VIDEO CONFERENCING/Hassle-Free Video Conferencing with WebRTC/$49 USD/MONTHLY', 'VIDEO CONFERENCING/Hassle-Free Video Conferencing with WebRTC/$49 USD/MONTHLY'), ('IP-TV - INDIVIDUAL PACKAGES/SEE TV NETWORK/$4.99/ MONTHLY', 'IP-TV - INDIVIDUAL PACKAGES/SEE TV NETWORK/$4.99/ MONTHLY')], max_length=150, null=True, verbose_name='Type of Plan')),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True, verbose_name='Total Cost')),
                ('recurring_bill', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Cancelled', 'Cancelled'), ('Pending', 'Pending')], max_length=100, verbose_name='Did we set up recurring bill?')),
                ('pypal_bill', models.TextField(blank=True, null=True, verbose_name='Paypal Details for Billing')),
                ('due_date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Plan Details',
                'verbose_name_plural': 'Plan Details',
                'ordering': ['pypal_bill'],
            },
        ),
        migrations.CreateModel(
            name='OtherLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_logins', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ActivationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_request_date', models.DateField(null=True)),
                ('request_date_initiated', models.DateField(null=True)),
                ('date_line_activated', models.DateField(null=True)),
                ('date_line_terminated', models.DateField(null=True)),
                ('phone_line_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Cancelled', 'Cancelled'), ('Pending', 'Pending')], max_length=100)),
                ('client_company_user', models.CharField(blank=True, choices=[('Vodaconnect', 'Vodaconnect'), ('Landmaster.Us', 'Landmaster.Us'), ('CallMe.Com.Ph', 'CallMe.Com.Ph'), ('PsalmsGlobal.Com', 'PsalmsGlobal.Com')], max_length=150, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Activation Details',
                'verbose_name_plural': 'Activation Details',
                'ordering': ['client_company_user'],
            },
        ),
    ]
