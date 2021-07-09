from django.contrib import admin

# Register your models here.
from .models import Cat, Breed

class CatAdmin(admin.ModelAdmin):
      list_display = ('nickname','breed','weight')
      search_fields = ('nickname',)
      

class BreedAdmin(admin.ModelAdmin):
      search_fields = ('name',)
      def __str__(self):
            return self.name

admin.site.register(Breed, BreedAdmin)

admin.site.register(Cat, CatAdmin)