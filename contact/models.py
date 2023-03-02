from django.core.exceptions import ValidationError
from django.db import models
from django_jalali.db import models as jmodels
from ckeditor_uploader.fields import RichTextUploadingField


class Settings(models.Model):
    twitter = models.CharField(max_length=30)
    instagram = models.CharField(max_length=30)
    telegram = models.CharField(max_length=30)
    whatsapp = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=30)
    facebook = models.CharField(max_length=30)
    created_at = jmodels.jDateField(auto_now_add=True)
    updated_at = jmodels.jDateField(auto_now=True)
    about_use = RichTextUploadingField()

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات کلی'

    def save(self, *args, **kwargs):
        if not self.pk and Settings.objects.exists():
            raise ValidationError('There is can be only one JuicerBaseSettings instance')
        return super(Settings, self).save(*args, **kwargs)

    def __str__(self):
        return self.instagram


class Part(models.Model):
    name = models.CharField(max_length=44)
    address = models.CharField(max_length=44)
    created_at = jmodels.jDateField(auto_now_add=True)
    updated_at = jmodels.jDateField(auto_now=True)

    class Meta:
        verbose_name = 'بخش'
        verbose_name_plural = 'بخش ها'

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    class State(models.IntegerChoices):
        UNREAD = 0
        READ = 1

    name = models.CharField(max_length=30)
    email = models.EmailField()
    content = models.TextField()
    state = models.IntegerField(choices=State.choices, default=State.UNREAD)

    def __str__(self):
        return self.name
