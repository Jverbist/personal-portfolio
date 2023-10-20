from django.db import models
from django.db.models.fields import CharField

# Create your models here.
# site for reference fields: https://docs.djangoproject.com/en/4.2/ref/models/fields/
class Project(models.Model):
    title = models.CharField(max_lenth = 100)
    description = CharField(max_lenth= 250)
    image = models.ImageField(upload_to='folio/images/')
    url = models.URLField(blank=True)


