from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django_jalali.db import models as jmodels


class Category(models.Model):
    name = models.CharField(max_length=33)
    created_at = jmodels.jDateField(auto_now_add=True)
    updated_at = jmodels.jDateField(auto_now=True)

    class Meta:
        verbose_name = 'دسته اصلی'
        verbose_name_plural = 'دسته های اصلی'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=33)
    parent = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = jmodels.jDateField(auto_now_add=True)
    updated_at = jmodels.jDateField(auto_now=True)

    class Meta:
        verbose_name = 'دسته فرعی'
        verbose_name_plural = 'دسته های فرعی'

    def __str__(self):
        return self.name


class Post(models.Model):
    class Type(models.IntegerChoices):
        NORMAL = 0
        VIDEO = 1
        PICTURE = 2

    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    created_at = jmodels.jDateField(auto_now_add=True)
    updated_at = jmodels.jDateField(auto_now=True)
    picture = models.ImageField(upload_to='upload')
    views = models.IntegerField(default=0)
    state = models.IntegerField(choices=Type.choices, default=Type.NORMAL)

    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'خبرها'

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    name = models.CharField(max_length=33)
    created_at = jmodels.jDateField(auto_now_add=True)
    updated_at = jmodels.jDateField(auto_now=True)

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.name


class HashtagNew(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    created_at = jmodels.jDateField(auto_now_add=True)
    updated_at = jmodels.jDateField(auto_now=True)

    class Meta:
        verbose_name = 'برچسب پست'
        verbose_name_plural = 'برچسب های پست'

    def __str__(self):
        return self.post.title


class Comment(models.Model):
    class State(models.IntegerChoices):
        UNREAD = 0
        READ = 1
        # important message
        MARK = 2

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    state = models.IntegerField(choices=State.choices, default=State.UNREAD)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    content = models.TextField()
    created_at = jmodels.jDateField(auto_now_add=True)
    updated_at = jmodels.jDateField(auto_now=True)

    class Meta:
        verbose_name = 'نظر خبر'
        verbose_name_plural = 'نظرهای خبر'

    def __str__(self):
        return self.name
