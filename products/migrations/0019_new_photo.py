# Generated by Django 4.0.5 on 2022-09-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
