# Generated by Django 3.1.6 on 2021-02-15 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210215_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
