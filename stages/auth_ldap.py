#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django_auth_ldap.backend import LDAPBackend
from django.contrib.auth import get_user_model

class LDAPBackendAdmin(LDAPBackend):
    settings_prefix = "AUTH_LDAP_ADMIN_"

    def authenticate(self, username, password):
    	user = LDAPBackend.authenticate(self, username, password)
    	if user:
    	    user.is_staff = True
            user.is_superuser = True
	    user.save()
    	return user

    def get_or_create_user(self, username, ldap_user):
        kwargs = {
            'username': username,
            'defaults': {'is_superuser': True, 'is_staff': True}
        }
        user_model = get_user_model()
        return user_model.objects.get_or_create(**kwargs)

class LDAPBackendUsers(LDAPBackend):
    settings_prefix = "AUTH_LDAP_USERS_"
