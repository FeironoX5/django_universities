from django.db import models
from django.urls import reverse


class University(models.Model):
    full_name = models.TextField("Полное название", max_length=250)
    short_name = models.CharField("Сокращенное название", max_length=50)
    address = models.CharField("Адрес", max_length=150)
    phone = models.CharField("Телефон", max_length=50)
    url = models.URLField(max_length=150, unique=True)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = "Университет"
        verbose_name_plural = "Университеты"

    def get(self):
        return reverse("univer_info", kwargs={"pk": self.id})


class Subject(models.Model):
    name = models.TextField("Полное название", max_length=250)

    def __str__(self):
        return self.name


class Olympiad(models.Model):
    name = models.TextField("Полное название", max_length=250)
    rating = models.FloatField("Рейтинг")
    description = models.CharField("Описание", max_length=3000)
    url = models.URLField(max_length=150, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    universities = models.ManyToManyField(University)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Олимпиада"
        verbose_name_plural = "Олимпиады"


# class LinkOlympiads(models.Model):
#     univer = models.ForeignKey(University, on_delete=models.CASCADE)
#     olymp = models.ForeignKey(Olympiad, on_delete=models.CASCADE)
