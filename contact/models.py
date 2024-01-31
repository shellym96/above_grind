from django.db import models

class Contact(models.Model):
    """ Contact form model """
    CONTACT_CHOICES = [
        ('general', 'General Enquiry'),
        ('order', 'Order Enquiry '),
        ('return', 'Return Request'),
        ('complaint', 'Complaint'),
    ]
    subject = models.CharField(max_length=150)
    reason = models.CharField(max_length=45, choices=CONTACT_CHOICES)
    message = models.TextField(max_length=800)
    email = models.EmailField()

    def __str__(self):
        return self.email
