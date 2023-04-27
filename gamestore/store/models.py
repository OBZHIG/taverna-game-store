from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    money = models.IntegerField(default = 0)

    # add additional fields in here

    def __str__(self):
        return self.username




class services(models.Model):
    title = models.TextField(unique=True)
    description = models.TextField()
    price = models.FloatField()
    is_on_sale = models.BooleanField(default=False)
    discount = models.IntegerField(blank=True, null=True)
    prise_with_discount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_computed(self):
        result = self.price - self.price / 100 * self.discount
        return result

    def save(self, *args, **kwargs):
        if self.is_on_sale:
            self.prise_with_discount = self.get_computed()
        super(services, self).save(*args, **kwargs)


class item(models.Model):
    title = models.TextField(unique=True)
    description = models.TextField()
    price = models.FloatField()
    is_on_sale = models.BooleanField(default=False)
    discount = models.IntegerField(blank=True, null=True)
    prise_with_discount = models.IntegerField(blank=True, null=True)
    haract = models.TextField(blank=True, null=True)
    M3_Lee_garant= models.IntegerField(default=12)
    storage_status = models.BooleanField()
    type10MBT = models.TextField()
    min_range = models.IntegerField()
    max_range = models.IntegerField()
    Sampling_method = models.TextField(blank=True, null=True)
    Measured_gases = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_computed(self):
        result = self.price - self.price / 100 * self.discount
        return result

    def save(self, *args, **kwargs):
        if self.is_on_sale:
            self.prise_with_discount = self.get_computed()
        super(item, self).save(*args, **kwargs)