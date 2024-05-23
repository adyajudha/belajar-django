from django.urls import path
from . import views

urlpatterns = [
    path('<str:operasi>/<int:num1>/<int:num2>/', views.kalkulator, name='kalkulator'),
]
