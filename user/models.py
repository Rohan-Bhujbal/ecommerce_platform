import uuid
from django.db import models
from app.globals import TABLE_PREFIX


class User(models.Model):
    class Meta():
        db_table = TABLE_PREFIX+'users'

    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False, max_length=256
        )
    full_name = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=256, unique=True)
    mobile = models.CharField(max_length=256, unique=True)
    user_code = models.CharField(max_length=256, unique=True)
    address = models.CharField(max_length=1000, null=True)
    password = models.CharField(max_length=1000, null=True)
    permissions = models.CharField(max_length=2000, null=True)
    user_type = models.CharField(max_length=256, null=True)
    is_active = models.BooleanField(default=True)
    author = models.UUIDField(max_length=256, null=True)
    related_id = models.UUIDField(max_length=256, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class UserToken(models.Model):
    class Meta():
        db_table = TABLE_PREFIX+'user_tokens'

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_id = models.UUIDField(max_length=256, null=True)
    user_ip = models.CharField(max_length=256, null=True)
    fcm_token = models.CharField(max_length=256, null=True)
    user_agent = models.CharField(max_length=500, null=True)
    device_id = models.CharField(max_length=256, null=True)
    device_type = models.CharField(max_length=256, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserMagicCode(models.Model):
    class Meta():
        db_table = TABLE_PREFIX+'user_magic_code'

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_id = models.UUIDField(max_length=256, null=True)
    device_id = models.CharField(max_length=256, null=True)
    device_type = models.CharField(max_length=256, null=True)
    magic_code = models.CharField(max_length=256, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)