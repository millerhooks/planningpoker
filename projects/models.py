from django.db import models

DECK = (
    (0,0),
    (1,1),
    (2,2),
    (3,3),
    (5,5),
    (8,8),
    (13,13),
    (20,20),
    (40,40,),    
)

class UserProfile(model.Model):
    avatar  = models.FileField(upload_to="dynamic/files", blank=True)
    bio     = models.TextField(blank=True)
    title   = models.CharField(max_length=255)

class Project(model.Model):
    owner       = models.ForeignKey(User)
    managers    = models.ManyToManyField(User)
    description = models.TextField(blank=True)
    #tags
    
class Story(model.Model):
    story           = models.ForeignKey(Story)
    description     = models.TextField(blank=True)
    project         = models.ForeignKey(Project)
    developers      = models.ManyToManyField(User)
    owner           = models.ForeignKey(User)

class PlayedCard(model.Model):
    story   = models.ForeignKey(Story)
    player  = models.ForeignKey(User)
    card    = models.CharField(max_length=1, choices=DECK)

# Create your models here.
