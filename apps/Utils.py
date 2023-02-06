import os

from storages.backends.ftp import FTPStorage

from apps.authentication.models import CustomUser as User
from core import settings


def username_exists(username):
    user_query = User.objects.filter(username=username)
    if user_query.exists():
        return user_query.first()

    return False


def email_exists(email):
    user_query = User.objects.filter(email=email)

    if user_query.exists():
        return user_query.first()

    return False


def delete_user(to_delete_user_username):
    user = User.objects.filter(username=to_delete_user_username)
    if user.count() == 0:
        return False, 'User not found.'
    if user.last().is_superuser:
        return False, 'Cannot delete superuser.'
    try:
        user.delete()
    except Exception as e:
        return False, str(e)
    return True, f'{to_delete_user_username} deleted successfully.'


def upload(username, image):
    file_obj = image

    # do your validation here e.g. file size/type check

    # organize a path for the file in bucket
    file_directory_within_bucket = f'{username}'

    # synthesize a full file path; note that we included the filename
    file_path_within_bucket = os.path.join(
        file_directory_within_bucket,
        file_obj.name
    )

    media_storage = FTPStorage()

    if not media_storage.exists(file_path_within_bucket):  # avoid overwriting existing file
        media_storage.save(file_path_within_bucket, file_obj)

    return media_storage.url(file_path_within_bucket)


def cfg_val(aVarName):
    return getattr(settings, aVarName, None)


def cfg_FTP_UPLOAD():
    return cfg_val("FTP_UPLOAD")
