from multiprocessing import context
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.http import HttpResponse
from django.shortcuts import redirect

# Access Mixin
class AccessMixin:

    login_url = None
    permission_denied_message = ''
    raise_exception = False
    redirect_field_name = REDIRECT_FIELD_NAME

    def get_login_url(self):

        login_url = self.login_url or settings.LOGIN_URL
        if not login_url:
            raise ImproperlyConfigured(
                '{0} is missing the login_url attribute. Define {0}.login_url, settings.LOGIN_URL, or override '
                '{0}.get_login_url().'.format(self.__class__.__name__)
            )
        return str(login_url)

    def get_permission_denied_message(self):

        return self.permission_denied_message

    def get_redirect_field_name(self):
        return self.redirect_field_name
    
    # def handle_no_permission(self):
    #     if self.raise_exception or self.request.user.is_authenticated:
    #         raise PermissionDenied(self.get_permission_denied_message())
    #     return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

class LoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        
        if  request.user.is_authenticated:
            if  request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
        
        return redirect('customadmin:custom-admin-login')