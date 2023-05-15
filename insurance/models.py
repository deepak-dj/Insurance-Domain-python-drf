from django.db import models


class RegisterUser(models.Model):
    name = models.CharField()
    mon_no = models.IntegerField()
    email = models.EmailField()
    password = models.CharField()

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField()
    mon_no = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Policy(models.Model):
    name = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.user.name


class Claim(models.Model):
    name = models.CharField()
    description = models.TextField()
    user = models.ManyToManyField(User)
    policy = models.ManyToManyField(Policy)

    def __str__(self):
        return self.user.name
