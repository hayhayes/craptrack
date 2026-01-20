from django.core.management.base import BaseCommand
from dog.models import Brand

# RUN COMMAND python manage.py populate_brands

class Command(BaseCommand):
    help = 'populate the Brands table with popular dog food brands'

    def handle(self, *args, **options):
        dog_food_brands = [
            "Blue Buffalo",
            "Hill's Science Diet",
            "Royal Canin",
            "Purina Pro Plan",
            "Purina ONE",
            "Iams",
            "Nutro",
            "Wellness",
            "Orijen",
            "Acana",
            "Natural Balance",
            "Taste of the Wild",
            "Merrick",
            "Canidae",
            "Pedigree",
            "Eukanuba",
            "Fromm",
            "Instinct",
            "Earthborn Holistic",
            "Victor",
            "Solid Gold",
            "Diamond Naturals",
            "American Journey",
            "Rachel Ray Nutrish",
            "Holistic Select",
            "Farmina",
            "Nature's Logic",
            "Nature's Variety",
            "Annamaet",
            "Dr. Tim's",
            "Stella & Chewy's",
            "Primal",
            "Ziwi Peak"
        ]


        for brand_name in dog_food_brands:
            brand, created = Brand.objects.get_or_create(name=brand_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added brand: {brand_name}"))
            else:
                self.stdout.write(f"Already exists: {brand_name}")
