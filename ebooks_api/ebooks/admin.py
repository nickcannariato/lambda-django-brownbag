from django.contrib import admin

from .models import Ebook, Review


@admin.register(Ebook, Review)
class EbookAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    pass
