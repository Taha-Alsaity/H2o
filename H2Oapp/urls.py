from django.urls import path
from . import views


urlpatterns = [
    path('h2o/', views.index, name='home'),
    path('calories/', views.indexC, name='homeC'),
    path('', views.mainindex, name='mhome'),
    path('resault/<str:name>', views.calc, name='calc'),
    path('resault2/<str:name>', views.calcalc, name='calcalc'),
    
    path('h2o/en/', views.indexen, name='homeen'),
    path('calories/en/', views.indexCen, name='homeCen'),
]