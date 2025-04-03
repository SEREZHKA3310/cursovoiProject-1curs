from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    BEGINNER = 'Начинающий'
    INTERMEDIATE = 'Средний'
    PROFESSIONAL = 'Профессионал'

    DIFFICULTY_LEVELS = [
        (BEGINNER, 'Начинающий'),
        (INTERMEDIATE, 'Средний'),
        (PROFESSIONAL, 'Профессионал'),
    ]

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=False, null=True)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS)
    date_earned = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=False, null=True)
    height = models.FloatField(blank=False, null=True)
    weight = models.FloatField(blank=False, null=True)

    def __str__(self):
        return self.user.username


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.active}"


class Workout(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.IntegerField()
    sets = models.IntegerField()

    def __str__(self):
        return f"{self.workout.name} - {self.exercise.name}"