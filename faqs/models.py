from django.db import models


class FAQ(models.Model):
    """ FAQs model. """
    question = models.CharField(max_length=250, null=False, blank=False)
    answer = models.TextField(null=False, blank=False)
    link_text = models.CharField(max_length=100, null=True, blank=True)
    link_url = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "FAQs"
        ordering = ["id", ]

    def __str__(self):
        return self.question
