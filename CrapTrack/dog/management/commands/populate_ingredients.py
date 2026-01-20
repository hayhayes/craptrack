from django.core.management.base import BaseCommand
from dog.models import Ingredient

class Command(BaseCommand):
    help = "Populate the Ingredient table with common dog food ingredients"

    def handle(self, *args, **options):
        ingredients_list = [
            # Meat
            {"name": "Chicken", "role": "meat"},
            {"name": "Beef", "role": "meat"},
            {"name": "Lamb", "role": "meat"},
            {"name": "Turkey", "role": "meat"},
            {"name": "Duck", "role": "meat"},
            {"name": "Salmon", "role": "meat"},
            {"name": "Whitefish", "role": "meat"},
            {"name": "Venison", "role": "meat"},
            {"name": "Bison", "role": "meat"},
            {"name": "Rabbit", "role": "meat"},
            {"name": "Pork", "role": "meat"},

            # Protein Meals
            {"name": "Chicken Meal", "role": "protien"},
            {"name": "Beef Meal", "role": "protien"},
            {"name": "Lamb Meal", "role": "protien"},
            {"name": "Fish Meal", "role": "protien"},
            {"name": "Turkey Meal", "role": "protien"},
            {"name": "Duck Meal", "role": "protien"},

            # Grains
            {"name": "Brown Rice", "role": "grain"},
            {"name": "White Rice", "role": "grain"},
            {"name": "Oats", "role": "grain"},
            {"name": "Barley", "role": "grain"},
            {"name": "Millet", "role": "grain"},
            {"name": "Corn", "role": "grain"},
            {"name": "Sorghum", "role": "grain"},
            {"name": "Rye", "role": "grain"},

            # Vegetables
            {"name": "Sweet Potato", "role": "vegtable"},
            {"name": "Potato", "role": "vegtable"},
            {"name": "Peas", "role": "vegtable"},
            {"name": "Carrots", "role": "vegtable"},
            {"name": "Spinach", "role": "vegtable"},
            {"name": "Pumpkin", "role": "vegtable"},
            {"name": "Green Beans", "role": "vegtable"},
            {"name": "Kale", "role": "vegtable"},
            {"name": "Broccoli", "role": "vegtable"},
            {"name": "Zucchini", "role": "vegtable"},

            # Fruits
            {"name": "Blueberries", "role": "fruit"},
            {"name": "Cranberries", "role": "fruit"},
            {"name": "Apples", "role": "fruit"},
            {"name": "Bananas", "role": "fruit"},
            {"name": "Pears", "role": "fruit"},
            {"name": "Raspberries", "role": "fruit"},
            {"name": "Pumpkin (fruit)", "role": "fruit"},

            # Fats
            {"name": "Chicken Fat", "role": "fat"},
            {"name": "Fish Oil", "role": "fat"},
            {"name": "Sunflower Oil", "role": "fat"},
            {"name": "Flaxseed Oil", "role": "fat"},
            {"name": "Canola Oil", "role": "fat"},

            # Fillers
            {"name": "Corn Gluten Meal", "role": "filler"},
            {"name": "Soybean Meal", "role": "filler"},
            {"name": "Wheat Gluten", "role": "filler"},
            {"name": "Rice Bran", "role": "filler"},

            # Preservatives
            {"name": "Salt", "role": "preservative"},
            {"name": "Mixed Tocopherols", "role": "preservative"},
            {"name": "Citric Acid", "role": "preservative"},
            {"name": "Rosemary Extract", "role": "preservative"},
            {"name": "Ascorbic Acid", "role": "preservative"},

            # Vitamins / Minerals
            {"name": "Vitamin A", "role": "vitamin/mineral"},
            {"name": "Vitamin D3", "role": "vitamin/mineral"},
            {"name": "Vitamin E", "role": "vitamin/mineral"},
            {"name": "Vitamin K", "role": "vitamin/mineral"},
            {"name": "Vitamin B12", "role": "vitamin/mineral"},
            {"name": "Niacin", "role": "vitamin/mineral"},
            {"name": "Calcium Carbonate", "role": "vitamin/mineral"},
            {"name": "Zinc Sulfate", "role": "vitamin/mineral"},
            {"name": "Iron Sulfate", "role": "vitamin/mineral"},
            {"name": "Copper Sulfate", "role": "vitamin/mineral"},
            {"name": "Manganese Sulfate", "role": "vitamin/mineral"},
            {"name": "Potassium Chloride", "role": "vitamin/mineral"},
            {"name": "Magnesium Oxide", "role": "vitamin/mineral"},

            # Additional proteins / meat sources
            {"name": "Egg", "role": "protien"},
            {"name": "Egg Meal", "role": "protien"},
            {"name": "Lamb Liver", "role": "meat"},
            {"name": "Beef Liver", "role": "meat"},
            {"name": "Duck Liver", "role": "meat"},
            {"name": "Venison Meal", "role": "protien"},
            {"name": "Rabbit Meal", "role": "protien"},

            # Extra vegetables / fruits
            {"name": "Chicory Root", "role": "vegtable"},
            {"name": "Alfalfa Meal", "role": "vegtable"},
            {"name": "Applesauce", "role": "fruit"},
            {"name": "Carrot Powder", "role": "vegtable"},

            # Other fats
            {"name": "Coconut Oil", "role": "fat"},
            {"name": "Lamb Fat", "role": "fat"},
            {"name": "Tallow", "role": "fat"},

            # Herbs / natural additives
            {"name": "Parsley", "role": "vegtable"},
            {"name": "Rosemary", "role": "vegtable"},
            {"name": "Yucca Schidigera Extract", "role": "vegtable"},

            # Grains & legumes
            {"name": "Chickpeas", "role": "grain"},
            {"name": "Lentils", "role": "grain"},
            {"name": "Peas", "role": "grain"},
            {"name": "Quinoa", "role": "grain"},

            # Treat-specific fillers
            {"name": "Glycerin", "role": "filler"},
            {"name": "Gelatin", "role": "filler"},

            # Other minerals
            {"name": "Sodium Selenite", "role": "vitamin/mineral"},
            {"name": "Potassium Iodide", "role": "vitamin/mineral"}
        ]


        for ingredient in ingredients_list:
            ing, created = Ingredient.objects.get_or_create(
                name=ingredient["name"],
                role=ingredient["role"]
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added ingredient: {ingredient['name']} ({ingredient['role']})"))
            else:
                self.stdout.write(f"Already exists: {ingredient['name']} ({ingredient['role']})")

        self.stdout.write(self.style.SUCCESS("Ingredient table population complete!"))
