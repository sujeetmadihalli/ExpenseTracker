from django.db import models

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)  # Automatically set the date when an expense is created

    def __str__(self):
        return f'{self.category}: {self.amount} on {self.date}'
