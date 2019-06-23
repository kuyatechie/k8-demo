from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create),
    path('view/date:<str:date>', views.view_day_attendance),
]