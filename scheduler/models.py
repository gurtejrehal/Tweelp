from django.db import models


class ScrapedLink(models.Model):
    keyword = models.CharField(max_length=200, blank=False, null=False)
    scrape_data = models.TextField(max_length=3000, blank=True)
    schedule_day = models.IntegerField(default=3)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.keyword


class RescrapedLink(models.Model):
    keyword = models.ForeignKey(ScrapedLink, on_delete=models.CASCADE)
    scrape_data = models.TextField(max_length=3000, blank=True)
    score = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.keyword.keyword)
