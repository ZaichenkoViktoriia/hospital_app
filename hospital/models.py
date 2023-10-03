from django.contrib.auth.models import AbstractUser
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Doctor(AbstractUser):
    def __str__(self):
        return self.username


class Assistant(models.Model):
    name = models.CharField(max_length=255, default=None)
    room = models.ForeignKey("Room", related_name="assistants", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.name} in {self.room} room"


class Room(models.Model):
    number = models.CharField(max_length=63)
    department = models.ForeignKey(
        "Department",
        on_delete=models.CASCADE,
        null=True,
        related_name="rooms",
        default=None,
    )

    def __str__(self):
        return self.number


class Medicament(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Patient(models.Model):
    full_name = models.CharField(max_length=255)
    diagnosis = models.CharField(max_length=255)
    home_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=63)
    room = models.ForeignKey(
        "Room",
        on_delete=models.CASCADE,
        related_name="patients"
    )
    medicament = models.ManyToManyField("Medicament", related_name="patients", default=None)

    def __str__(self):
        return f"{self.full_name} {self.room} {self.diagnosis}"

