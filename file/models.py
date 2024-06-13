import uuid
from django.db import models
from app.globals import TABLE_PREFIX


class UserFile(models.Model):
    class Meta():
        db_table = TABLE_PREFIX+'user_file'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_id = models.UUIDField(max_length=256, null=True)
    name = models.CharField(max_length=256, null=True)
    original_name = models.CharField(max_length=256, null=True)
    size = models.CharField(max_length=256, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    is_s3_url = models.BooleanField(default=False)
    is_350_thumb = models.BooleanField(default=False)
