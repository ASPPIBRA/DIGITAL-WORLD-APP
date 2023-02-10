import os
from http import HTTPStatus

from django.http import JsonResponse
from django.shortcuts import render

from apps import Utils
from apps.Utils import cfg_FTP_UPLOAD
from apps.accounts.forms import EditProfileForm


def edit_profile(request):
    if request.method == 'GET':
        return render(request, 'home/dashboard-settings.html')
    form = EditProfileForm(request.POST, instance=request.user)
    if not form.is_valid():
        return JsonResponse({
            'errors': form.errors
        }, status=HTTPStatus.BAD_REQUEST)
    form.save()
    return JsonResponse({}, status=HTTPStatus.OK)


def upload_avatar(request):
    if not cfg_FTP_UPLOAD():
        return JsonResponse({
            'errors': 'Please check app settings (IMG storage).'
        }, status=400)

    image = request.FILES.get('avatar', None)
    if image:

        try:
            avatar_url = Utils.upload(request.user.username, image)
            request.user.image = os.getenv("upload_url", '') + '/'.join(avatar_url.split("/")[-2:])
            request.user.save()
        except Exception as e:
            print(str(e))
            print("There is a problem in connection with FTP")
            return JsonResponse({
                'errors': 'There is a problem in connection with FTP'
            }, status=HTTPStatus.INTERNAL_SERVER_ERROR)

    return JsonResponse({}, status=HTTPStatus.OK)
