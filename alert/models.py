from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture_url = models.URLField(null=True, blank=True)
    concurrency = models.IntegerField(default=3)
    is_previously_logged = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     if self.college.lower() == "jalpaiguri government engineering college" or self.college.lower() == "jgec":
    #         self.college = "JGEC"
    #     super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


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
