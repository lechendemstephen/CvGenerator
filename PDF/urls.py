from django.urls import path
from . import views
urlpatterns = [
    path('cv/', views.home, name='home' ),
    path('<int:id>/', views.resume, name='resume'),

    path('download/', views.cv, name='cv')
]
