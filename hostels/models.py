from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class AdminManager(models.Manager):
    def get_queryset(self):
        return super(AdminManager, self).get_queryset()\
                                 .filter(owner__username='admin')


class Hostel(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='hostel_post')

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=462)

    image = models.ImageField(upload_to='hostel_image',
                              blank=False,
                              default='../static/available_hostels/img/001.jpg')

    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=250,
                            unique_for_date='publish',
                            default="")

    objects = models.Manager()
    admin = AdminManager()
    facilities = models.TextField(default='')

    def get_absolute_url(self):
        return reverse('hostel:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    def name_slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name
