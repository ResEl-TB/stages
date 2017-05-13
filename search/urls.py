from django.conf.urls import url

from .views import IndexView, DetailView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^announce/(?P<pk>[0-9]+)$', DetailView.as_view(), name='detail'),
]