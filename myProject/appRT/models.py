from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
	position = models.CharField(max_length=10)
	name = models.CharField(max_length=50)
	description = models.TextField()
	image = models.CharField(max_length=255)
	productionCompany = models.CharField(max_length=50)
	genre = models.CharField(max_length=50)
	director = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	rating = models.CharField(max_length=20)
	
	def __unicode__(self):
		#return (self.position, self.name, self.productionCompany, self.description, self.image, self.genre, self.director, self.author)
		return "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}".format(self.position, self.name, self.productionCompany, self.description, self.image, self.genre, self.director, self.author, self.rating)
