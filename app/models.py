from django.db import models

# Create your models here.
class Accounts(models.Model):
    name= models.CharField(max_length=32)
    DOB= models.DateField()
    Aadhar= models.CharField(max_length=12)
    pan=models.CharField(max_length=10)
    mobile=models.IntegerField()
    address=models.TextField()
    acc= models.BigAutoField(primary_key=True)
    bal=models.DecimalField(max_digits=7, decimal_places=2, default=1000.0)
    pin=models.IntegerField(default=0)
    email=models.EmailField(default="dhanushaerolla02@gmail.com")  
    otp=models.IntegerField(default=0)