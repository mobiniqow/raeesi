from django.db import models


class Banners(models.Model):
    class State(models.IntegerChoices):
        TOP_BANNER = 0
        SIDE_BANNER = 1

    name = models.CharField(max_length=30)
    url = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='images/banner')
    state = models.IntegerField(choices=State.choices, default=State.TOP_BANNER)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنرها'
