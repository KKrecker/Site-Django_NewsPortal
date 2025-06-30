from django.contrib import admin
from .models import Post, News, Advertisement,Offer
# Register your models here.

admin.site.register(Post)
admin.site.register(News)
admin.site.register(Advertisement)
admin.site.register(Offer)