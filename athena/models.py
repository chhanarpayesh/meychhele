from django.conf import settings
from django.db import models
from django import forms
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator

import os

User = settings.AUTH_USER_MODEL
class AthenaCard(models.Model):
    looks = (
        ('l', 'L'),
        ('ll', 'L+'),
    )
    physique = (
        ('b', 'B'),
        ('bb', 'B+'),
    )
    places = (
        ('sa', 'South Asian'),
        ('wo', 'World'),
    )
    fmk = (
        ('f', 'Carnal Knowledge'),
        ('m', 'Tie the knot'),
    )

    def update_image_file(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.slug, ext)
        return os.path.join('athena/foodpic', filename)

    def update_vid_file(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.name, ext)
        return os.path.join('athena/videos', filename)

    def update_img_file(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.name, ext)
        return os.path.join('athena/images', filename)

    owner       =models.ForeignKey(User)
    name        =models.CharField(max_length=30, blank=False, null=True)
    details     =models.CharField(max_length=120, blank=True, null=True)
    roots       =models.CharField(max_length=14, blank=False, choices=places, null=True)
    dob         =models.DateField(blank=False, null=True, default='01/01/89')
    face        =models.CharField(max_length=5, blank=True, choices=looks, null=True)
    body        =models.CharField(max_length=5, blank=True, choices=physique, null=True)
    bazooka     =models.BooleanField(default=False)
    tushy       =models.BooleanField(default=False)
    incomplete  =models.BooleanField(default=False)
    mugshot     =models.ImageField(upload_to=update_image_file, blank=True, null=True)
    images      =models.ImageField(upload_to=update_img_file, blank=True, null=True)
    vid         =models.FileField(upload_to=update_vid_file, blank=True, null=True)
    vid1        =models.URLField(blank=True, null=True)
    vid2        =models.URLField(blank=True, null=True)
    vid3        =models.URLField(blank=True, null=True)
    vid4        =models.URLField(blank=True, null=True)
    status      =models.CharField(max_length=20, blank=False, choices=fmk, null=True)
    timestamp   =models.DateTimeField(auto_now_add=True)
    updated     =models.DateTimeField(auto_now=True)
    slug        =models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('athena:detail', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('timestamp',)

    @property
    def title(self):
        return self.name


class AthenaRank(models.Model):
    owner       =models.ForeignKey(User)
    athena      =models.ForeignKey(AthenaCard, on_delete=models.CASCADE, blank=False)
    rank        =models.IntegerField(unique=True, blank=True, null=False)
    timestamp   =models.DateTimeField(auto_now_add=True)
    updated     =models.DateTimeField(auto_now=True)
    slug        =models.SlugField(blank=True, null=True)

    def __str__(self):
        return str(self.athena)

    def get_absolute_url(self):
        return reverse('athena:rank')

    class Meta:
        ordering = ('rank',)


class AthenaVideoFile(models.Model):
    def update_vid_file(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.athena.name, ext)
        return os.path.join('athena/videos', filename)

    exts = ['mp4', 'mkv', 'avi', '3gp']

    athena      =models.ForeignKey(AthenaCard, on_delete=models.CASCADE, blank=False)
    vid         =models.FileField(upload_to=update_vid_file, validators=[FileExtensionValidator(allowed_extensions=exts)], null=True)
    timestamp   =models.DateTimeField(auto_now_add=True)
    updated     =models.DateTimeField(auto_now=True)
    slug        =models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.athena.name
    
    def filename(self):
        return os.path.basename(self.athena.name)
    
    def get_absolute_url(self):
        return reverse('athena:detail', kwargs={'slug':self.athena.slug})

    class Meta:
        ordering = ('timestamp',)

    @property
    def title(self):
        return self.athena.name


class AthenaImageFile(models.Model):
    def update_img_file(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.athena.name, ext)
        return os.path.join('athena/images', filename)

    athena      =models.ForeignKey(AthenaCard, on_delete=models.CASCADE, blank=False)
    img         =models.ImageField(upload_to=update_img_file, null=True)
    timestamp   =models.DateTimeField(auto_now_add=True)
    updated     =models.DateTimeField(auto_now=True)
    slug        =models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.athena.name
    
    def filename(self):
        return os.path.basename(self.athena.name)
    
    def get_absolute_url(self):
        return reverse('athena:detail', kwargs={'slug':self.athena.slug})

    class Meta:
        ordering = ('timestamp',)

    @property
    def title(self):
        return self.athena.name


def ac_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.name = str(instance.name).title()
        instance.slug = slugify(instance.name)

def ar_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = instance.rank

pre_save.connect(ac_pre_save_receiver, sender=AthenaCard)
pre_save.connect(ar_pre_save_receiver, sender=AthenaRank)
