from alert import views
from django.urls import path, include

app_name = 'alert'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('results/', views.process, name="process"),
    path('reports/', views.reports, name="reports"),
    path('map/', views.map, name="map"),
    path('social-scrape-data/', views.social, name='social'),
    path('send-alert/', views.trigger_alert, name='alert_system'),
    path('tweelp-api/<str:keyword>/', views.api, name='api'),
    path('update-notifications/', views.update_notifications, name='update_notifications'),
    path('update-notifications-base/', views.update_notifications_base, name='update_notifications_base'),
    path('update/', views.update, name='update'),
    path('read/', views.read, name='read'),
    path('scheduler/', include('scheduler.urls'), name='scheduler'),
]
