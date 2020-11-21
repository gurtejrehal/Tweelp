import math
import random
import json

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

predicted_data = {
    'News_Authenticity': '92%',
    'Accuracy Score': '95%'
}
old_data = json.dumps(predicted_data)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture_url = models.URLField(null=True, blank=True,
                                  default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRThY_01nTnP3fP1WlRQrF45q43HGU5O2PwjA&usqp=CAU')
    concurrency = models.IntegerField(default=3)
    crawled_links = models.IntegerField(default=0)
    recent_link = models.IntegerField(default=5)
    is_previously_logged = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     if self.college.lower() == "jalpaiguri government engineering college" or self.college.lower() == "jgec":
    #         self.college = "JGEC"
    #     super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def time_spent_working(self):
        now = timezone.now()
        diff = now - self.user.date_joined
        minutes = diff.total_seconds() / 3600
        return round(minutes, 1)

    def percent(self):
        result = random.randint(-3, 10)
        return (True, result) if result >= 0 else (False, -1 * result)

    def concurrency_percent(self):
        return (self.concurrency / 10) * 100


class Keyword(models.Model):
    """
    Keywords Table
    """

    name = models.CharField(max_length=100, blank=False, null=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Category Table
    """

    name = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower().replace(' ', '_')
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'


class Report(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    predicted_data = models.TextField(max_length=3000, blank=True, default=old_data)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "for keyword " + str(self.keyword) + " in category " + str(self.category)


class UserReport(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    reschedule = models.IntegerField(default=3)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "by - " + self.userprofile.user.username

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.pub_date

        if diff.days == 0 and 0 <= diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"

            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and 60 <= diff.seconds < 3600:
            minutes = math.floor(diff.seconds / 60)

            if minutes == 1:
                return str(minutes) + " minute ago"

            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and 3600 <= diff.seconds < 86400:
            hours = math.floor(diff.seconds / 3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if 1 <= diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if 30 <= diff.days < 365:
            months = math.floor(diff.days / 30)

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years = math.floor(diff.days / 365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"


class Notifications(models.Model):
    """
    Notifications Table
    """

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, blank=False, null=False)
    read = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user.username + " ----------> " + str(self.pub_date)

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.pub_date

        if diff.days == 0 and 0 <= diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"

            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and 60 <= diff.seconds < 3600:
            minutes = math.floor(diff.seconds / 60)

            if minutes == 1:
                return str(minutes) + " minute ago"

            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and 3600 <= diff.seconds < 86400:
            hours = math.floor(diff.seconds / 3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if 1 <= diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if 30 <= diff.days < 365:
            months = math.floor(diff.days / 30)

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years = math.floor(diff.days / 365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"
