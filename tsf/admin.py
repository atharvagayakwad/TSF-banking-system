from django.contrib import admin
from tsf.models import TransactionDetailModel, CustomerDetailModel


# Register your models here.
admin.site.register(TransactionDetailModel)
admin.site.register(CustomerDetailModel)