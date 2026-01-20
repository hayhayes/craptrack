from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("meals", views.meals, name="meals"),
    path("activity", views.activity, name="activity"),
    path("crap", views.crap, name="crap"),
    path("about", views.about, name="about"),
    path("breeds", views.breeds, name="breeds"),
    path("foods/<int:brand>", views.foods, name="foods"),
    path("brands", views.brands, name="brands"),
    path("dog", views.dog, name="dog"),
    path("dogs/<int:id>", views.dog_profile, name="dog_profile"),
    path("meals/<int:id>/edit", views.edit_meal, name="edit_meal"),
    path("meals/<int:id>/delete/", views.delete_meal, name="delete_meal"),

]
