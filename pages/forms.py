from django import forms
from django.core.mail import EmailMessage

class ContactForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        mail = EmailMessage(
            subject = "[Stages] Un utilisateur requiert votre attention",
            body = self.cleaned_data['message'],
            from_email = self.cleaned_data['email'],
            reply_to = [self.cleaned_data['email']],
            to = ["stages-admin@resel.fr"],
        )
        mail.send()