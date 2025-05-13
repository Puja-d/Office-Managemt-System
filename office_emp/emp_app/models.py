from django.core.validators import RegexValidator
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class office(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
class Department(models.Model):
      name=models.CharField(max_length=100,null=False)
      location=models.CharField(max_length=100)
      
      def __str__(self):
            return self.name
      
class Role(models.Model):
      name=models.CharField(max_length=100,null=False)
      
      def __str__(self):
            return self.name
class Employee(models.Model):
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonous=models.IntegerField(default=0)            
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?\d{10,15}$', message="Enter a valid phone number.")],
        null=False,
        blank=False
    )
    hire_date=models.DateField()
    
    
    def __str__(self):
          return '%s %s %s' %(self.first_name,self.last_name,self.phone)
