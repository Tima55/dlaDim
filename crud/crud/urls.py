from django.urls import path
from hello import views

urlpatterns = [
    path("", views.index),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("update/<int:id>/", views.update),  # новый маршрут для обновления
    path("delete/<int:id>/", views.delete),
]