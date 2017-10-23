from django.conf import settings
from django.contrib.auth.models import User

from ldap3 import Server, Connection

class ReselAdminMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.is_superuser:
            ldap = Connection(
                Server(host=settings.LDAP_URL, port=int(settings.LDAP_PORT)),
                auto_bind=True
            )
            if ldap.search(setings.LDAP_ADMIN_OU, "(&(uid={}))".format(request.user.uid)):
                user = User.objects.get(uid=request.user.uid)
                user.is_admin = True
                user.is_staff = True
                user.is_superuser = True
                user.save()
            ldap.unbind()

        response = self.get_response(request)
        return response