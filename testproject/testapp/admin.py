from django import forms
from django.contrib import admin

from .models import AdminStylesTest, SimpleInlineTest


class SimpleInlineTestInlineForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = SimpleInlineTest
        widgets = {}


class SimpleInlineTestInline(admin.TabularInline):

    extra = 0
    form = SimpleInlineTestInlineForm
    model = SimpleInlineTest


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
    list_per_page = 3
    inlines = [
        SimpleInlineTestInline,
        AdminStylesTestInline,
    ]
    search_fields = [
        'char',
    ]
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
                (
                    'email',
                    'float',
                    'integer',
                    'ipaddress',
                    'text',
                ),
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

        ('Filer', {
            'fields': [
                'filer_file',
                'filer_image',
            ],
        }),
    ]
    list_display = [
        '__str__',
        'boolean',
        'char',
        'char_choices',
    ]
    list_editable = [
        'boolean',
        'char',
        'char_choices',
    ]
    list_filter = [
        'boolean',
        'char',
        'char_choices',
        'date',
        'datetime',
        'decimal',
        'duration',
    ]


admin.site.register(AdminStylesTest, AdminStylesTestAdmin)
