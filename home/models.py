from django.db import models


class Home(models.Model):
    image = models.FilePathField(path='/img')