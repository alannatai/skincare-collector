from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

STATUS = (
  ('0', 'No change'), 
  ('10', 'Great!'), 
  ('STR', 'Start product'), 
  ('FIN', 'Finish product'), 
  ('OIL', 'Oily'), 
  ('DRY', 'Dry'), 
  ('NOR', 'Normal'), 
  ('HY', 'Hydrated'), 
  ('DHY', 'Dehydrated'),
  ('ACB', 'Breakout'),
  ('ACR', 'Acne reduced'), 
  ('PC', 'Clogged pores'),
  ('PR', 'Reduced pores'), 
  ('B', 'Bright'), 
  ('D', 'Dull'), 
  ('RD', 'Redness'),
  ('WR', 'Wrinkles reduced')
  )

class Ingredient(models.Model):
  name = models.CharField(max_length=50)
  details = models.TextField(max_length=500, default='No description')

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('ingredients_detail', kwargs={'pk': self.id})

class Skincare(models.Model):
  name = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  rating = models.DecimalField(max_digits=2, decimal_places=1)
  buy_again = models.CharField(max_length=10)
  pros = models.TextField(max_length=255)
  cons = models.TextField(max_length=255)
  ingredients = models.ManyToManyField(Ingredient)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={ 'product_id': self.id })

class Progress(models.Model):
  date = models.DateField('Skin Status Date')
  status = models.CharField(
    max_length=4,
    choices=STATUS,
    default=STATUS[0][0]
  )
  skincare = models.ForeignKey(Skincare, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_status_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  skincare = models.ForeignKey(Skincare, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for skincare_id: {self.skincare_id} @{self.url}"