from django.contrib import admin

from shop.models import Category, Contact_us,Product,ProductImage,Type, About, Feature


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact_us)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'reason', 'subject')
    search_fields = ('name', )
    list_filter = ('reason',)
    date_hierarchy = 'created_at'
    ordering = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('start_date',"end_date","title", "description",)
    date_hierarchy = 'start_date'

@admin.register(Feature)
class Feature(admin.ModelAdmin):
    pass
