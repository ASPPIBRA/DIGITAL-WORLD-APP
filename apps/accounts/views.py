import os
from http import HTTPStatus
from django.http import JsonResponse
from django.shortcuts import render
from apps.accounts.forms import EditProfileForm


def edit_profile(request):
    if request.method == 'GET':
        return render(request, 'home/dashboard-settings.html')
    form = EditProfileForm(request.POST, instance=request.user)
    print(form.data)
    print(form.errors)
    if not form.is_valid():
        return JsonResponse({
            'errors': form.errors
        }, status=HTTPStatus.BAD_REQUEST)
    form.save()
    return JsonResponse({}, status=HTTPStatus.OK)

    
def upload_avatar(request):

    image = request.FILES.get('avatar', None)
    if image:

        try:
            old_image = ''
            if request.user.image:
                old_image = request.user.image.path

            request.user.image = image
            request.user.save()
            if old_image:
                if os.path.exists(old_image):
                    os.remove(old_image)
        except Exception as e:
            return JsonResponse({
                'errors': 'Erro ao carregar a immagen'
            }, status=HTTPStatus.INTERNAL_SERVER_ERROR)

    return JsonResponse({}, status=HTTPStatus.OK)
