from django.contrib import admin
from .models import tourModel
from .models import feedbackModel
# Register your models here.

admin.site.register(tourModel)
admin.site.register(feedbackModel)
