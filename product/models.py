import socket
from io import BytesIO
from PIL import Image

from django.db import models
from django.utils.text import slugify
from django.core.files import File

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return self.name

    @property
    def absolute_url(self):
        return f'/{self.slug}/'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnail/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added',]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    @property
    def image_url(self):
        if self.image:
            domain = socket.gethostname()
            return domain + self.image.url
        return ''

    @property
    def thumbnail_url(self):
        domain = socket.gethostname()
        if self.thumbnail:
            return domain + self.thumbnail.url
        elif self.image:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()
            return domain + self.thumbnail.url
        return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

