from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from shops.models import ShopsData


def upload_location(instance, filename, **kwargs):
    file_path = "items/{item_from_shop}/{item_name}-{filename}".format(
        item_from_shop=str(instance.item_from_shop.shop_name), item_name=str(instance.item_name), filename=filename
    )
    return file_path


class ItemModel(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50, null=False, blank=False)
    item_description = models.TextField(max_length=5000, null=False, blank=False)
    item_regular_price = models.IntegerField(null=False, blank=False)
    item_quantity = models.IntegerField(default=0, null=False, blank=False)
    item_discounted_price = models.IntegerField(null=False, blank=False)
    item_image1 = models.ImageField(upload_to=upload_location, null=False, blank=False)
    item_image2 = models.ImageField(upload_to=upload_location, null=False, blank=False)
    item_image3 = models.ImageField(upload_to=upload_location, null=False, blank=False)
    item_created = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    item_updated = models.DateTimeField(auto_now_add=True, verbose_name="date updated")
    item_from_shop = models.ForeignKey(ShopsData, on_delete=models.CASCADE)
    item_slug = models.SlugField(blank=True, unique=True)

    class Meta:
        verbose_name_plural = "Items"

    def __str__(self):
        return self.item_name


@receiver(post_delete, sender=ItemModel)
def submission_delete(sender, instance, **kwargs):
    instance.item_image1.delete(False)
    instance.item_image2.delete(False)
    instance.item_image3.delete(False)


def pre_save_item_data_receiver(sender, instance, *args, **kwargs):
    if not instance.item_slug:
        instance.item_slug = slugify(instance.item_from_shop.shop_name + " " + instance.item_name)


pre_save.connect(pre_save_item_data_receiver, sender=ItemModel)
