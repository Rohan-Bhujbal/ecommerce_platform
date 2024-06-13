import os
from django.conf import settings
from file.models import UserFile
from file.files import (
    file_upload,
)


def get_avatar_url(avatar):
    return settings.BASE_URL+settings.MEDIA_URL+settings.AVATARS_URL+'/'+avatar


def get_s3_avatar_url(user_eid,avatar):
    return settings.MEDIA_URL_S3+settings.S3_AVATARS_URL+'/'+user_eid+'/'+avatar


def valid_file_extension(filename):
    extension_str = ''
    extension_list4 = ['.png', '.jpg', '.pdf']
    extension_list5 = ['.jpeg']

    if filename[-4:].lower() in extension_list4:
        extension_str = filename[-4:].lower()
    if filename[-5:].lower() in extension_list5:
        extension_str = filename[-5:].lower()

    return extension_str

def valid_xlsx_extension(filename):
    extension_str = ''
    extension_list5 = ['.xlsx']
    if filename[-5:].lower() in extension_list5:
        extension_str = filename[-5:].lower()

    return extension_str

def file_helper_func(file, user_id):
    data = {}
    if valid_file_extension(str(file)):
        extension = os.path.splitext(str(file))[1].lower()
        data = file_upload(file, extension)
        if data:
            user_file = UserFile(
                id=data['id'], user_id=user_id, name=data['name'], size=data['size'], original_name=str(file), is_s3_url=data['s3_url'],
                is_350_thumb=data["s3_thumb_350"],
                )
            user_file.save()
            data['name']=str(file)
            data['view_file_url'] = f"view/file/{user_file.id}"
            data['view_thumbnail_url'] = f"view/thumbnail/{user_file.id}"
    else:
        data = {}
    return data
