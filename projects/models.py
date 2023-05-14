from django.db import models
import uuid

# Create your models here.


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, default=None)
    repository = models.URLField(max_length=9999, unique=True)
    link_deploy = models.URLField(max_length=9999)
    img = models.URLField(max_length=9999)
    created_at = models.DateTimeField(auto_now_add=True)

    techs = models.ManyToManyField("techs.Tech", related_name="projects")
