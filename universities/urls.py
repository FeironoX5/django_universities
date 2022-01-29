from django.urls import path
from . import views

urlpatterns = [
    # path("", views.AllView.as_view()),
    path("universities", views.UniversitiesView.as_view()),
    path("olymps", views.OlympiadsView.as_view()),
    path("<int:pk>/", views.UniversityView.as_view(), name="univer_info")
]
