from pydoc import ModuleScanner
from django.db import models
from django.utils import timezone


class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime()}"
