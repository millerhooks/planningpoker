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
    avatar
    bio
    title

class Project(model.Model):
    owner       = models.ForeignKey(User)
    managers    = models.ManyToManyField(User)
    description
    tags
    
class Story(model.Model):
    story
    description
    project         = models.ForeignKey(Project)
    developers      = models.ManyToManyField(User)
    owner           = models.ForeignKey(User)

class PlayedCard(model.Model):
    story
    player
    card    = models.CharField(max_length=1, choices=DECK)

# Create your models here.
