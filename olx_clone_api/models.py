from django.db import models


class BikeModel(models.Model):
    name = models.CharField(max_length=250)
    post_date = models.DateField(auto_now_add=True)
    price  = models.PositiveIntegerField()
    is_negotiable = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name