from django.db import models

"""
    python3 erds/manage.py graph_models --pygraphviz app -I Classroom,Student,Assessment,Image,AssessmentImageGroup,Response,ImageGroup -o erd.png && open erd.png
"""
class Classroom(models.Model):
    name = models.TextField()

class Student(models.Model):
    name = models.TextField()
    classroom = models.ForeignKey(Classroom)

class Assessment(models.Model):
    name = models.TextField()

class Image(models.Model):
    file = models.FileField()

class ImageGroup(models.Model):
    target = models.ForeignKey(Image, related_name='target')
    foil1 = models.ForeignKey(Image, related_name='foil1')
    foil2 = models.ForeignKey(Image, related_name='foil2')
    foil3 = models.ForeignKey(Image, related_name='foil3')

class AssessmentImageGroup(models.Model):
    assessment = models.ForeignKey(Assessment)
    image_group = models.ForeignKey(ImageGroup)
    sort = models.IntegerField()

class Response(models.Model):
    student = models.ForeignKey(Student)
    image = models.ForeignKey(Image)
    image_group = models.ForeignKey(ImageGroup)
    correct = models.BooleanField()
    text = models.TextField()
