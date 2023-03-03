from django.contrib import admin

from application.models import Account, Device, Complaint


class AccountAdmin(admin.ModelAdmin):
    fields = ('number', 'date', 'paid',)
    search_fields = ('number',)


class DeviceAdmin(admin.ModelAdmin):
    fields = ('name',)


class ComplaintAdmin(admin.ModelAdmin):
    fields = ('number', 'date', 'completed_date',
              'date_at_work',
              'files_attached',
              'status',
              'description',
              'address_main',
              'address_additional',
              'client_name',
              'client_phone',
              'client_email',
              'device_type',
              'additional_comment',
              'price',
              'transport_hours',
              'act_photo',
              'account',)


admin.site.register(Account, AccountAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Complaint, ComplaintAdmin)
