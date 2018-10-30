# Generated by Django 2.1.2 on 2018-10-30 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20181015_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminstylestest',
            name='filepath',
            field=models.FilePathField(allow_folders=True, blank=True, default='', help_text='this is a help text for the file path field', path='/home/alaric/Dev/Apps/DjangoAdminStyles/django-admin-styles/testproject/media', recursive=True, verbose_name='FilePathField'),
        ),
        migrations.AlterField(
            model_name='adminstylestest',
            name='onetoone',
            field=models.OneToOneField(blank=True, help_text='this is a help text for the one to one field', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='testapp_adminstylestest_onetoone', to='testapp.AdminStylesTest', verbose_name='OneToOneField'),
        ),
    ]
