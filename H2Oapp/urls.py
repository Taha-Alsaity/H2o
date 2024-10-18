from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('resault/<str:name>', views.calc, name='calc'),
    path('info/<str:name>', views.info, name='info'),
    path('en/', views.indexen, name='homeen'),
]