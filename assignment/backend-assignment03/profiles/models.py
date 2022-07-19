from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    age = models.IntegerField(blank=True)
    phone = models.CharField(max_length=20, null=False, blank=False)


class url(models.Model):
    profile=models.ForeignKey('Profile',on_delete=models.CASCADE, null=True, blank=True)
    content=models.CharField(max_length=20, null=True, blank=True)
    link = models.URLField(max_length=500)
    pup_date=models.DateTimeField(auto_now_add=True)

    # auto_now=변경될때 마다 나옴.