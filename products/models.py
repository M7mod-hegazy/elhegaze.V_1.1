from os import name
from django.db import models
from datetime import datetime
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=200, unique=True)
    price = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_active = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['publish_date']


class Child(models.Model):
    product = models.ForeignKey(
        Product, related_name='childs', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=19, decimal_places=2, blank=True, default=1)
    oldPrice = models.CharField(max_length=200, blank=True)
    details = models.TextField(max_length=1000, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',  blank=False)
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo5 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, null=True)

    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def save(self, *args, **kwargs):
        chi = self.id
        prod = self.product.id
        qrcode_img = qrcode.make(
            'http/elhegazy/' + str(prod) + '/info/' + str(chi))
        canvas = Image.new('RGB', (330, 330), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
        
       

    is_active = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ['-publish_date']


# Create your models here.
