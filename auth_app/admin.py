from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from DroneLogApp.admin import InlineDroneAppAttributes
from K9TrakApp.admin import ProfileInline
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, InlineDroneAppAttributes)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin,)
