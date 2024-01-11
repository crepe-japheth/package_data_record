from django.db import models

from django.contrib.auth.models import User



class LocalPackage(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField(max_length=200)
    sender_address = models.CharField(max_length=200)
    sender_phone_number = models.CharField(max_length=200)
    recipient_name = models.CharField(max_length=200)
    recipient_email = models.EmailField(max_length=200)
    recipient_address = models.CharField(max_length=200)
    recipient_phone_number = models.CharField(max_length=200)
    package_type = models.CharField(max_length=200)
    package_destination = models.CharField(max_length=200)
    package_weight = models.DecimalField(max_digits=5, decimal_places=2)
    tracking_number = models.CharField(max_length=100, unique=True)
    branch = models.CharField(max_length=200)
    received_date = models.DateTimeField(auto_now_add=True)
    is_exception = models.CharField(max_length=50, choices=[
        ('regular', 'regular'),
        ('exception', 'exception'),
    ])
    content = models.TextField(blank=True, null=True)
    
    @property
    def package_price(self):
        price = self.package_weight
        return price
    
    class Meta:
        ordering = ['-received_date']

    def __str__(self):
        return self.tracking_number


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return self.user.username




