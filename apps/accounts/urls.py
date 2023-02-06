from django.urls import path
from apps.accounts.views import edit_profile, upload_avatar

urlpatterns = [
    path('user_profile/', edit_profile, name='edit-profile'),
    path('upload_avatar/', upload_avatar, name='edit-avatar'),
]
