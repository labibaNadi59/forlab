from django.contrib import admin
from .models import CustomUser, Parent, Hospital


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Parent)
admin.site.register(Hospital)