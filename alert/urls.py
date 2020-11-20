from alert import views
from django.urls import path

app_name = 'alert'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('update-notifications/', views.update_notifications, name='update_notifications'),
    path('update-notifications-base/', views.update_notifications_base, name='update_notifications_base'),
    path('update/', views.update, name='update'),
    path('read/', views.read, name='read'),
]
