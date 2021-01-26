from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:val1>', views.num_ret),
    path('<int:val2>/edit', views.edit_num),
    path('<int:val3>/delete', views.destroy)
]