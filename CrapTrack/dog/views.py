from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from django.utils.dateparse import parse_datetime
from django.http import HttpResponseBadRequest


from .models import User, Dog, Ownership, Meal, Activity, Crap, Breed, Food, Brand

# TO START ENVIROMENT: source venv/bin/activate

# Create your views here.
def index(request):
    return render(request, "dog/index.html")

def about(request):
    return render(request, "dog/about.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "dog/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "dog/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "dog/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "dog/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "dog/register.html")

@login_required
def profile(request, username):
    user = request.user

    dogs = Dog.objects.filter(ownership__user=user).values(
        "id",
        "name",
        "image",
        "gender",
        "age",
        breed_name=F("breed__name"),
    )

    meals = Meal.objects.filter(user=user).order_by("-datetime").values(
        "id",
        "datetime",
        "meal",
        "amount",
        food_name=F("food__name"),
        dog_name=F("dog__name"),
    )

    activities = Activity.objects.filter(user=user).order_by("-datetime").values(
        "id",
        "datetime",
        "activity",
        "intensity",
        "minutes",
        dog_name=F("dog__name"),
    )

    craps = Crap.objects.filter(user=user).order_by("-datetime").values(
        "id",
        "datetime",
        "crap_type",
        "color",
        dog_name=F("dog__name"),
    )
    return render(request, "dog/profile.html", {
        "dogs": list(dogs),
        "meals": list(meals),
        "activities": list(activities),
        "craps": list(craps),
    })

@login_required
def dog_profile(request, id):
    if request.method != 'GET':
        return HttpResponseBadRequest("Invalid request method")

    user = request.user

    try:
        dog = Dog.objects.get(id=id, ownership__user=user)
    except Dog.DoesNotExist:
        return HttpResponseBadRequest("Dog not found or you do not have access")

    meals = Meal.objects.filter(user=user, dog=dog).order_by("-datetime").values(
        "id",
        "datetime",
        "meal",
        "amount",
        food_name=F("food__name"),
        dog_name=F("dog__name")
    )

    activities = Activity.objects.filter(user=user, dog=dog).order_by("-datetime").values(
        "id",
        "datetime",
        "activity",
        "intensity",
        "minutes",
        dog_name=F("dog__name")
    )

    craps = Crap.objects.filter(user=user, dog=dog).order_by("-datetime").values(
        "id",
        "datetime",
        "color",
        "crap_type",
        dog_name=F("dog__name")
    )

    return render(request, "dog/dog.html", {
        "dog": {
            "id": dog.id,
            "name": dog.name,
            "breed": dog.breed.name,
            "age": dog.age,
            "gender": dog.gender,
            "image": dog.image
        },
        "meals": list(meals),
        "activities": list(activities),
        "craps": list(craps),
    })

@login_required
@csrf_exempt
def dog(request):
    if request.method == "POST":
        name = request.POST.get("name")
        image = request.POST.get("image")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        breed_id = request.POST.get("breed")

        if not all([name, gender, age, breed_id]):
            return HttpResponseBadRequest("Missing fields")

        try:
            breed = Breed.objects.get(id=breed_id)
        except Breed.DoesNotExist:
            return HttpResponseBadRequest("Invalid breed")

        dog = Dog.objects.create(
            name=name,
            image=image,
            gender=gender,
            age=int(age),
            breed=breed
        )

        Ownership.objects.create(
            user=request.user,
            dog=dog,
            role="Owner"
        )

        return JsonResponse({
            "id": dog.id,
            "name": dog.name,
            "image": dog.image,
            "gender": dog.gender,
            "age": dog.age,
            "breed": dog.breed.name
        })

    return HttpResponseBadRequest("Invalid request")

@login_required
@csrf_exempt
def meals(request):
    if request.method == 'GET':
        meals = Meal.objects.filter(user=request.user).values(
            "id", "date", "meal", "food_name", "amount", "dog__name"
        )
        return JsonResponse(list(meals), safe=False)

    if request.method == "POST":
        dog_id = request.POST.get("dog")
        food_id = request.POST.get("food")
        meal_type = request.POST.get("meal")
        amount = request.POST.get("amount")
        date = request.POST.get("date")

        if not all([dog_id, food_id, meal_type, amount, date]):
            return HttpResponseBadRequest("Missing required fields")

        try:
            dog = Dog.objects.get(id=dog_id, ownership__user=request.user)
            food = Food.objects.get(id=food_id)
        except (Dog.DoesNotExist, Food.DoesNotExist):
            return HttpResponseBadRequest("Invalid dog or food")

        meal = Meal.objects.create(
            user=request.user,
            dog=dog,
            food=food,
            meal=meal_type,
            amount=int(amount),
            datetime=parse_datetime(date)
        )

        return JsonResponse({
            "id": meal.id,
            "datetime": meal.datetime,
            "meal": meal.meal,
            "food_name": meal.food.name,
            "amount": meal.amount,
            "dog_name": meal.dog.name
        })

    return HttpResponseBadRequest("Invalid request method")

@login_required
@csrf_exempt
def edit_meal(request, id):
    if request.method != "POST":
        return HttpResponseBadRequest("POST required")

    try:
        meal = Meal.objects.get(id=id, user=request.user)
    except Meal.DoesNotExist:
        return HttpResponseBadRequest("Meal not found")

    dog_id = request.POST.get("dog")
    food_id = request.POST.get("food")
    meal_type = request.POST.get("meal")
    amount = request.POST.get("amount")
    date = request.POST.get("date")

    if not all([dog_id, food_id, meal_type, amount, date]):
        return HttpResponseBadRequest("Missing fields")

    try:
        dog = Dog.objects.get(id=dog_id, ownership__user=request.user)
        food = Food.objects.get(id=food_id)
    except (Dog.DoesNotExist, Food.DoesNotExist):
        return HttpResponseBadRequest("Invalid dog or food")

    meal.dog = dog
    meal.food = food
    meal.meal = meal_type
    meal.amount = amount
    meal.date = date
    meal.save()

    return JsonResponse({
        "id": meal.id,
        "date": meal.date.isoformat(),
        "meal": meal.meal,
        "food_name": meal.food.name,
        "amount": meal.amount,
        "dog_name": meal.dog.name,
    })

@login_required
@csrf_exempt
def delete_meal(request, id):
    if request.method != "POST":
        return HttpResponseBadRequest("POST required")

    try:
        meal = Meal.objects.get(id=id, user=request.user)
    except Meal.DoesNotExist:
        return HttpResponseBadRequest("Meal not found")

    meal.delete()
    return JsonResponse({"success": True, "id": id})

@login_required
@csrf_exempt
def activity(request):
    if request.method == 'GET':
        activities = Activity.objects.filter(user=request.user).values(
            "id", "date", "type", "duration", "dog__name"
        )
        return JsonResponse(list(activities), safe=False)

    if request.method == "POST":
        dog_id = request.POST.get("dog")
        date = request.POST.get("date")
        activity_name = request.POST.get("activity")
        intensity = request.POST.get("intensity")
        minutes = request.POST.get("minutes")

        if not all([dog_id, date, activity_name, intensity, minutes]):
            return HttpResponseBadRequest("Missing required fields")

        try:
            dog = Dog.objects.get(id=dog_id, ownership__user=request.user)
        except Dog.DoesNotExist:
            return HttpResponseBadRequest("Invalid dog")

        activity = Activity.objects.create(
            user=request.user,
            dog=dog,
            activity=activity_name,
            intensity=intensity,
            minutes=int(minutes),
            datetime=parse_datetime(date)
        )

        return JsonResponse({
            "id": activity.id,
            "datetime": activity.datetime.isoformat(),
            "activity": activity.activity,
            "intensity": activity.intensity,
            "minutes": activity.minutes,
            "dog_name": activity.dog.name
        })

    return HttpResponseBadRequest("Invalid request method")

@login_required
@csrf_exempt
def crap(request):
    if request.method == 'GET':
        craps = Crap.objects.filter(user=request.user).values(
            "id", "date", "amount", "dog__name"
        )
        return JsonResponse(list(craps), safe=False)

    if request.method == "POST":
        dog_id = request.POST.get("dog")
        date = request.POST.get("date")
        crap_type = request.POST.get("type")
        color = request.POST.get("color")

        if not all([dog_id, date, crap_type, color]):
            return HttpResponseBadRequest("Missing required fields")

        try:
            dog = Dog.objects.get(id=dog_id, ownership__user=request.user)
        except (Dog.DoesNotExist, ValueError):
            return HttpResponseBadRequest("Invalid data")

        crap = Crap.objects.create(
            user=request.user,
            dog=dog,
            datetime=parse_datetime(date),
            crap_type=crap_type,
            color=color
        )

        return JsonResponse({
            "id": crap.id,
            "date": crap.datetime.isoformat(),
            "type": crap.crap_type,
            "color": crap.color,
            "dog_name": crap.dog.name
        })

    return HttpResponseBadRequest("Invalid request method")



def breeds(request):
    if request.method == 'GET':
        breeds = Breed.objects.all().order_by("name").values(
            "id", "name"
        )
        return JsonResponse(list(breeds), safe=False)

def brands(request):
    if request.method == 'GET':
        brands = Brand.objects.all().order_by("name").values(
            "id", "name"
        )
        return JsonResponse(list(brands), safe=False)

def foods(request, brand):
    if request.method == 'GET':
        foods = Food.objects.filter(brand__id=brand).order_by("name").values(
            "id", "name"
        )
        return JsonResponse(list(foods), safe=False)
