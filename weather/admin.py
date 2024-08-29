from django.contrib import admin
from .models import Reading



class ReadingAdmin(admin.ModelAdmin):
    list_display = ('id','temperature','time','humidity')
    # list_per_page = 7
    # list_max_show_all = 7
    
admin.site.register(Reading,ReadingAdmin)

# Register your models here.
