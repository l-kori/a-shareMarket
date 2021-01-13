from django.db import models

class allstock_a(models.Model):
    stock_id = models.CharField(max_length=10,null=False)