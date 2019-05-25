from django.contrib import admin

# Register your models here.
from .models import AthenaCard, AthenaRank, AthenaVideoFile, AthenaImageFile
admin.site.register(AthenaCard)
admin.site.register(AthenaRank)
admin.site.register(AthenaVideoFile)
admin.site.register(AthenaImageFile)
