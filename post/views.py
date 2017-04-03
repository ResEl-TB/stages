from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.contrib import messages

from post.forms import AnnonceForm
from post.models import Annonce

@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required, name='dispatch')
class AnnonceCreate(CreateView):
    model = Annonce
    template_name = 'post/creation.html'
    form_class = AnnonceForm
    success_url = '/post/'

    def form_valid(self, form):
        response = super(AnnonceCreate, self).form_valid(form)
        messages.success(self.request, "L'annonce a bien été créée.")
        return response