from django.db import models
from django.utils.translation import gettext_lazy as _


class Stock(models.Model):
    """Stock Model for Electronics. Stock(product, quantity, create_date, last_mod)
    """
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    last_mod = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name + ", quantity: " + str(self.quantity)

    class Meta:
        ordering = ['-create_date']
        verbose_name = _('Stock')
        verbose_name_plural = _('Stocks')

    def increase(self, x=1):
        if self.quantity > 1:
            self.quantity += x
            self.save(update_fields=['quantity'])

    def decrease(self, x=1):
        self.quantity -= x
        self.save(update_fields=['quantity'])


class Product(models.Model):
    """Product Model. Product(name, price)
    """
    name = models.CharField(max_length=200, unique=True)
    price = models.PositiveIntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    last_mod = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ", price: " + str(self.price)

    class Meta:
        ordering = ['-create_date']
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
