from __future__ import unicode_literals

from django import forms
from django.contrib import admin

from .models import AdminStylesTest


class AdminStylesTestInlineForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = AdminStylesTest
        widgets = {
            'foreignkey_a': forms.Select,
            'foreignkey_b': forms.RadioSelect,
            'manytomany_b': forms.CheckboxSelectMultiple,
        }


class AdminStylesTestInline(admin.StackedInline):

    extra = 0
    fk_name = 'foreignkey_a'
    filter_horizontal = [
        'manytomany_c',
    ]
    filter_vertical = [
        'manytomany_d',
    ]
    form = AdminStylesTestInlineForm
    model = AdminStylesTest


class AdminStylesTestAdminForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = AdminStylesTest
        widgets = {
            'foreignkey_a': forms.Select,
            'foreignkey_b': forms.RadioSelect,
            'manytomany_b': forms.CheckboxSelectMultiple,
        }


class AdminStylesTestAdmin(admin.ModelAdmin):

    filter_horizontal = [
        'manytomany_c',
    ]
    filter_vertical = [
        'manytomany_d',
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
                'onetoone',
                'foreignkey_a',
                'foreignkey_b',
                'manytomany_a',
                'manytomany_b',
                'manytomany_c',
                'manytomany_d',
            ],
        }),
    ]


admin.site.register(AdminStylesTest, AdminStylesTestAdmin)
