from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import News

admin.site.register(News)
from .models import Book

admin.site.register(Book)
from .models import PurchaseDetail

admin.site.register(PurchaseDetail)
