from django.db import models
from django.conf import settings
# Create your models here.


class collab_project(models.Model):
    p_name = models.CharField(max_length=75)
    p_desc = models.CharField(max_length=200)
    p_prerequisite = models.CharField(max_length=200,
                                      default="No prerequisite required")
    p_level = models.CharField(max_length=20, default="Beginner")
    p_category = models.CharField(max_length=30, default="Beginner")
    p_part = models.IntegerField()
    p_image = models.ImageField(upload_to="project/media", default="")

    def __str__(self):
        return self.p_name
