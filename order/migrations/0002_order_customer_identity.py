# Generated by Django 5.0 on 2024-04-02 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_identity',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
