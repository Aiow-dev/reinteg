from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_show, name='home'),
    path('method/piece_linear_approximation/',
         views.piece_linear_approximation_show,
         name='piece_linear_approximation_method'),
    path('method/piece_permanent_approximation/',
         views.piece_permanent_approximation_show,
         name='piece_permanent_approximation_method'),
    path('functions/', views.functions, name='functions'),
    path('functions/result', views.result, name='result'),
]
