from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/create', views.create_course),
    path('/destroy/<int:id>', views.confirm_delete),
    path('/<int:id>/destroy', views.delete_course)
]