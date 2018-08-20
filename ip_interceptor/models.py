from django.db import models


class ForbiddenIP(models.Model):
    ip = models.CharField(max_length=18)
    reason = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = verbose_name_plural = 'forbidden_ip'

    def __str__(self):
        return f'ForbiddenIP:{self.ip}'
