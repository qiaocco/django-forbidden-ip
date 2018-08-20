django-forbidden-ip
---

This is a django application to forbid access by IP address.

Install
===

    pip install django-forbidden-ip
    
Config
===

1. Add `ip_interceptor` to `INSTALLED_APPS`.
2. Add `ip_interceptor.middleware.IPInterceptorMiddleware` to `MIDDLEWARE`.
3. Run `./manage.py makemigrations ip_interceptor` and `./manage.py migrate ip_interceptor`.
4. Add IP you want to block to `ForbiddenIP`.
