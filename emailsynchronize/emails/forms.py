# coding: utf8
import re

from django import forms
from emails.constants import DOMAINS
from emails.models import LogPass


class LogPassForm(forms.ModelForm):
    """
    Simple form for work with emails
    """
    class Meta:
        model = LogPass
        widgets = {
            'portal_password': forms.PasswordInput(),
        }
        fields = ('user_email', 'portal_password')

    def clean_user_email(self):
        """
        Validate user's email
        """
        user_email = self.cleaned_data.get('user_email', False)
        domaine = user_email.split('@')[1]
        if domaine not in DOMAINS:
            raise forms.ValidationError(
                'Введите свою рабочую почту '
                f'{DOMAINS}. '
                f'Почта с доменом {domaine} не подходит.'
                )
        return user_email

    def clean_portal_password(self):
        portal_password = self.cleaned_data.get('portal_password', False)
        if re.search('[а-яА-Я]', portal_password):
            raise forms.ValidationError('Пароль не может содержать русских '
                                        'букв! Смените раскладку.')
        return portal_password
