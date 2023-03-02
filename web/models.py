from django.db import models


class Banners(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='images/banner')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنرها'
