from django.db import models


# Create your models here.
class User(models.Model):
    USER_CHOICES=[
            ('GUARD', 'GUARD'),
            ('INSTRUCTOR', 'INSTRUCTOR'),
            ('ADMIN', 'ADMIN')
        ]
    employee_id = models.CharField(max_length=20, unique=True)
    employee_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    position = models.CharField(max_length=10, choices=USER_CHOICES)
        

    def __str__(self):
        return self.employee_name