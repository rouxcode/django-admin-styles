from __future__ import unicode_literals

from django import forms
from django.contrib import admin

from .models import AdminStylesTest, AdminStylesTestProxy


class AdminStylesTestAdminForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = AdminStylesTest
        widgets = {
            'foreignkey_a': forms.Select,
            'foreignkey_b': forms.RadioSelect,
            'manytomany_b': forms.SelectMultiple,
            'manytomany_c': forms.CheckboxSelectMultiple,
        }


class AdminStylesTestAdmin(admin.ModelAdmin):

    filter_horizontal = [
        'manytomany_d',
    ]
    filter_vertical = [
        'manytomany_e',
    ]
    form = AdminStylesTestAdminForm


admin.site.register(AdminStylesTest, AdminStylesTestAdmin)


class AdminStylesTestProxyAdmin(admin.ModelAdmin):

    filter_horizontal = [
        'manytomany_d',
    ]
    filter_vertical = [
        'manytomany_e',
    ]
    form = AdminStylesTestAdminForm

    fieldsets = [
        (None, {
            'fields': [
                'boolean',
                'char',
                'char_choices',
                'date',
                'datetime',
                'decimal',
                'duration',
                'email',
                'float',
                'integer',
                'ipaddress',
                'text',
                'time',
                'url',
            ]
        }),
        ('File', {
            'fields': [
                'file',
                'filepath',
                'image',
            ],
        }),
        ('Related', {
            'classes': [
                'collapse',
            ],
            'fields': [
                'foreignkey_a',
                'foreignkey_b',
                'manytomany_a',
                'manytomany_b',
                'manytomany_c',
                'manytomany_d',
                'manytomany_e',
                'onetoone',
            ],
        }),
    ]


admin.site.register(AdminStylesTestProxy, AdminStylesTestProxyAdmin)
