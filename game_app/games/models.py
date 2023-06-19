from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class GameModel(models.Model):
    title = models.CharField(unique=True, max_length=30)
    category = models.CharField(choices=(('Action', 'Action'),
                                         ("Adventure", 'Adventure'),
                                         ('Puzzle', 'Puzzle'),
                                         ('Strategy', 'Strategy'),
                                         ('Strategy', 'Strategy'),
                                         ('Sports', 'Sports'),
                                         ('Board/Card Game', 'Board/Card Game'),
                                         ('Other', 'Other')
                                         ),
                                max_length=15
                                )
    rating = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(5.0)])
    max_level = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0.1)] )
    image_url = models.URLField()
    summary = models.TextField(null=True, blank=True)