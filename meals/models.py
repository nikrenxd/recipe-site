from django.db import models


class Meal(models.Model):
    type = models.CharField(max_length=75)
    meal_image = models.ImageField(upload_to="images/meals/", null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.type
