from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from post.models import Annonce
from .forms import SearchForm

@method_decorator(login_required, name='dispatch')
class IndexView(ListView, FormView):
    model = Annonce
    template_name = 'search/index.html'
    paginate_by = 20
    form_class = SearchForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = form_class(data={
            'zone': self.request.GET.get('zone', ''),
            'duree': self.request.GET.get('duree', ''),
            'domain': self.request.GET.getlist('domain', ''),
            'type_de_contrat': self.request.GET.get('type_de_contrat', ''),
            'nom_entreprise': self.request.GET.get('nom_entreprise', ''),
        })
        return form

    def get_queryset(self):
        form = self.get_form()
        return form.build_queryset()
    
@method_decorator(login_required, name='dispatch')
class DetailView(DetailView):
    model = Annonce
    template_name = 'search/detail.html'

    def get_object(self):
        # Call the superclass
        object = super(DetailView, self).get_object()
        # Record the last accessed date
        object.visites += 1
        object.save()
        # Return the object
        return object

