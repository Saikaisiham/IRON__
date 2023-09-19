from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from .views import send_email_to_user

class CustomUserAdmin(UserAdmin):
    def send_email_action(self, request, queryset):
        for user in queryset:
            send_email_to_user(user)
        self.message_user(request, f'Email sent to {queryset.count()} user(s).')
    send_email_action.short_description = "Send email to selected users"

    actions = [send_email_action]  

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
