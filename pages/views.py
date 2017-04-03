from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from pages.forms import ContactForm

@method_decorator(login_required, name='dispatch')
class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Votre mail a bien été envoyé.')
        return super(ContactView, self).form_valid(form)