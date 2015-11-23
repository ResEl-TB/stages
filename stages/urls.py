#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from .views import ContactView
from search.views import IndexView
import post.urls as post_urls
import search.urls as search_urls

urlpatterns = [
	url(r'^$', IndexView.as_view(), name="home"),
	url(r'^login/$', auth_views.login, name="login"),
	url(r'^logout/$', auth_views.logout, name="logout"),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^contact', ContactView.as_view() , name="contact"),
    	url(r'^post/', include(post_urls, namespace="post")),
    	url(r'^search/', include(search_urls, namespace="search")),
]
