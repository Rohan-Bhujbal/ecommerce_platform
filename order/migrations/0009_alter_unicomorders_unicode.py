# Generated by Django 5.0 on 2024-05-10 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_order_unicode_unicomorders_shipping_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unicomorders',
            name='uniCode',
            field=models.CharField(max_length=256),
        ),
    ]
