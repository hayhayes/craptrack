from django.core.management.base import BaseCommand
from dog.models import Food, Brand

# RUN COMMAND python manage.py populate_food

class Command(BaseCommand):
    help = 'populate the Foods table with popular dog food '

    def handle(self, *args, **options):
        foods_by_brand = {
            "Blue Buffalo": [
                "Life Protection Formula Chicken & Brown Rice",
                "Freedom Grain Free Salmon & Sweet Potato",
                "Homestyle Recipe Chicken Dinner"
            ],
            "Hill's Science Diet": [
                "Adult Sensitive Stomach & Skin",
                "Puppy Healthy Development Chicken",
                "Adult Large Breed Chicken"
            ],
            "Royal Canin": [
                "Mini Adult Dry Dog Food",
                "Medium Breed Puppy",
                "Gastrointestinal Fiber Response"
            ],
            "Purina Pro Plan": [
                "Savor Adult Shredded Blend Chicken & Rice",
                "Focus Adult Sensitive Skin Salmon & Rice",
                "Pro Plan Puppy Chicken & Rice"
            ],
            "Purina ONE": [
                "SmartBlend True Instinct Chicken & Rice",
                "Tender Selects Blend with Real Chicken",
                "Healthy Weight Adult Chicken & Rice"
            ],
            "Iams": [
                "ProActive Health Adult Chicken",
                "Healthy Puppy Chicken",
                "Sensitive Stomach & Skin"
            ],
            "Nutro": [
                "Wholesome Essentials Adult Chicken & Brown Rice",
                "Ultra Grain Free Salmon & Lentils",
                "Max Adult Large Breed Chicken"
            ],
            "Wellness": [
                "Complete Health Adult Deboned Chicken & Oatmeal",
                "CORE Grain Free Original Turkey & Chicken",
                "Healthy Development Puppy Chicken"
            ],
            "Orijen": [
                "Original Dry Dog Food",
                "Regional Red Grain Free",
                "Six Fish Grain Free"
            ],
            "Acana": [
                "Grasslands Grain Free",
                "Wild Prairie Grain Free",
                "Pacifica Grain Free"
            ],
            "Natural Balance": [
                "L.I.D. Limited Ingredient Diets Chicken & Brown Rice",
                "Ultra Whole Body Health Chicken & Fish",
                "Fat Dogs Chicken & Oatmeal"
            ],
            "Taste of the Wild": [
                "High Prairie Canine Recipe",
                "Pacific Stream Canine Recipe",
                "Sierra Mountain Canine Recipe"
            ],
            "Merrick": [
                "Grain Free Real Texas Beef",
                "Backcountry Raw Infused Beef & Venison",
                "Lil’ Plates Small Breed Chicken"
            ],
            "Canidae": [
                "All Life Stages Multi-Protein",
                "Pure Limited Ingredient Duck & Potato",
                "Grain Free PURE Sea"
            ],
            "Pedigree": [
                "Adult Complete Nutrition Chicken",
                "Small Breed Complete Nutrition",
                "Dentastix Dog Treats"
            ],
            "Eukanuba": [
                "Adult Large Breed Chicken",
                "Puppy Small Breed Chicken",
                "Adult Weight Control Chicken"
            ],
            "Fromm": [
                "Gold Adult Chicken & Liver",
                "Four-Star Nutritionals Beef & Lamb",
                "Classic Puppy Chicken & Lamb"
            ],
            "Instinct": [
                "Raw Boost Grain Free Chicken",
                "Original Grain Free Real Lamb",
                "Frozen Raw Bites Turkey"
            ],
            "Earthborn Holistic": [
                "Primitive Natural Chicken & Turkey",
                "Ocean Fusion Grain Free Salmon",
                "Great Plains Feast"
            ],
            "Victor": [
                "Hi-Pro Plus Chicken & Rice",
                "Select Protein Formula Beef & Rice",
                "Purpose Nutra Pro"
            ],
            "Solid Gold": [
                "Wolf King Large Breed",
                "Leaping Waters Grain Free Salmon",
                "Fit & Fabulous Small Breed"
            ],
            "Diamond Naturals": [
                "Large Breed Chicken & Rice",
                "Small Breed Chicken & Brown Rice",
                "Skin & Coat Formula Salmon"
            ],
            "American Journey": [
                "Adult Chicken & Brown Rice",
                "Grain Free Turkey & Sweet Potato",
                "Puppy Chicken & Brown Rice"
            ],
            "Rachel Ray Nutrish": [
                "Real Chicken Recipe",
                "Indoor Complete Chicken & Brown Rice",
                "Zero Grain Turkey & Potato"
            ],
            "Holistic Select": [
                "Adult Health Chicken & Brown Rice",
                "Sensitive Stomach Salmon & Rice",
                "Weight Management Chicken"
            ],
            "Farmina": [
                "N&D Grain Free Chicken & Pomegranate",
                "N&D Grain Free Lamb & Blueberry",
                "N&D Low Grain Chicken & Pumpkin"
            ],
            "Nature's Logic": [
                "Canine Chicken Meal Feast",
                "Canine Turkey Meal Feast",
                "Canine Salmon Meal Feast"
            ],
            "Nature's Variety": [
                "Instinct Raw Boost Chicken",
                "Instinct Raw Boost Lamb",
                "Primal Freeze-Dried Beef Nuggets"
            ],
            "Annamaet": [
                "Grain Free Chicken & Turkey",
                "Grain Free Salmon & Turkey",
                "Performance Dog Food Beef"
            ],
            "Dr. Tim's": [
                "Pet Food Basics Chicken & Rice",
                "Weight Management Formula",
                "All Life Stages Formula"
            ],
            "Stella & Chewy's": [
                "Freeze-Dried Raw Dinner Chicken",
                "Frozen Raw Nuggets Beef",
                "Freeze-Dried Raw Patties Turkey"
            ],
            "Primal": [
                "Freeze-Dried Chicken Nuggets",
                "Frozen Beef Patties",
                "Frozen Turkey Nuggets"
            ],
            "Ziwi Peak": [
                "Air-Dried Beef Recipe",
                "Air-Dried Lamb Recipe",
                "Air-Dried Venison Recipe"
            ]
        }


        for brand_name, food_list in foods_by_brand.items():
            brand, _ = Brand.objects.get_or_create(name=brand_name)
            for food_name in food_list:
                food, created = Food.objects.get_or_create(name=food_name, brand=brand)
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added food: {food_name} ({brand_name})"))
                else:
                    self.stdout.write(f"Already exists: {food_name} ({brand_name})")

        self.stdout.write(self.style.SUCCESS("Food table population complete!"))
