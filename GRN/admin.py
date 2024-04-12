from django.contrib import admin
from .models import GRN, purchase_orders
# Register your models here.
admin.site.register(GRN)
admin.site.register(purchase_orders)