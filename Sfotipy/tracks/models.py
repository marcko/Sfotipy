from django.db import models

# Create your models here.


from albums.models import Album 
from artists.models import Artist 


class Track(models.Model):
	title = models.CharField(max_length=255)
	order = models.PositiveIntegerField()
	track = models.FileField(upload_to= 'tracks_file')
	artist = models.ForeignKey(Artist)
	album = models.ForeignKey(Album)

	def __str__(self):
		return self.title
