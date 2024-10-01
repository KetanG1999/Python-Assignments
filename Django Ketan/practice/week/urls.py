from django.urls import path
from .import views

urlpatterns = [
    path('<str:week>',views.weekly_task),
    path('<int:week>',views.weekly_task_by_number)
]