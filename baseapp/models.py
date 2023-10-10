from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True)
    registration_date = models.DateField(auto_now_add=True)


    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'


class Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profit_loss = models.DecimalField(decimal_places=2, max_digits=6)
    timespan = models.DurationField()
    trade_date = models.DateTimeField(auto_now_add=True)

    
    # trader_id = models.integerField()
    # profit_loss = random.uniform(-10, 10)
    # timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

