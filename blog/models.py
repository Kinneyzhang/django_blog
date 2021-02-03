# -*- coding: utf-8 -*-
from django.db import models
from mdeditor.fields import MDTextField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    POST_STATUS = (
        ('editing', 'editing'),
        ('completed', 'completed')
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, db_index=True)
    abstract = models.CharField(max_length=200)
    count = models.IntegerField()
    status = models.CharField(max_length=10, choices=POST_STATUS)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
    )
    timestamp = models.DateTimeField()
    # auto_now_add=True
    updatetime = models.DateTimeField(auto_now=True)
    content = MDTextField()
    
    def __str__(self):
        return self.title

class Friend(models.Model):
    name = models.CharField(max_length=20)
    link = models.URLField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=50)
    iframe = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Diary(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    content = MDTextField()

class PlanCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Plan(models.Model):
    PLAN_STATUS = (
        ('todo', 'todo'),
        ('done', 'done'),   
    )
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=4, choices=PLAN_STATUS)
    category = models.ForeignKey(
        PlanCategory,
        on_delete=models.CASCADE,
        null=True,
    )
    timestamp = models.DateTimeField(auto_now_add=True)
