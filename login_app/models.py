from django.db import models

class UserLogin(models.Model):
    email_or_phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  # Storing plain text

    def __str__(self):
        return self.email_or_phone
