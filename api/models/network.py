from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Network(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.2/ref/models/fields/
  address = models.CharField(max_length=100)
  subnet = models.IntegerField()
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The network is {self.address}/{self.subnet}."

