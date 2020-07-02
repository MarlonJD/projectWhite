from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


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
        ordering = ['-last_mod']
        verbose_name = _('Stock')
        verbose_name_plural = _('Stocks')

    def increase(self, x=1):
        if self.quantity > 1:
            self.quantity += x
            self.save(update_fields=['quantity'])

    def decrease(self, x=1):
        self.quantity -= x
        self.save(update_fields=['quantity'])


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product Model. Product(name, price)
    """
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_mod = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-create_date']
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Recipt(models.Model):
    """Recipt Model()
    """
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField(max_length=500, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Shift(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='shift_set',
                             blank=True,
                             null=True)
    check_in = models.ForeignKey('CheckIn',
                                 on_delete=models.CASCADE,
                                 default=None,
                                 null=True,
                                 blank=True)
    check_out = models.ForeignKey('CheckOut',
                                  on_delete=models.CASCADE,
                                  default=None,
                                  null=True,
                                  blank=True)


class CheckIn(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='checkin_set',
                             blank=True,
                             null=True)
    date = models.DateTimeField(auto_now_add=True)


class CheckOut(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='checkout_set',
                             blank=True,
                             null=True)
    date = models.DateTimeField(auto_now_add=True)
