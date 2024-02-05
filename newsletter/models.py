from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(max_length=256, null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    

    def __str__(self):
        return self.email
