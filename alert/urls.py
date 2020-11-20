from alert import views
from django.urls import path

app_name = 'alert'

urlpatterns = [
    path('', views.index, name='index')
]
