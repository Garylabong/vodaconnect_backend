from django import forms
from django.forms import ModelForm

from .models import ActivationDetail, PlanDetail


class DateInput(forms.DateInput):
    input_type = "date"


class ActivationDetailForm(forms.ModelForm):
    class Meta:
        model = ActivationDetail
        fields = (
            "order_request_date",
            "request_date_initiated",
            "date_line_activated",
            "date_line_terminated",
            "phone_line_status",
            "client_company_user",
        )
        widgets = {
            "order_request_date": DateInput(),
            "request_date_initiated": DateInput(),
            "date_line_activated": DateInput(),
            "date_line_terminated": DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ActivationDetailForm, self).__init__(*args, **kwargs)
        CLIENT_COMPANY_USER_CATEGORY = (
            ("", "-------"),
            ("Vodaconnect", "Vodaconnect"),
            ("Landmaster.Us", "Landmaster.Us"),
            ("CallMe.Com.Ph", "CallMe.Com.Ph"),
            ("PsalmsGlobal.Com", "PsalmsGlobal.Com"),
        )
        self.fields["client_company_user"] = forms.ChoiceField(
            required=True,
            label="Client Company User",
            choices=CLIENT_COMPANY_USER_CATEGORY,
        )


class PlanDetailsUpdateForm(forms.ModelForm):
    class Meta:
        model = PlanDetail
        fields = (
            "plan_type",
            "total_cost",
            "due_date",
            "recurring_bill",
            "pypal_bill",
        )

    def __init__(self, *args, **kwargs):
        super(PlanDetailsUpdateForm, self).__init__(*args, **kwargs)
        PLAN_CHOICES = (
            (
                "BASIC PACKAGES/STANDARD/$4.99/MONTHLY",
                "BASIC PACKAGES/STANDARD/$4.99/MONTHLY",
            ),
            (
                "BASIC PACKAGES/PROFESSIONAL/$19.95/MONTHLY",
                "BASIC PACKAGES/PROFESSIONAL/$19.95/MONTHLY",
            ),
            (
                "BASIC PACKAGES/ENTERPRISE/$24.95/MONTHLY",
                "BASIC PACKAGES/ENTERPRISE/$24.95/MONTHLY",
            ),
            (
                "12-24 MOS. LOCK IN PLANS/STANDARD/$4.99/MONTHLY",
                "12-24 MOS. LOCK IN PLANS/STANDARD/$4.99/MONTHLY",
            ),
            (
                "12-24 MOS. LOCK IN PLANS/PROFESSIONAL/$14.99/MONTHLY",
                "12-24 MOS. LOCK IN PLANS/PROFESSIONAL/$14.99/MONTHLY",
            ),
            (
                "12-24 MOS. LOCK IN PLANS/ENTERPRISE/$19.99/MONTHLY",
                "12-24 MOS. LOCK IN PLANS/ENTERPRISE/$19.99/MONTHLY",
            ),
            (
                "TEXT AND CALL  FEATURES/STANDARD/$8.99/MONTHLY",
                "TEXT AND CALL  FEATURES/STANDARD/$8.99/MONTHLY",
            ),
            (
                "TEXT AND CALL  FEATURES/PROFESSIONAL/$21.99/MONTHLY",
                "TEXT AND CALL  FEATURES/PROFESSIONAL/$21.99/MONTHLY",
            ),
            (
                "TEXT AND CALL  FEATURES/ENTERPRISE/$29.99/MONTHLY",
                "TEXT AND CALL  FEATURES/ENTERPRISE/$29.99/MONTHLY",
            ),
            (
                "TEXT MESSAGING/Standard/$8.95/MONTHLY",
                "TEXT MESSAGING/Standard/$8.95/MONTHLY",
            ),
            (
                "TEXT MESSAGING/	Professional/$11.95/MONTHLY",
                "TEXT MESSAGING/	Professional/$11.95/MONTHLY",
            ),
            (
                "TEXT MESSAGING/	Enterprise/$14.95/MONTHLY",
                "TEXT MESSAGING/	Enterprise/$14.95/MONTHLY",
            ),
            (
                "TEXT MESSAGING/	Enterprise Plus (Volume Pricing)/$4.95 Access Fee",
                "TEXT MESSAGING/	Enterprise Plus (Volume Pricing)/$4.95 Access Fee",
            ),
            (
                "TOLL-FREE/OPTION 1/1800-$29.95/MONTHLY",
                "TOLL-FREE/OPTION 1/1800-$29.95/MONTHLY",
            ),
            (
                "TOLL-FREE/OPTION 1/1888-$29.95/MONTHLY",
                "TOLL-FREE/OPTION 1/1888-$29.95/MONTHLY",
            ),
            (
                "TOLL-FREE/OPTION 1/1877-$29.95/MONTHLY",
                "TOLL-FREE/OPTION 1/1877-$29.95/MONTHLY",
            ),
            (
                "TOLL-FREE/OPTION 1/1866-$29.95/MONTHLY",
                "TOLL-FREE/OPTION 1/1866-$29.95/MONTHLY",
            ),
            (
                "TOLL-FREE/OPTION 2/1800-$9.99/MONTHLY",
                "TOLL-FREE/OPTION 2/1800-$9.99/MONTHLY",
            ),
            (
                "TOLL-FREE/OPTION 2/1888-$9.99/MONTHLY",
                "TOLL-FREE/OPTION 2/1888-$9.99/MONTHLY",
            ),
            (
                "TOLL-FREE/OPTION 2/1877-$12.99/MONTHLY",
                "TOLL-FREE/OPTION 2/1877-$12.99/MONTHLY",
            ),
            (
                "TOLL-FREE/OPTION 2/1866-$12.99/MONTHLY",
                "TOLL-FREE/OPTION 2/1866-$12.99/MONTHLY",
            ),
            (
                "FAX NUMBER/FAX NUMBER/$7.99/MONTHLY",
                "FAX NUMBER/FAX NUMBER/$7.99/MONTHLY",
            ),
            (
                "FAX NUMBER/Porting/CAT A-$5.00,CAT C-$100.00",
                "FAX NUMBER/Porting/CAT A-$5.00,CAT C-$100.00",
            ),
            (
                "CORPORATE PACKAGES/STANDARD/$699/MONTHLY",
                "CORPORATE PACKAGES/STANDARD/$699/MONTHLY",
            ),
            (
                "CORPORATE PACKAGES/PROFESSIONAL/$1299/MONTHLY",
                "CORPORATE PACKAGES/PROFESSIONAL/$1299/MONTHLY",
            ),
            (
                "CORPORATE PACKAGES/ENTERPRISE/$2899/MONTHLY",
                "CORPORATE PACKAGES/ENTERPRISE/$2899/MONTHLY",
            ),
            (
                "VIDEO CONFERENCING/Hassle-Free Video Conferencing with WebRTC/$49 USD/MONTHLY",
                "VIDEO CONFERENCING/Hassle-Free Video Conferencing with WebRTC/$49 USD/MONTHLY",
            ),
            (
                "IP-TV - INDIVIDUAL PACKAGES/SEE TV NETWORK/$4.99/ MONTHLY",
                "IP-TV - INDIVIDUAL PACKAGES/SEE TV NETWORK/$4.99/ MONTHLY",
            ),
        )
        RECURRING_BILL_CHOICES = (
            ("Yes", "Yes"),
            ("No", "No"),
            ("Cancelled", "Cancelled"),
            ("Pending", "Pending"),
        )
        self.fields["recurring_bill"] = forms.ChoiceField(
            required=True,
            label="Did We Set Up Recurring Bill?",
            choices=RECURRING_BILL_CHOICES,
        )
        self.fields["plan_type"] = forms.ChoiceField(
            required=True,
            label="Type Of Plan",
            choices=PLAN_CHOICES,
        )
        self.fields["due_date"] = forms.DateField(
            required=True,
            label="Due Date",
            widget=forms.DateInput(
                attrs={
                    "class": "form-control1",
                    "type": "date",
                    "style": "background-color: transparent",
                    "border-color": "#ed5fdc",
                }
            ),
        )
        self.fields["pypal_bill"] = forms.CharField(
            required=True,
            label="Paypal Details for Billing",
            widget=forms.Textarea(
                attrs={
                    "class": "form-control2",
                }
            ),
        )
        self.fields["total_cost"] = forms.CharField(
            required=True,
            label="Total Cost",
            widget=forms.TextInput(attrs={"class": "form-control3", "type": "number"}),
        )
