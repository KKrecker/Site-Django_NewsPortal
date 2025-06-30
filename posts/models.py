from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.title} ({self.id})"

class News(Post):
    pass

class Advertisement(Post):
    description = models.TextField(null=True, blank=True)


class Offer(Post):
    email = models.EmailField(blank= True, null= True)
    phone = PhoneNumberField(blank= True, null= True,region = 'RU')
