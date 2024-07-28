from django.urls import path
from . import views
urlpatterns = [
    path('cv/', views.home, name='home' ),
    path('download_cv/<int:id>/', views.resume, name='resume')

]
