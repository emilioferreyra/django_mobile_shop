from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from .models import Make, Model, ProductType, Product, ProductPicture, Offer


class ModelInlines(admin.StackedInline):
    model = Model
    min_num = 1
    extra = 0


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'model']
    search_fields = ['name', 'model__name']
    list_filter = ('model',)
    inlines = [ModelInlines]


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'make']
    list_filter = ['make']
    search_fields = ['name']


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    pass


class ProductPictureInline(AdminImageMixin, admin.TabularInline):
    model = ProductPicture
    extra = 1
    max_num = 5
    min_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_main_picture',
        'product_name',
        'product_type',
    )
    list_display_links = ['product_main_picture', 'product_name']

    list_filter = (
        ('make', admin.RelatedOnlyFieldListFilter),
        ('model', admin.RelatedOnlyFieldListFilter),
        ('product_type', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = ['make__name', 'model__name']
    inlines = [ProductPictureInline]


@admin.register(Offer)
class OfferAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = [
        'get_image_tag',
        'product',
        'start_date',
        'end_date',
        'price',
        'active'
    ]

    list_display_links = ['get_image_tag', 'product']

    list_editable = ['active']
