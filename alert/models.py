from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture_url = models.URLField(null=True, blank=True)
    is_previously_logged = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     if self.college.lower() == "jalpaiguri government engineering college" or self.college.lower() == "jgec":
    #         self.college = "JGEC"
    #     super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username
