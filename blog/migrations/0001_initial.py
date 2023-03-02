# Generated by Django 4.1.7 on 2023-03-01 07:59

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=33)),
                ('created_at', django_jalali.db.models.jDateField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
            options={
                'verbose_name': 'دسته',
                'verbose_name_plural': 'دسته ها',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(0, 'Unread'), (1, 'Read'), (2, 'Mark')], default=0)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('created_at', django_jalali.db.models.jDateField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'نظر خبر',
                'verbose_name_plural': 'نظرهای خبر',
            },
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=33)),
                ('created_at', django_jalali.db.models.jDateField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'برچسب',
                'verbose_name_plural': 'برچسب ها',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', ckeditor.fields.RichTextField()),
                ('created_at', django_jalali.db.models.jDateField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateField(auto_now=True)),
                ('picture', models.ImageField(upload_to='upload')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
            options={
                'verbose_name': 'خبر',
                'verbose_name_plural': 'خبرها',
            },
        ),
        migrations.CreateModel(
            name='HashtagNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateField(auto_now=True)),
                ('hashtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.hashtag')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
            options={
                'verbose_name': 'برچسب پست',
                'verbose_name_plural': 'برچسب های پست',
            },
        ),
    ]