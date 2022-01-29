from django.shortcuts import render
from django.views.generic.base import View

from .models import University, Olympiad


class UniversitiesView(View):
    """Список университетов"""

    def get(self, request):
        universities = University.objects.all()
        return render(request, "universities/list_univer.html", {"universities_list": universities})


class UniversityView(View):
    """Информация о университете"""

    def get(self, request, pk):
        university = University.objects.get(id=pk)
        return render(request, "universities/list_id.html", {"univer": university})


class OlympiadsView(View):
    """Список олимпиад"""

    def get(self, request):
        olympiads = Olympiad.objects.all()
        return render(request, "universities/list_olymp.html", {"olympiads_list": olympiads})
