from django.urls import path
from . import views

urlpatterns = [
    path('home', views.wall),
    path('all', views.wall_detail),
    path('create', views.wall_create),
    path('comment/<int:mess_id>/create', views.comment_create),
    path('message/<int:mess_id>/destroy', views.message_delete)
]