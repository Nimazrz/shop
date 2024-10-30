from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.name


class Sort(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def get_absolute_url(self):
        return reverse('shop:product_list_by_sort', kwargs={'sort_slug': self.slug})

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='دسته بندی')
    name = models.CharField(max_length=255, verbose_name='نام ')
    slug = models.SlugField(max_length=255, verbose_name='اسلاگ')
    description = models.TextField(max_length=1200, verbose_name='توضیحات')
    inventory = models.PositiveIntegerField(default=0, verbose_name='موجودی')
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت')
    weight = models.PositiveIntegerField(default=0, verbose_name='وزن')
    off = models.PositiveIntegerField(default=0, verbose_name='تخفیف')
    new_price = models.PositiveIntegerField(default=0, verbose_name='قیمت پس از تخفیف')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'id': self.id, 'slug': self.slug})

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name='محصول')
    image_file = models.ImageField(upload_to='product_images/%Y/%m/%d',
                                   max_length=500)  #<<upload_to_author_directory>> this function imported from others.py file
    title = models.CharField(max_length=200, verbose_name='عنوان', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]


class ProductFeature(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام ویژگی')
    value = models.CharField(max_length=255, verbose_name='مقدار ویژگی')
    product = models.ForeignKey(Product, related_name='features', on_delete=models.CASCADE, verbose_name='محصول ها')

    def __str__(self):
        return self.name + ':' + self.value
