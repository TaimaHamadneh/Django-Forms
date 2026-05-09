from django.db import models
from django.utils.text import slugify

# Create your models here.
# save a shortened link to db - name, url, slug, # of clicks
class Link(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField()
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.clicks} clicks"
    
    def click(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.name.lower().replace(" ", "-")
        return super().save(*args, **kwargs)