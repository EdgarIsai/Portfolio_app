from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    image = models.ImageField(upload_to="project_image",
                              blank=False,
                              default="../static/img/square-ppic.jpg")
    view_url = models.CharField(max_length=20, default="")
    code_url = models.CharField(max_length=200, default="")
