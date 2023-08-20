from django.db import models

# Create your models here.


class Business(models.Model):
    email = models.CharField(max_length=100)
    key = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
class BusinessSummary(models.Model):
    business = models.ForeignKey(Business , on_delete=models.CASCADE)
    summary = models.TextField(max_length=100000)

class BusinessChatHistory(models.Model):
    business = models.ForeignKey(Business , on_delete=models.CASCADE)
    chat_history = models.JSONField(max_length=100000)

    def __str__(self):
        return self.business.email