from django.contrib import admin
from .models import CustomerLogin, OwnerLogin

# Register your models here.

admin.site.register([CustomerLogin, OwnerLogin])
