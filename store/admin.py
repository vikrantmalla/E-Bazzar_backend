from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_image", "product_price", "product_offer", "product_status"]
    list_filter = ["product_offer", "product_status"]
    search_fields = ["product_name"]
    actions = ["make_out_of_stock", "make_in_stock"]

    def make_out_of_stock(self, request, queryset):
        rows_updated = queryset.update(product_status="out_of_stock")
        self.message_user(request, f"{rows_updated} product(s) marked as out of stock.")

    make_out_of_stock.short_description = "Mark selected product(s) as out of stock"

    def make_in_stock(self, request, queryset):
        rows_updated = queryset.update(product_status="stock")
        self.message_user(request, f"{rows_updated} product(s) marked as in stock.")

    make_in_stock.short_description = "Mark selected product(s) as in stock"

    def offer_label(self, obj):
        return "On Offer" if obj.product_offer else "Not On Offer"

    offer_label.short_description = "Offer Status"

admin.site.register(Product, ProductAdmin)