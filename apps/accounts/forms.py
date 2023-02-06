from django import forms

from apps.authentication.models import CustomUser


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'birthday', 'gender', 'email', 'phone', 'address', 'number', 'city', 'country',
            'zipcode')
