from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django_cas_ng import views as cas_views

from search.views import IndexView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name="home"),
	url(r'^login_local/$', auth_views.login, name="login_ldap"),
	url(r'^logout_local/$', auth_views.logout, name="logout_ldap"),
	url(r'^login$', cas_views.login, {'next_page': '/'}, name="login"),
    url(r'^logout$', cas_views.logout, name="logout"),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^post/', include('post.urls', namespace="post")),
	url(r'^search/', include('search.urls', namespace="search")),
]
