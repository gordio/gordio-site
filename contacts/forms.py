from django import forms
from django.conf import settings
from django.core.mail import send_mail as django_send_mail
from django.utils.translation import ugettext_lazy as _
from captcha.fields import CaptchaField


class ContactsForm(forms.Form):
    email = forms.CharField(label=_("You email"), max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter you contact Email'}))
    content = forms.CharField(label=_("You message"), max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Enter you message'}))
    captcha = CaptchaField()

    def send_mail(self):
        return django_send_mail(
            _("{0} New message from site".format(settings.EMAIL_PREFIX)),
            self.cleaned_data['content'],
            self.cleaned_data['email'],
            [manager[1] for manager in settings.MANAGERS]
        )
