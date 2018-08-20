from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

from .models import ForbiddenIP


class IPInterceptorMiddleware(MiddlewareMixin):
    def __init__(self, get_reqponse):
        self.get_response = get_reqponse

    def validate_ip(self, remote_ip):
        if ForbiddenIP.objects.filter(ip=remote_ip).count():
            return False
        return True

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if not self.validate_ip(ip):
            return HttpResponseForbidden('')
