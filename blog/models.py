from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class reviews(models.Model):
    """ Review blog for products reviews """

    review = models.CharField(blank=True, null=True, max_length=100)
    title = models.CharField(max_length=130, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews',)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = models.ImageField(blank=True, upload_to='blogimages')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title