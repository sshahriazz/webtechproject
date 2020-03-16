from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver


def upload_location(instance, filename, **kwargs):
    file_path = "shop/{shop_owner_id}/{shop_name}-{filename}".format(
        shop_owner_id=str(instance.shop_owner.id), shop_name=str(instance.shop_name), filename=filename
    )
    return file_path


class ShopsData(models.Model):
    shop_name = models.CharField(max_length=50, null=False, blank=False)
    shop_description = models.TextField(max_length=5000, null=False, blank=False)
    shop_front_image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    shop_created = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    shop_updated = models.DateTimeField(auto_now_add=True, verbose_name="date updated")
    shop_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        verbose_name_plural = "Shops Data"

    def __str__(self):
        return self.shop_name


@receiver(post_delete, sender=ShopsData)
def submission_delete(sender, instance, **kwargs):
    instance.shop_front_image.delete(False)


def pre_save_shop_data_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.shop_owner.username + " " + instance.shop_name)


pre_save.connect(pre_save_shop_data_receiver, sender=ShopsData)
