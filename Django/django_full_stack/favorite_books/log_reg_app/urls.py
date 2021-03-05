from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/create', views.new_user),
    path('user/login', views.login_user),
    path('user/logout', views.logout),

    path('books', views.home),
    path('books/create', views.create_book)
]