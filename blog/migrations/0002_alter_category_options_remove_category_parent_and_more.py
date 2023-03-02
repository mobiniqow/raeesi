# Generated by Django 4.1.7 on 2023-03-01 09:15

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته اصلی', 'verbose_name_plural': 'دسته های اصلی'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=33)),
                ('created_at', django_jalali.db.models.jDateField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
            options={
                'verbose_name': 'دسته فرعی',
                'verbose_name_plural': 'دسته های فرعی',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.subcategory'),
        ),
    ]