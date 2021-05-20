from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ActivationDetailForm, PlanDetailsUpdateForm
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.views import View
from .views import *
from .models import *


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "SubscribersInventory/home.html"


class SubsInvView(LoginRequiredMixin, TemplateView):
    template_name = "SubscribersInventory/subs_inventory.html"


class VoipListView(LoginRequiredMixin, ListView):
    model = VoIpInformation
    context_object_name = "list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)
        return context


class VoipDetailView(DetailView):
    model = VoIpInformation
    context_object_name = "detail"
    template_name = "SubscribersInventory/voipinformation_detail.html"


class ActivationDetailListView(LoginRequiredMixin, ListView):
    model = ActivationDetail
    context_object_name = "list"
    template_name = "SubscribersInventory/activationdetail_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)
        return context


class ActivationDetailAddView(SuccessMessageMixin, CreateView):
    model = ActivationDetail
    form_class = ActivationDetailForm
    context_object_name = "add"
    template_name = "SubscribersInventory/activationdetails_addview.html"
    success_message = "%(activationdetail)s created successfully"

    def form_valid(self, form):
        activationdetail = form.save(commit=False)
        activationdetail.user = self.request.user
        activationdetail.save()
        messages.success(self.request, "You have been Created a Details!")
        return redirect("subs_Inv:activation_details_list")


class PlanDetailsListView(LoginRequiredMixin, ListView):
    model = PlanDetail
    context_object_name = "list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)
        return context


class PlanDetailsUpdateView(LoginRequiredMixin, UpdateView):
    model = PlanDetail
    form_class = PlanDetailsUpdateForm
    template_name = "SubscribersInventory/plandetail_form.html"
    success_url = reverse_lazy("subs_Inv:plan_details")
    # form_class = MonthlyChargeUpdateForm
    # template_name = "Billing/monthlycharge_Update.html"
    # success_url = reverse_lazy("bill:month_list")


class SubscribersStatusView(TemplateView):
    template_name = "SubscribersInventory/subs_status.html"


class ForwardingInfoView(TemplateView):
    template_name = "SubscribersInventory/forwarding_info.html"


class ProfileView(TemplateView):
    template_name = "SubscribersInventory/profile.html"


class OtherChargeView(TemplateView):
    template_name = "SubscribersInventory/other_charge.html"


class MonthlyChargeView(TemplateView):
    template_name = "SubscribersInventory/monthly_charge.html"


class OrderRequestView(TemplateView):
    template_name = "SubscribersInventory/order_request.html"
