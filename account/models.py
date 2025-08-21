from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
ROLE_CHOICES=[
('Admin','Admin'),
  ('Manager','Manager'),
  ('Cashier','Cashier'),
  ('waiter','Waiter'),

  
]


role=models.CharDField(max_length=20,choices=ROLE_CHOICES,default='Waiter')
def__str__(self):
return f"{self.username}({self.role})"
# Create your models here.

