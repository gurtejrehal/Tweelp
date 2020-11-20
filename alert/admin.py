from django.contrib import admin
from alert.models import UserProfile, Notifications, Category

admin.site.site_header = 'Tweelp administration'

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'pub_date', )
    search_fields = ['user']

    class Meta:
        verbose_name_plural = 'Notifications'

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Notifications, NotificationsAdmin)
