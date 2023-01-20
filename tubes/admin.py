from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from  .models import Tube, TubeBatch, TubeBatchPosition


class TubeAdmin(admin.ModelAdmin):
    list_filter = (
        ('created', DateFieldListFilter),
    )
admin.site.register(Tube, TubeAdmin)
admin.site.register(TubeBatch)
admin.site.register(TubeBatchPosition)