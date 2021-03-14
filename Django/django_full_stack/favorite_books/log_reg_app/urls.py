from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/create', views.new_user),
    path('user/login', views.login_user),
    path('user/logout', views.logout),

    path('books', views.home),
    path('books/create', views.create_book),
    path('books/<int:book_id>', views.view_book),
    path('books/<int:book_id>/edit', views.edit_book),
    path('books/<int:book_id>/destroy', views.delete_book),
    path('books/<int:book_id>/favorite', views.fav_book),
    path('books/<int:book_id>/unfav', views.unfav_book)
]