from django.db import models
from django.contrib.auth import get_user_model
from ExpenseIncomeTracker.settings import STATIC_URL

# Create your models here.
User = get_user_model()

TRANS_FIELD_CHOICES = [
    ('debit', 'Debit'),
    ('credit', 'Credit'),
]

TAX_FIELD_CHOICES = [
    ('flat', 'Flat'),
    ('percentage', 'Percentage'),
]


class ExpenseIncome(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    transaction_type=models.CharField(max_length=10,choices=TRANS_FIELD_CHOICES)
    tax = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    tax_type = models.CharField(max_length=10,choices=TAX_FIELD_CHOICES,default='flat')
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
    
    
    def calculate_total(self):
        if self.tax_type == 'flat':
            return self.amount + self.tax
        elif self.tax_type == 'percentage':
            return self.amount + (self.amount * self.tax / 100)
        return self.amount

    def save(self, *args, **kwargs):
        self.total = self.calculate_total()
        super().save(*args, **kwargs)
    
    