from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    fields = (
        'id', 'username', 'email', 
        'is_active', 'is_staff', 'is_superuser', 
    )
    list_display = (
        'id', 'username', 'email', 
        'is_active', 'is_staff', 'is_superuser', 
    )
    list_editable = (
        'is_active', 'is_staff', 'is_superuser',
    )
    search_fields = (
        'id', 'username', 'email', 
        'is_active', 'is_staff', 'is_superuser', 
    )
    readonly_fields = (
        'id',
    )


admin.site.register(User, UserAdmin)