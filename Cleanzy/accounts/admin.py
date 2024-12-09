from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from Cleanzy.accounts.forms import CleanzyUserCreationForm, CleanzyUserChangeForm


user = get_user_model()

@admin.register(user)
class AppUserAdmin(UserAdmin):
    add_form = CleanzyUserCreationForm
    form = CleanzyUserChangeForm
    list_display = ('pk', 'username', 'email', 'is_staff', 'is_active')
    fieldsets = (
        ('Information', {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username', 'email',)
    ordering = ('pk',)
    readonly_fields = ('last_login',)
