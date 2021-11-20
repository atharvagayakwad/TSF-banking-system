from django.db import models

# Create your models here.
class TransactionDetailModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    debit_amount = models.IntegerField()
    credit_amount = models.IntegerField()
    account_balance = models.IntegerField()

    def __str__(self):
            return self.name

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

class CustomerDetailModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    available_balance = models.IntegerField()

    class Meta:
        verbose_name = 'Customer Detail'
        verbose_name_plural = 'Customer Details'

    def __str__(self):
        return self.name
