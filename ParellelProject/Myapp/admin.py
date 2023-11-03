from django.contrib import admin
from Myapp.models import shopdb,productdb
from webapp.models import cartdb

# Register your models here.

admin.site.register(shopdb)
admin.site.register(productdb)
admin.site.register(cartdb)
