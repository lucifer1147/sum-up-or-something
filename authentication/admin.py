from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = CustomUser

    list_display = ('email', 'username', 'is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'first_name', 'last_name', 'description', 'profile_photo')}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser","groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'password', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions', 'profile_photo'
            )
        }),
    )

    search_fields = ('email', 'username')
    ordering = ['username']


admin.site.register(CustomUser, CustomUserAdmin)
