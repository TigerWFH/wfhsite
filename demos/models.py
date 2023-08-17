from django.db import models
from wagtail.core.models import Page


class StudentPage(Page):
    pass


class Student(models.Model):
    sname = models.CharField(max_length=20)
    sage = models.IntegerField()
    cid = models.ForeignKey('Class',
                            on_delete=models.CASCADE,
                            related_name='class_name')

    def __str__(self):
        return self.sname


class Class(models.Model):
    cname = models.CharField(max_length=20)
    cother = models.CharField(max_length=244)

    def __str__(self):
        return self.cname