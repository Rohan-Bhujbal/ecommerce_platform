import os
import boto3
import requests
from django.conf import settings
from app.globals import VAR_MEDIA
from botocore.client import Config
from django.http import FileResponse


def s3_file_upload(file_path, user_eid, object_name, profile_flag=False):
    url = ""
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    file_name = os.path.join(
            file_path
        )

    data = open(file_name, 'rb')
    s3 = boto3.resource(
        's3',
        aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
        config=Config(signature_version='s3v4')
    )
    if profile_flag == True :
        url = s3.Bucket(bucket_name).put_object(Key= VAR_MEDIA +"/" + settings.AVATARS_URL+f"/{user_eid}/" + object_name, Body=data, ACL='public-read')
    else:
        url = s3.Bucket(bucket_name).put_object(Key= VAR_MEDIA +"/" + settings.FILES_URL +"/" + object_name, Body=data, ACL='public-read')
    return url


def s3_thumbnail_upload(thumbnail_file_path, user_eid, object_name, profile_flag, size):
    url = ""
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    file_name = os.path.join(
            thumbnail_file_path
        )

    data = open(file_name, 'rb')

    s3 = boto3.resource(
        's3',
        aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
        config=Config(signature_version='s3v4')
    )
    if profile_flag == True :
        url = s3.Bucket(bucket_name).put_object(Key= VAR_MEDIA +"/" + settings.AVATARS_URL+f"/{user_eid}/" + size+ "/" +object_name, Body=data, ACL='public-read')
    else:
        url = s3.Bucket(bucket_name).put_object(Key= VAR_MEDIA +"/" + settings.THUMBNAILS_URL +"/" + size+ "/" + object_name, Body=data, ACL='public-read')
    return url


def s3_file_download(file_url, filename):
    res = ""
    filepath = os.path.join(settings.MEDIA_ROOT +"/" + settings.FILES_URL+'/'+ filename)
    response = requests.get(file_url)
    if response:
        open(filepath, "wb").write(response.content)
        res = FileResponse(open(filepath, 'rb'))
        os.remove(filepath)
    return res