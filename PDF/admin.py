from django.contrib import admin
from .models import Profile
# Register your models here.

class profileAdmin(admin.ModelAdmin): 
    list_display = ('name', 'email', 'phone', 'degree', 'school', 'university', 'skills')



admin.site.register(Profile, profileAdmin)