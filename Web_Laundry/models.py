from django.db import models


class FormNames(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.IntegerField(default=1234567)
    message = models.TextField()

    def __str__(self):
        return self.name


class AppointmentSection(models.Model):
    name = models.CharField(max_length=222)
    numb = models.IntegerField()
    services = models.CharField(max_length=222)
    serviceman = models.CharField(max_length=222)

    def __str__(self):
        return self.name


class SubscribeForm(models.Model):
    subscribe = models.EmailField()

    def __str__(self):
        return self.subscribe
