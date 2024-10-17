from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ShopUser


class ShopUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = ShopUser
        fields = ['phone', 'first_name', 'last_name', 'address', 'is_active', 'is_staff', 'is_superuser']



    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if self.instance.pk:
            if ShopUser.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('phone number is already in use.')
        else:
            if ShopUser.objects.filter(phone=phone) .exists():
                raise forms.ValidationError('phone number is already in use.')

        if not phone.isdigit():
            raise forms.ValidationError('phone number is invalid.')
        if not phone.startswith('09'):
            raise forms.ValidationError('phone number is invalid.')
        if len(phone) != 11:
            raise forms.ValidationError('phone number is invalid.')
        return phone


class ShopUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = ShopUser
        fields = ['phone', 'first_name', 'last_name', 'address', 'is_active', 'is_staff', 'is_superuser']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if self.instance.pk:
            if ShopUser.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('phone number is already in use.')
        else:
            if ShopUser.objects.filter(phone=phone) .exists():
                raise forms.ValidationError('phone number is already in use.')

        if not phone.isdigit():
            raise forms.ValidationError('phone number is invalid.')
        if not phone.startswith('09'):
            raise forms.ValidationError('phone number is invalid.')
        if len(phone) != 11:
            raise forms.ValidationError('phone number is invalid.')
        return phone

