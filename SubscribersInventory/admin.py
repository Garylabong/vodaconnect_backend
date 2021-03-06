from django.contrib import admin
from SubscribersInventory.models import (
    VoIpInformation,
    ActivationDetail,
    PlanDetail,
    SubscriberStatus,
    ForwardingInfo,
    TotalNumExtension,
    ZiptrunkLoginDetail,
    OtherLogin,
    Note,
    VodaConnectNumber,
)

# Register your models here.

admin.site.register(VodaConnectNumber)
admin.site.register(VoIpInformation)
admin.site.register(ActivationDetail)
admin.site.register(PlanDetail)
admin.site.register(SubscriberStatus)
admin.site.register(ForwardingInfo)
admin.site.register(TotalNumExtension)
admin.site.register(ZiptrunkLoginDetail)
admin.site.register(OtherLogin)
admin.site.register(Note)
