from django.db import models


# Create your models here.


class Weapon(models.Model):
    name = models.CharField(max_length=100)
    damage = models.IntegerField(max_length=5)

    def __str__(self):
        return self.name


class Avatar(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(max_length=3)
    weapon = models.ManyToManyField(Weapon, blank=True, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ForeignKey(Avatar, blank=True, null=True, on_delete=models.CASCADE)  # 1 to many

    def __str__(self):
        return self.name


class Person(models.Model):
    fio = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3)
    player = models.OneToOneField(Player, blank=True, null=True, on_delete=models.CASCADE)  # 1 to 1

    def __str__(self):
        return self.fio
