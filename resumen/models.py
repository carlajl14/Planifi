from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Resumen(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # Ingresos mensuales
    monthly_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # Gastos mensuales
    budget_utilization = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # Utilizacion del presupuesto

    def __str__(self):
        return f'{self.user_id.username}'