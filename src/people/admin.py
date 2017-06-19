from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import PersonType, Person


class PersonResource(resources.ModelResource):
    """
    This class allow to user import and export option
    in PersonAdmin.
    """
    class Meta:
        model = Person


@admin.register(PersonType)
class PersonTypeAdmin(admin.ModelAdmin):
    """docstring for PersonTypeAdmin"""
    ordering = ['id']


@admin.register(Person)
class PersonAdmin(AdminImageMixin, ImportExportModelAdmin):
    resources = PersonResource  # Use resources PersonResource

    fields = (
        'picture',
        'name',
        'gender',
        'person_type',
        'email',
        'phone_number',
        'address',
        'status_active'
    )
    list_display = (
        'image_tag',
        'name',
        'person_type',
        'gender',
        'email',
        'status_active'
    )
    list_display_links = ('image_tag', 'name',)
    search_fields = ['name']
    list_filter = (
        'status_active',
        'gender',
        ('person_type', admin.RelatedOnlyFieldListFilter),
    )
    ordering = ['id']
