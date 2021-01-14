from django.contrib import admin
from .models import CustomUser


class UserAdmin(admin.ModelAdmin):
    exclude = ['username']

    list_display = ('first_name', 'last_name', 'cellphone', 'is_active', 'is_confirmed')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["cellphone", 'first_name', 'last_name', 'date_joined', 'last_login', 'email']
        else:
            return []


admin.site.register(CustomUser, UserAdmin)
