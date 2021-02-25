from django.db import models
from allauth.app_settings import USER_MODEL
from django.contrib.auth.models import User


class Yogacourse(models.Model):
    COURSE_LEVEL_CHOICES = [
        ('L', 'Low'),
        ('M', 'Middle'),
        ('H', 'High')
    ]
    course = models.CharField(max_length=250)
    instructor = models.CharField(max_length=200)
    level = models.CharField(max_length=1, 
                            choices=COURSE_LEVEL_CHOICES,
                            default='M')
    description = models.TextField()
    datetime_start = models.DateTimeField()
    start_end_time = models.CharField(max_length=500)
    books = models.ManyToManyField(User, blank=True, related_name='course_books')

    class Meta:
        ordering = ('datetime_start',)

    def __str__(self):
        return self.course  

    def total_books(self):
        return self.books.count()

    #def get_absolute_url(self):
        #return reverse('yogastudio:course_detail', 
