from django.db import models

class Shares(models.Model):
    share_name = models.CharField(max_length=50)
    share_quantity = models.IntegerField(default=0)
    shares_owned = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    share_price = models.IntegerField(default=0)
    balance = models.IntegerField(default=10000)
    def __str__(self):
        return self.shares_text

