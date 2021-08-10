from django.contrib import admin
from ads.models import Ad
# Register your models here.

# Define the PicAdmin class
class AdAdmin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')


# Register the admin class with the associated model
admin.site.register(Ad, AdAdmin)