from django.db import models


class ProductStatusChoices(object):
    stock = "stock"
    out_of_stock = "out_of_stock"

    choices = (
        (stock, "Stock"),
        (out_of_stock, "Out of Stock"),
    )

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_image = models.ImageField(upload_to="images")
    product_price = models.IntegerField()
    product_offer = models.BooleanField(default=False)
    product_status = models.CharField(
        max_length=12,
        choices=ProductStatusChoices.choices,
        default=ProductStatusChoices.stock,
    )

    def __str__(self):
        return self.product_name
