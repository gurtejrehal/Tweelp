from django.contrib import admin
from alert.models import UserProfile, Notifications, Category, Report, UserReport

admin.site.site_header = 'Tweelp administration'


class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'pub_date',)
    search_fields = ['user']

    class Meta:
        verbose_name_plural = 'Notifications'


class ReportAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'category',)
    search_fields = ['keyword', 'category']
    list_filter = ['keyword', 'category']


class UserReportAdmin(admin.ModelAdmin):
    list_display = ('userprofile', 'reschedule', 'report',)
    search_fields = ['userprofile', 'report__keyword__name', 'report__category__name']
    list_filter = ['userprofile', 'report__category', 'report__keyword__name', ]
    list_editable = ('reschedule',)


admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Notifications, NotificationsAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(UserReport, UserReportAdmin)
