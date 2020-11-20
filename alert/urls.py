from alert import views
from django.urls import path

app_name = 'alert'

urlpatterns = [
    path('home/', views.index, name='index')
]
