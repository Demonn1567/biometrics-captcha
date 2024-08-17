from django.db import models

# Create your models here.
class UserBehavior(models.Model):
    user_id = models.CharField(max_length=100)
    behavior_data = models.JSONField()
    browser_info = models.JSONField(default=dict)  # Store browser info as JSON
    ip_address = models.GenericIPAddressField()  # Store IP address
    timestamp = models.DateTimeField(auto_now_add=True)