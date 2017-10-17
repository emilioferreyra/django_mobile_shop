from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator

from sorl.thumbnail import ImageField
from model_utils.models import TimeStampedModel
from audit_log.models import AuthStampedModel
from smart_selects.db_fields import ChainedForeignKey


class ProductType(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        verbose_name = "ProductType"
        verbose_name_plural = "ProductTypes"

    def __str__(self):
        return self.name


class Make(models.Model):
    name = models.CharField(unique=True, max_length=50)
    product_type = models.ForeignKey(ProductType, default=1)

    class Meta:
        verbose_name = "Make"
        verbose_name_plural = "Makes"

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(unique=True, max_length=50)
    make = models.ForeignKey(Make)

    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Models"

    def __str__(self):
        return self.name


class ProductFeature(models.Model):

    class Meta:
        verbose_name = "Product Feature"
        verbose_name_plural = "Product Features"

    def __str__(self):
        pass


class Product(TimeStampedModel, AuthStampedModel):
    make = models.ForeignKey(Make)
    model = ChainedForeignKey(
        Model,
        chained_field="make",
        chained_model_field="make",
    )

    product_type = models.ForeignKey(ProductType, default=1)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        unique_together = (('make', 'model'),)

    def __str__(self):
        return '%s %s' % (self.make, self.model)

    def product_name(self):
        return '%s %s' % (self.make, self.model)

    product_name.short_description = "Product Name"
    product_name.allow_tags = True
    product_name.admin_order_field = 'id'

    def product_main_picture(self):
        """
        Returns product main picture, the first on
        """
        picture = ProductPicture.objects.filter(product_id=self.id).first()
        if picture:
            return u'<img src="%s" width="60" height="75" />'\
                % picture
        else:
            return ' '

    product_main_picture.short_description = "Picture"
    product_main_picture.allow_tags = True
    product_main_picture.admin_order_field = 'id'


class ProductPicture(models.Model):
    product = models.ForeignKey(Product)
    picture = ImageField(upload_to='product_pictures', null=True, blank=True)

    class Meta:
        verbose_name = "Product Picture"
        verbose_name_plural = "Product Pictures"

    def __str__(self):
        return '%s' % (self.picture.url)

    def get_image_tag(self):
        if self.picture:
            return u'<img src="%s" width="60" height="75" />'\
                % self.picture.url
        else:
            return ' '
    get_image_tag.short_description = 'Photo'
    get_image_tag.allow_tags = True
    # get_image_tag.admin_order_field = 'name'


class Offer(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    product = models.ForeignKey(Product)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    reviews = models.PositiveIntegerField(null=True)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.TextField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    picture = ImageField(upload_to='product_pictures', null=True, blank=True)

    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"

    def __str__(self):
        return str(self.product)

    def get_image_tag(self):
        if self.picture:
            return u'<img src="%s" width="60" height="75" />'\
                % self.picture.url
        else:
            return ' '
    get_image_tag.short_description = 'Photo'
    get_image_tag.allow_tags = True
