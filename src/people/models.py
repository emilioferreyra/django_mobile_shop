from django.db import models
# from datetime import date
# from django.core.exceptions import ValidationError
# from django.shortcuts import get_object_or_404

from sorl.thumbnail import ImageField
from model_utils.models import TimeStampedModel
from audit_log.models import AuthStampedModel
from localflavor.us.models import PhoneNumberField


d = dict(
    employee=1,
    customer=2,
    contact=3
)


class EmployeeManager(models.Manager):
    """
    Manage Employees query set to only return
    person type = employee
    """

    def get_queryset(self):
        return super(EmployeeManager, self).\
            get_queryset().filter(person_type=d['employee'])


class CustomerManager(models.Manager):
    """
    Manage Customer query set to only return
    person type = customer
    """

    def get_queryset(self):
        return super(CustomerManager, self).\
            get_queryset().filter(person_type=d['customer'])


class ContactManager(models.Manager):
    """
    Manage Contact query set to only return
    person type = contact
    """

    def get_queryset(self):
        return super(ContactManager, self).\
            get_queryset().filter(person_type=d['contact'])


class PersonType(models.Model):
    """
    Stores person type information. Related objects:
    :model:`people.Person`
    """
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Person Type"
        verbose_name_plural = "Person Types"

    def __str__(self):
        return self.name


class Person(TimeStampedModel, AuthStampedModel):
    """
    Stores person information. Related objects:
    :model:`people.PersonType`
    """
    name = models.CharField(max_length=100)
    person_type = models.ForeignKey(PersonType)
    gender = models.CharField(
        max_length=1,
        choices=(
            ('M', "Male"),
            ('F', "Female"),
        ),
        null=True
    )
    email = models.EmailField(blank=True, verbose_name="e-mail")
    phone_number = PhoneNumberField(help_text='999-999-9999')
    address = models.TextField(blank=True, null=True)
    picture = ImageField(upload_to='people_pictures', null=True, blank=True)
    status_active = models.BooleanField(default=True)
    objects = models.Manager()
    employee = EmployeeManager()
    customer = CustomerManager()
    contact = ContactManager()

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.picture:
            return u'<img src="%s" width="60" height="75" />'\
                % self.picture.url
        else:
            return ' '
    image_tag.short_description = 'Photo'
    image_tag.allow_tags = True
    image_tag.admin_order_field = 'name'
