# Generated by Django 3.0 on 2021-05-05 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_request', models.DateField(blank=True, null=True)),
                ('plan_type', models.CharField(blank=True, choices=[('BASIC PACKAGES/STANDARD/$4.99/MONTHLY', 'BASIC PACKAGES/STANDARD/$4.99/MONTHLY'), ('BASIC PACKAGES/PROFESSIONAL/$19.95/MONTHLY', 'BASIC PACKAGES/PROFESSIONAL/$19.95/MONTHLY'), ('BASIC PACKAGES/ENTERPRISE/$24.95/MONTHLY', 'BASIC PACKAGES/ENTERPRISE/$24.95/MONTHLY'), ('12-24 MOS. LOCK IN PLANS/STANDARD/$4.99/MONTHLY', '12-24 MOS. LOCK IN PLANS/STANDARD/$4.99/MONTHLY'), ('12-24 MOS. LOCK IN PLANS/PROFESSIONAL/$14.99/MONTHLY', '12-24 MOS. LOCK IN PLANS/PROFESSIONAL/$14.99/MONTHLY'), ('12-24 MOS. LOCK IN PLANS/ENTERPRISE/$19.99/MONTHLY', '12-24 MOS. LOCK IN PLANS/ENTERPRISE/$19.99/MONTHLY'), ('TEXT AND CALL  FEATURES/STANDARD/$8.99/MONTHLY', 'TEXT AND CALL  FEATURES/STANDARD/$8.99/MONTHLY'), ('TEXT AND CALL  FEATURES/PROFESSIONAL/$21.99/MONTHLY', 'TEXT AND CALL  FEATURES/PROFESSIONAL/$21.99/MONTHLY'), ('TEXT AND CALL  FEATURES/ENTERPRISE/$29.99/MONTHLY', 'TEXT AND CALL  FEATURES/ENTERPRISE/$29.99/MONTHLY'), ('TEXT MESSAGING/Standard/$8.95/MONTHLY', 'TEXT MESSAGING/Standard/$8.95/MONTHLY'), ('TEXT MESSAGING/\tProfessional/$11.95/MONTHLY', 'TEXT MESSAGING/\tProfessional/$11.95/MONTHLY'), ('TEXT MESSAGING/\tEnterprise/$14.95/MONTHLY', 'TEXT MESSAGING/\tEnterprise/$14.95/MONTHLY'), ('TEXT MESSAGING/\tEnterprise Plus (Volume Pricing)/$4.95 Access Fee', 'TEXT MESSAGING/\tEnterprise Plus (Volume Pricing)/$4.95 Access Fee'), ('TOLL-FREE/OPTION 1/1800-$29.95/MONTHLY', 'TOLL-FREE/OPTION 1/1800-$29.95/MONTHLY'), ('TOLL-FREE/OPTION 1/1888-$29.95/MONTHLY', 'TOLL-FREE/OPTION 1/1888-$29.95/MONTHLY'), ('TOLL-FREE/OPTION 1/1877-$29.95/MONTHLY', 'TOLL-FREE/OPTION 1/1877-$29.95/MONTHLY'), ('TOLL-FREE/OPTION 1/1866-$29.95/MONTHLY', 'TOLL-FREE/OPTION 1/1866-$29.95/MONTHLY'), ('TOLL-FREE/OPTION 2/1800-$9.99/MONTHLY', 'TOLL-FREE/OPTION 2/1800-$9.99/MONTHLY'), ('TOLL-FREE/OPTION 2/1888-$9.99/MONTHLY', 'TOLL-FREE/OPTION 2/1888-$9.99/MONTHLY'), ('TOLL-FREE/OPTION 2/1877-$12.99/MONTHLY', 'TOLL-FREE/OPTION 2/1877-$12.99/MONTHLY'), ('TOLL-FREE/OPTION 2/1866-$12.99/MONTHLY', 'TOLL-FREE/OPTION 2/1866-$12.99/MONTHLY'), ('FAX NUMBER/FAX NUMBER/$7.99/MONTHLY', 'FAX NUMBER/FAX NUMBER/$7.99/MONTHLY'), ('FAX NUMBER/Porting/CAT A-$5.00,CAT C-$100.00', 'FAX NUMBER/Porting/CAT A-$5.00,CAT C-$100.00'), ('CORPORATE PACKAGES/STANDARD/$699/MONTHLY', 'CORPORATE PACKAGES/STANDARD/$699/MONTHLY'), ('CORPORATE PACKAGES/PROFESSIONAL/$1299/MONTHLY', 'CORPORATE PACKAGES/PROFESSIONAL/$1299/MONTHLY'), ('CORPORATE PACKAGES/ENTERPRISE/$2899/MONTHLY', 'CORPORATE PACKAGES/ENTERPRISE/$2899/MONTHLY'), ('VIDEO CONFERENCING/Hassle-Free Video Conferencing with WebRTC/$49 USD/MONTHLY', 'VIDEO CONFERENCING/Hassle-Free Video Conferencing with WebRTC/$49 USD/MONTHLY'), ('IP-TV - INDIVIDUAL PACKAGES/SEE TV NETWORK/$4.99/ MONTHLY', 'IP-TV - INDIVIDUAL PACKAGES/SEE TV NETWORK/$4.99/ MONTHLY')], max_length=150, null=True, verbose_name='Type of Plan')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Complete Address ( Incase of porting)')),
                ('preferred_code', models.CharField(blank=True, max_length=150, null=True, verbose_name='Prepared Area Code')),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='total Number Of Phone Lines Needed')),
                ('fax', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=150, null=True, verbose_name='Do You Need Fax?')),
                ('request', models.CharField(blank=True, choices=[('New Number Request', 'New Number Request'), ('Porting Request', 'Porting Request'), ('Other Request', 'Other Request')], max_length=150, null=True, verbose_name='Type Of Request')),
                ('category_request', models.CharField(blank=True, choices=[('Connect to CallMe.Com.Ph', 'Connect to CallMe.Com.Ph'), ('Connect to PsalmsGlobal', 'Connect to PsalmsGlobal'), ('Personal Use', 'Personal Use'), ('Business Use', 'Business Use'), ('Others', 'Others')], max_length=150, null=True, verbose_name='Category Of Request')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='PayPal Email Address for Billing')),
                ('order_status', models.CharField(blank=True, choices=[('New Order', 'New Order'), ('Pending Request', 'Pending Request'), ('Processing', 'Processing'), ('Follow-up with the Client', 'Follow-up with the Client'), ('Declined', 'Declined'), ('Order Complete', 'Order Complete')], max_length=150, null=True, verbose_name='Order Status')),
                ('notes', models.TextField(blank=True, null=True)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Client', verbose_name='Company Name ( That will appear in your caller ID)')),
            ],
        ),
    ]
