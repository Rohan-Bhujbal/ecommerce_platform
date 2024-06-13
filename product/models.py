import uuid
from django.db import models
from app.globals import TABLE_PREFIX

# Create your models here.

class Product(models.Model):
    class Meta():
        db_table = TABLE_PREFIX+'product'
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    product_name = models.CharField(max_length=256, unique=True)
    short_description = models.CharField(max_length=256, null=True)
    product_image = models.CharField(max_length=256, null=True)
    mrp = models.CharField(max_length=256, null=True)
    is_active = models.BooleanField(default=True)
    author = models.UUIDField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)