from django.db import models

# class Skincare:
#     def __init__(self, name, price, star_ingredients, rating, buy_again, pros, cons):
#         self.name = name
#         self.price = price
#         self.star_ingredients = star_ingredients
#         self.rating = rating
#         self.buy_again = buy_again
#         self.pros = pros
#         self.cons = cons

class Skincare(models.Model):
  name = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  star_ingredients = models.TextField(max_length=250)
  rating = models.DecimalField(max_digits=2, decimal_places=1)
  buy_again = models.CharField(max_length=10)
  pros = models.TextField(max_length=250)
  cons = models.TextField(max_length=250)

  def __str__(self):
    return self.name