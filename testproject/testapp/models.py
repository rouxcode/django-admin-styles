from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class AdminStylesTest(models.Model):

    boolean = models.BooleanField(
        default=True,
        verbose_name='boolean',
        help_text='this is a help text for the boolean field',
    )
    char = models.CharField(
        max_length=250,

        verbose_name='charfield',
        help_text='this is a help text for the char field'
    )
    char_choices = models.CharField(
        max_length=250,
        choices=[
            ('one', 'one'),
            ('two', 'two'),
            ('three', 'three'),
            ('four', 'alkdsjalksdj asdlkj asdlkajs dlakjds lakjdslkajsd l'),
        ],
        verbose_name='charfield choices',
        help_text='this is a help text for the char field choices'
    )
    date = models.DateField(
        default=timezone.now,
        verbose_name='DateField',
        help_text='this is a help text for the date field'
    )
    datetime = models.DateTimeField(
        default=timezone.now,
        verbose_name='DateTimeField',
        help_text='this is a help text for the date time field'
    )
    decimal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='DecimalField',
        help_text='this is a help text for the date decimal field'
    )
    duration = models.DurationField(
        verbose_name='DurationField',
        help_text='this is a help text for the date duration field'
    )
    email = models.EmailField(
        verbose_name='EmailField',
        help_text='this is a help text for the date email field'
    )
    file = models.FileField(
        upload_to='testapp',
        blank=True,
        default='',
        verbose_name='FileField',
        help_text='this is a help text for the file field'
    )
    filepath = models.FilePathField(
        path=settings.MEDIA_ROOT,
        recursive=True,
        allow_files=True,
        allow_folders=True,
        blank=True,
        default='',
        verbose_name='FilePathField',
        help_text='this is a help text for the file path field'
    )
    float = models.FloatField(
        verbose_name='FloatField',
        help_text='this is a help text for the float field'
    )
    image = models.ImageField(
        upload_to='testapp',
        blank=True,
        default='',
        verbose_name='ImageField',
        help_text='this is a help text for the image field'
    )
    integer = models.IntegerField(
        verbose_name='IntegerField',
        help_text='this is a help text for the integer field'
    )
    ipaddress = models.GenericIPAddressField(
        verbose_name='GenericIPAddressField',
        help_text='this is a help text for the ip address field'
    )
    text = models.TextField(
        verbose_name='TextField',
        help_text='this is a help text for the text field'
    )
    time = models.TimeField(
        verbose_name='TimeField',
        help_text='this is a help text for the time field'
    )
    url = models.URLField(
        verbose_name='URLField',
        help_text='this is a help text for the url field'
    )

    foreignkey_a = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_foreignkey_a',
        verbose_name='ForeignKey A',
        help_text='this is a help text for the foreign key field a'
    )
    foreignkey_b = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_foreignkey_b',
        verbose_name='ForeignKey B',
        help_text='this is a help text for the foreign key field b'
    )
    manytomany_a = models.ManyToManyField(
        'self',
        blank=True,
        verbose_name='ManyToManyField A',
        help_text='this is a help text for the many to many field a'
    )
    manytomany_b = models.ManyToManyField(
        'self',
        blank=True,
        verbose_name='ManyToManyField B',
        help_text='this is a help text for the many to many field b'
    )
    manytomany_c = models.ManyToManyField(
        'self',
        blank=True,
        verbose_name='ManyToManyField C',
        help_text='this is a help text for the many to many field c'
    )
    manytomany_d = models.ManyToManyField(
        'self',
        blank=True,
        verbose_name='ManyToManyField D',
        help_text='this is a help text for the many to many field d'
    )
    onetoone = models.OneToOneField(
        'self',
        null=True,
        blank=True,
        related_name='%(app_label)s_%(class)s_onetoone',
        verbose_name='OneToOneField',
        help_text='this is a help text for the one to one field'
    )

    class Meta:
        ordering = [
            'id',
        ]
        verbose_name = 'AdminStylesTest'
        verbose_name_plural = 'AdminStylesTests'

    def __str__(self):
        return 'AdminStylesTest {}'.format(self.id)
