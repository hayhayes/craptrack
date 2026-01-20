from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class User(AbstractUser):
    pass

class Breed(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField()
    image = models.URLField(blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female')]
    )
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} ({self.breed})"

class Ownership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, default="Owner")

class Brand(models.Model):
    name = models.CharField(unique=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.brand.name})"

class Ingredient(models.Model):
    TYPE_CHOICES = [
        ('meat', 'Meat'),
        ('protien', 'Protien'),
        ('grain', 'Grain'),
        ('vegtable', 'Vegtable'),
        ('fruit', 'Fruit'),
        ('preservative', 'Preservative'),
        ('filler', 'Filler'),
        ('fat', 'Fat'),
        ('vitamin/mineral', 'Vitamin / Mineral')
    ]
    name = models.CharField()
    role = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES
    )

class Recipe(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

class Meal(models.Model):
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    datetime = models.DateTimeField()
    meal = models.CharField(max_length=10, choices=MEAL_CHOICES)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    amount = models.FloatField(help_text="Amount of food in grams")
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.dog.name} - {self.get_meal_display()} at {self.datetime.strftime('%Y-%m-%d %H:%M')}"

class Activity(models.Model):
    datetime = models.DateTimeField()
    activity = models.CharField()
    minutes = models.IntegerField()
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    intensity = models.CharField(
        max_length=10,
        choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')]
    )

    def __str__(self):
        return f"{self.dog.name} - {self.activity} at {self.datetime.strftime('%Y-%m-%d %H:%M')}"

class Crap(models.Model):
    COLOR_CHOICES = [
        ('brown', 'Brown'),
        ('black', 'Black'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('white', 'White'),
        ('red', 'Red')
    ]
    datetime = models.DateTimeField()
    crap_type = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])
    color = models.CharField(
        max_length=15,
        choices=COLOR_CHOICES
    )
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


