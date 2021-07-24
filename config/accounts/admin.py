from django import forms
from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomCreationForm,CustomUserChangeForm


class CustomUserAdmin(UserAdmin):

    add_form = CustomCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['email','username','last_name','age','is_staff','address']
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('age','address',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('age','address',)}),
    )

admin.site.register(CustomUser,CustomUserAdmin)
