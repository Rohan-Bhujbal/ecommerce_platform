import os
import uuid
import boto3
from PIL import Image, ImageOps
from django.conf import settings
from botocore.client import Config
from file.models import UserFile
from django.forms.models import model_to_dict
from django.http import FileResponse, JsonResponse
from file.s3 import s3_file_upload, s3_thumbnail_upload
from app.globals import (
    VAR_350,
    VAR_FILES,         
    VAR_THUMBNAIL,
    IMAGE_EXTENSION_LIST
    )


def file_upload(file, extension):
    s3_thumb_350 = False
    is_s3_upload = True if settings.USE_S3 == True else False
    user_uploads = settings.MEDIA_ROOT + '/'+ VAR_FILES
    path = os.path.exists(user_uploads)
    if not path:
        os.makedirs(user_uploads)
    
    file_id = str(uuid.uuid4())
    object_name = file_id + extension
    file_path = os.path.join(user_uploads, object_name)    
    destination = open(file_path, 'wb+')

    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()
    if is_s3_upload:
        s3_url = s3_file_upload(file_path, "", object_name)
    else:
        s3_url = None
    s3_urlb =True if s3_url else False
    s3_thumb_350 = False
    thumbnail_uploads = settings.MEDIA_ROOT + '/'+settings.THUMBNAILS_URL
    ietf = os.path.exists(thumbnail_uploads)
    if not ietf:
        os.makedirs(thumbnail_uploads)

    if extension in IMAGE_EXTENSION_LIST :
        image_thumbnail(file_path, thumbnail_uploads, object_name)
        if is_s3_upload:
            s3_350_upload = s3_thumbnail_upload((thumbnail_uploads+'/'+ VAR_350+'/'+object_name), "", object_name, False, VAR_350)
        else:
            s3_350_upload = None
        
        if s3_350_upload :
            s3_thumb_350 = True

    size = os.path.getsize(file_path)
    
    if is_s3_upload:
        if s3_urlb:
            if os.path.exists(file_path):
                os.remove(file_path)
        if s3_thumb_350:
            if os.path.exists((thumbnail_uploads+'/'+ VAR_350+'/'+object_name)):
                    os.remove((thumbnail_uploads+'/'+ VAR_350+'/'+object_name))

    data = {
            'name': object_name,
            'size': size,
            'id': file_id,
            's3_url': s3_urlb,
            's3_thumb_350' : s3_thumb_350,
        }
    return data


def image_thumbnail(file_path, thumbnail_uploads, object_name):
    try:
        original_image = Image.open(file_path)
        image = ImageOps.exif_transpose(original_image)
        ele =eval(settings.LIST_SIZE)
        image.thumbnail((ele[0], ele[1]))
        path_350 = os.path.exists(thumbnail_uploads+'/'+ VAR_350)
        if not path_350:
            os.makedirs(thumbnail_uploads+'/'+ VAR_350)
        image.save(thumbnail_uploads+'/'+ VAR_350+'/'+object_name)
    except Exception as e:
        print(e)


def get_s3_file_url(user_id, object_name, profile_flag=False):
    if profile_flag == True:
        return settings.MEDIA_URL_S3+settings.S3_AVATARS_URL+'/'+ user_id_encryption(user_id) +'/'+object_name
    else:
        return settings.MEDIA_URL_S3 + settings.FILES_URL+'/'+object_name


def get_s3_thumb_url(user_id, object_name, profile_flag=False):
    if profile_flag == True:
        return settings.MEDIA_URL_S3+settings.S3_AVATARS_URL+'/'+ user_id_encryption(user_id)+'/'+ VAR_350 +'/'+object_name
    else:
        return settings.MEDIA_URL_S3 + settings.THUMBNAILS_URL+'/' + VAR_350+ '/'+object_name


def get_file_details(id):
    user_file_dict = {}
    try:
        user_file = UserFile.objects.get(id=uuid.UUID(id).hex)
        if user_file.deleted_at is None :
            user_file_dict = model_to_dict(user_file)
            user_file_dict['id'] = str(user_file.id)
            user_file_dict['file_name'] = user_file.name
            user_file_dict['view_file_url'] = f"view/<str:file>/<str:{user_file.id}>"
            user_file_dict['view_thumbnail_url'] = f"view/<str:thumbnail>/<str:{user_file.id}>"
            del user_file_dict['user_id']
            del user_file_dict['deleted_at']

    except UserFile.DoesNotExist:
        user_file_dict = {}
    return user_file_dict


def check_file(id):
    try:
        if id:
            user_file = UserFile.objects.filter(id=uuid.UUID(id).hex, deleted_at__isnull=True).first()
            return user_file
    except Exception:
        return None


def is_valid_file(id):
    return UserFile.objects.filter(id=uuid.UUID(id).hex).exists()


def user_id_encryption(user_id):
    output2 = ""
    output1 = ""
    output = ""
    user_id_list = str(user_id).split("-")
    for x in user_id_list:
        output1 = output1 + x[::2]
        output2 = output2 + x[1::2]
    output = output1[1::2] + output2[1::2] + output1[::2] + output2[::2]
    return output


def download_s3_file(file):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    s3 = boto3.resource(
        's3',
        aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
        config=Config(signature_version='s3v4')
    )
    path = settings.MEDIA_ROOT+'/'+settings.DOWNLOAD_URL
    is_exist = os.path.exists(path)
    if not is_exist:
        os.makedirs(path)
    filepath = path+'/'+file.split('/')[-1]
    s3.Bucket(bucket_name).download_file(file[1:], filepath)
    return filepath


def save_file(file):
    try:
        filepath = download_s3_file(file)
        res = FileResponse(open(filepath, 'rb'))
        os.remove(filepath)
        return res
    except Exception as e:
        res = {"error" : repr(e)}
        return JsonResponse(res, status=400)


def view_local_file(type, file_name):
    res = False
    file_path = ""
    if type == VAR_THUMBNAIL:
        thumbnail_uploads = settings.MEDIA_ROOT + '/'+ settings.THUMBNAILS_URL
        path = os.path.exists(thumbnail_uploads)
        if not path:
            os.makedirs(thumbnail_uploads)
        file_uploads = thumbnail_uploads + '/' + VAR_350 + '/'+ file_name
        file_uploads_path = os.path.exists(file_uploads)
        if file_uploads_path:
            file_path = file_uploads
    else:
        user_uploads = settings.MEDIA_ROOT + '/'+ VAR_FILES
        path = os.path.exists(user_uploads)
        if not path:
            os.makedirs(user_uploads)
        file_uploads = user_uploads + '/' + file_name
        file_uploads_path = os.path.exists(file_uploads)
        if file_uploads_path:
            file_path = file_uploads
    res = FileResponse(open(file_path, 'rb'))
    return res