from allauth.account.forms import SignupForm
from django import forms
from authentication.models import User, Client
from django.db import transaction
import datetime


class MyCustomSignupForm(SignupForm):
    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        DESIGNATION_CATEGORY = (
            ("Staff", "Staff"),
            ("New Client", "New Client"),
            ("Current Client", "Current Client"),
            ("Affiliate Partner", "Affiliate Partner"),
        )
        COMPANY_CATEGORY = (
            ("Vodaconnect", "Vodaconnect"),
            ("G.P.G Corporation", "G.P.G Corporation"),
            ("Landmaster.Us", "Landmaster.Us"),
            ("CallMe.Com.Ph", "CallMe.Com.Ph"),
            ("PsalmsGlobal.Com", "PsalmsGlobal.Com"),
            ("Affiliate Partner", "Affiliate Partner"),
        )
        self.fields["first_name"] = forms.CharField(required=True)
        self.fields["last_name"] = forms.CharField(required=True)
        self.fields["phone_number"] = forms.CharField(required=True)
        self.fields["create_pin"] = forms.CharField(required=True)
        self.fields["company_name"] = forms.ChoiceField(
            required=True, choices=COMPANY_CATEGORY
        )
        self.fields["designation_name"] = forms.ChoiceField(
            required=True, choices=DESIGNATION_CATEGORY
        )

    @transaction.atomic
    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.phone_number = self.cleaned_data.get("phone_number")
        user.create_pin = self.cleaned_data.get("create_pin")
        user.company_name = self.cleaned_data.get("company_name")
        user.designation_name = self.cleaned_data.get("designation_name")
        user.email = self.cleaned_data.get("email")
        user.is_client = True
        user.save()
        client = Client.objects.create(user=user)
        client.first_name = self.cleaned_data.get("first_name")
        client.last_name = self.cleaned_data.get("last_name")
        client.phone_number = self.cleaned_data.get("phone_number")
        client.email = self.cleaned_data.get("email")
        client.create_pin = self.cleaned_data.get("create_pin")
        client.company_name = self.cleaned_data.get("company_name")
        client.designation_name = self.cleaned_data.get("designation_name")
        client.save()
        return user