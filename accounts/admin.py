from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm 
from .models import CustomUser
from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.utils import unquote
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import (
    AdminPasswordChangeForm, UserChangeForm, UserCreationForm,
)
from django.contrib.auth.models import Group, User
from django.core.exceptions import PermissionDenied
from django.db import router, transaction
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.utils.decorators import method_decorator
from django.utils.html import escape
from django.utils.translation import gettext, gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters


class CustomUserAdmin(UserAdmin): 
   # add_form = CustomUserCreationForm 
   # form = CustomUserChangeForm 
    model = CustomUser
    list_per_page = 25
    list_display = ['username', 'email', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', ]
    list_editable = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        ('CUSTOMER INFORMATION',{'fields': ['email', 'address', 'city', 'postCode', 'country', 'phone']}),
        ('DELIVERY INFORMATION',{'fields': ('shippingName', 'shippingAddress', 'shippingCity', 'shippingPostcode', 'shippingCountry', 'deliveryPhone', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)