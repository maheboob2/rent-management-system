from django.db import models
from django.db.models import DateField

# Create your models here.

class tenant(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15,default="")
    monthly_rent=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    join_date=models.DateField()
    is_active=models.BooleanField(default=True)

    def __str__(self):
       return self.name
     

class payment(models.Model):
    tenant=models.ForeignKey(tenant,on_delete=models.CASCADE,null=True)
    MONTH_CHOICES = [

    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
]



    month=models.CharField(max_length=20,choices=MONTH_CHOICES)
    amount=models.DecimalField(max_digits=10,decimal_places=2,default="")
    status=models.CharField(max_length=20,null=True,
                            choices=[
                                ('paid','paid'),
                                ('unpaid','unpaid'),
                                ('pending','pending')]
                                )
    

    paid_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.tenant.name}-{self.month}"
    
