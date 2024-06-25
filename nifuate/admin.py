from django.contrib import admin
from .models import Logo,OnlineMember

# Register your models here.
admin.site.register(Logo)


class OnlineMemberAdmin(admin.ModelAdmin):
    list_display = ( 'phone_number','country' )

admin.site.register(OnlineMember, OnlineMemberAdmin)