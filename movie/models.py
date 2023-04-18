from django.db import models
from . import constants

class Movie(models.Model):
    name = models.TextField(null=True, blank=True, default='')
    protagonists = models.TextField(null=True, blank=True, default='')
    poster = models.TextField(null=True, blank=True, default='')
    started_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=constants.MOVIE_STATUS)
    ranking = models.IntegerField(default=0)

    def __str__(self):
        return '{}({})'.format(self.name, self.protagonists)
