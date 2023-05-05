from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_image = models.ImageField(upload_to = 'images')
    product_price = models.IntegerField()
    product_offer = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name