from django.conf import settings
from django.db import models
from django import forms
from django.db.models.signals import pre_save, post_save
from .utils import random_string_generator, unique_slug_generator, metadata_generator
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator

import os
import datetime

User = settings.AUTH_USER_MODEL
class CinemaBook(models.Model):
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z? ,-]*$', 'Only alphanumeric characters are allowed.')
	categories = (
		('Feature', 'Feature'),
		('Short', 'Short'),
		('Doc', 'Documentary'),
		)
	YEAR_CHOICES = []
	for r in range((datetime.datetime.now().year+1), 1900, -1):
	    YEAR_CHOICES.append((r,r))

	owner		=models.ForeignKey(User)
	name        =models.CharField(max_length=50, blank=False, validators=[alphanumeric])
	language    =models.CharField(max_length=40, blank=True, default='English')
	category    =models.CharField(max_length=10, choices=categories, blank=False)
	year        =models.IntegerField(choices=YEAR_CHOICES, blank=False, default=datetime.datetime.now().year)
	cast        =models.CharField(max_length=420, blank=True)
	director    =models.CharField(max_length=30, blank=True)
	metascore   =models.CharField(max_length=10, blank=True)
	meter       =models.CharField(max_length=10, blank=True)
	synopsis    =models.TextField(blank=True)
	wpurl 		=models.URLField(blank=True)
	cinto       =models.TextField(blank=True)
	dialogs     =models.TextField(blank=True)
	popref      =models.TextField(blank=True)
	verify      =models.BooleanField(default=False)
	public		=models.BooleanField(default=True)
	timestamp   =models.DateTimeField(auto_now_add=True)
	updated     =models.DateTimeField(auto_now=True)
	slug        =models.SlugField(blank=True, null=True)

	def __str__(self):
	    return self.name
	
	def get_absolute_url(self):
	    return reverse('cinema:detail', kwargs={'slug':self.slug})

	class Meta:
		ordering = ('-timestamp', 'name',)

	@property
	def title(self):
	    return self.name

class DesignShot(models.Model):
	def update_intdes_file(instance, filename):
		# shorten the name of the uploaded image
		ext = filename.split('.')[-1]
		filename = "%s_%s.%s" % (instance.dimage.name[:5], random_string_generator(size=5), ext)
		return os.path.join('cinema/intdes', filename)

	owner	 	=models.ForeignKey(User)
	dimage  	=models.ImageField(blank=True,upload_to=update_intdes_file)
	cinema 		=models.ForeignKey(CinemaBook, on_delete=models.CASCADE)
	timestamp   =models.DateTimeField(auto_now_add=True)
	updated     =models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.dimage)

	def get_absolute_url(self): # return to the cinema page
	    return ("/cinema/"+self.cinema.slug)

	class Meta:
		ordering = ('cinema',)

class FoodShot(models.Model):
	def update_foodmen_file(instance, filename):
		# shorten the name of the uploaded image
		ext = filename.split('.')[-1]
		filename = "%s_%s.%s" % (instance.fimage.name[:5], random_string_generator(size=5), ext)
		return os.path.join('cinema/foodmen', filename)

	owner	 	=models.ForeignKey(User)
	fimage  	=models.ImageField(blank=True, upload_to=update_foodmen_file)
	cinema 		=models.ForeignKey(CinemaBook, on_delete=models.CASCADE)
	timestamp   =models.DateTimeField(auto_now_add=True)
	updated     =models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.fimage)

	def get_absolute_url(self):
		# return to the cinema page
	    return ("/cinema/"+self.cinema.slug)

	class Meta:
		ordering = ('cinema',)

class LocationShot(models.Model):
	def update_location_file(instance, filename):
		# shorten the name of the uploaded image
		ext = filename.split('.')[-1]
		filename = "%s_%s.%s" % (instance.limage.name[:5], random_string_generator(size=5), ext)
		return os.path.join('cinema/location', filename)

	owner	 	=models.ForeignKey(User)
	limage  	=models.ImageField(blank=True, upload_to=update_location_file)
	cinema 		=models.ForeignKey(CinemaBook, on_delete=models.CASCADE)
	timestamp   =models.DateTimeField(auto_now_add=True)
	updated     =models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.limage)

	def get_absolute_url(self): # return to the cinema page
	    return ("/cinema/"+self.cinema.slug)

	class Meta:
		ordering = ('cinema',)

class Beginnings(models.Model):
	owner	 	=models.ForeignKey(User)
	lines    	=models.TextField(blank=True)
	scenes    	=models.TextField(blank=True)
	cinema 		=models.ForeignKey(CinemaBook, on_delete=models.CASCADE)
	timestamp   =models.DateTimeField(auto_now_add=True)
	updated     =models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id)

	def get_absolute_url(self):
		# return to the cinema page
	    return ("/cinema/"+self.cinema.slug)

	class Meta:
		ordering = ('cinema',)

class Endings(models.Model):
	owner	 	=models.ForeignKey(User)
	lines    	=models.TextField(blank=True)
	scenes    	=models.TextField(blank=True)
	cinema 		=models.ForeignKey(CinemaBook, on_delete=models.CASCADE)
	timestamp   =models.DateTimeField(auto_now_add=True)
	updated     =models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id)

	def get_absolute_url(self): # return to the cinema page
	    return ("/cinema/"+self.cinema.slug)

	class Meta:
		ordering = ('cinema',)

def cb_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

def cb_post_save_receiver(sender, instance=None, created=False, *args, **kwargs):
	if not instance:
		return

	if hasattr(instance, '_dirty'):
		return

	# crawl metadata from the web
	if '_' in instance.slug: # if instance is already created
		cast, dirm, meta, meter, syn, wp_url = metadata_generator(
			instance.name, instance.year
		)
		if (cast and dirm and meta and meter):
			instance.verify = True
		else:
			instance.verify = False

		instance.cast = cast
		instance.director = dirm
		instance.metascore = meta
		instance.meter = meter
		instance.synopsis = syn
		instance.wpurl = wp_url

		# insert the instance id to the slug
		urlslug = instance.slug.split('_')
		urlslug.insert(-1, str(instance.id))
		instance.slug = '-'.join(urlslug)
		print (instance.slug)

	# prevent going into a post_save loop
	try:
		instance._dirty = True
		instance.save()
	finally:
		del instance._dirty

pre_save.connect(cb_pre_save_receiver, sender=CinemaBook)
post_save.connect(cb_post_save_receiver, sender=CinemaBook)
