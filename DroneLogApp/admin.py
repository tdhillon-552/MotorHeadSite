from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from . models import DroneTable

admin.site.register(DroneTable)
admin.site.register(ReasonTable)
admin.site.register(MissionTable)


class ProfileInline(admin.StackedInline):
    model = DroneLogAttributes
    can_delete = False
    verbose_name = 'DroneLog Application Attributes'
    verbose_name_plural = 'test'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


