from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_likes(models.Model):
    user_id = models.IntegerField("user_id")
    card_id = models.IntegerField("card_id")

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"


class Card(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField("Title",max_length=50)
    img_url = models.TextField("Img_url")
    price = models.IntegerField("Price",max_length=1000)
    description = models.TextField("Description")

    def __str__(self):
        return self.title + '\n' + self.price
    
    def get_absolute_url(self):
        return "/"

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"