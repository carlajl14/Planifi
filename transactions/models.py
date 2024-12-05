from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self): 
        return self.name

class Transaction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    transaction_type = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user_id.username}'

class Budgets(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    period = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user_id.username}'

class Financial_goals(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    deadline = models.DateField()

    def __str__(self):
        return self.user_id.username

class Reports(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    report_name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=100)

    def __str__(self):
        return self.user_id.username