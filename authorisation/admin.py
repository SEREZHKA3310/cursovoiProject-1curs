from django.contrib import admin
from .models import Exercise, Profile, Subscription, Workout, WorkoutExercise

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "difficulty", "date_earned")
    search_fields = ("name",)
    list_filter = ("difficulty",)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "age", "height", "weight")
    search_fields = ("user__username",)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "start_date", "end_date", "active")
    list_filter = ("active",)
    search_fields = ("user__username",)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("name", "date_created")
    search_fields = ("name",)

@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ("workout", "exercise", "repetitions", "sets")
    search_fields = ("workout__name", "exercise__name")