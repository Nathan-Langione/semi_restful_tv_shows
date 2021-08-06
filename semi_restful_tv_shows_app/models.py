from django.db import models
from datetime import date, datetime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        desc_len = len(postData['description'])
        if 0 < desc_len and desc_len < 10:
            errors["description"] = "Description should be at least 10 characters"
        t_date = date.today()
        r_date =postData['release_date']
        fr_date = datetime.strptime(r_date,'%Y-%m-%d')
        if fr_date.year > t_date.year:
            errors["release_date"] = "Release date should be in the past"
        elif fr_date.year == t_date.year and fr_date.month > t_date.month:
            errors["release_date"] = "Release date should be in the past"
        elif fr_date.year == t_date.year and fr_date.month == t_date.month and fr_date.day > t_date.day:
            errors["release_date"] = "Release date should be in the past"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date= models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"User object: {self.title} {self.description} ({self.id})"
