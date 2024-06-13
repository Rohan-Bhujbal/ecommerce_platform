import uuid
from django.db import models
from app.globals import TABLE_PREFIX

# Create your models here.


class Order(models.Model):
    class Meta():
        db_table = TABLE_PREFIX+'orders'
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False, max_length=256
        )
    total = models.CharField(max_length=256, null=True)
    qty = models.IntegerField(default=0)
    address = models.CharField(max_length=100,null=True)
    address3 = models.CharField(max_length=100,null=True)
    user_id = models.UUIDField(max_length=256,null=True)
    product_id = models.UUIDField(max_length=256,null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)