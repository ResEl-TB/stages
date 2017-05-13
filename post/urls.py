from django.conf.urls import url
from .views import AnnonceCreate

urlpatterns = [
	url(r'^$', AnnonceCreate.as_view(), name='creation'),
]
