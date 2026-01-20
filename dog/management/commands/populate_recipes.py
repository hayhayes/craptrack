import random
from django.core.management.base import BaseCommand
from dog.models import Food, Ingredient, Recipe

# Randomly assigning for laziness
class Command(BaseCommand):
    help = "Automatically link Foods and Ingredients in the Recipe table"

    def handle(self, *args, **options):
        foods = Food.objects.all()
        ingredients = list(Ingredient.objects.all())

        if not ingredients:
            self.stdout.write(self.style.ERROR("No ingredients found. Populate ingredients first!"))
            return

        for food in foods:
            # Randomly assign 5-10 ingredients to each food
            num_ingredients = random.randint(5, 10)
            food_ingredients = random.sample(ingredients, min(num_ingredients, len(ingredients)))

            for ingredient in food_ingredients:
                recipe, created = Recipe.objects.get_or_create(
                    food=food,
                    ingredient=ingredient
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(
                        f"Linked {ingredient.name} to {food.name}"
                    ))
                else:
                    self.stdout.write(f"Already linked: {ingredient.name} -> {food.name}")

        self.stdout.write(self.style.SUCCESS("All foods have been linked to ingredients!"))
