from django.contrib import admin

# Register your models here.



from .models import Make, Auto

class AutoAdmin(admin.ModelAdmin):
      list_display = ('nickname','mileage','make','comments')

class MakeAdmin(admin.ModelAdmin):
      
      def __str__(self):
            return self.name

admin.site.register(Make, MakeAdmin)

admin.site.register(Auto, AutoAdmin)